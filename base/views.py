# views.py
from django.shortcuts import render
from .models import MenuItem
from django.http import HttpResponse
from .utils import fetch_weather_data, is_busy_time
from .ml import train_price_model, predict_price
from .models import DosaWorldMenu

def menu(request):
    items = MenuItem.objects.all()
    return render(request, "base/menu.html", {"items": items})


def update_prices(request):
    # Fetch weather data
    weather = fetch_weather_data()
    # Determine if the restaurant is busy
    busy = is_busy_time()

    # Train the ML model (this should have been done in a separate step, not every time)
    model, rain_encoder = train_price_model()

    # Check if the price should be adjusted based on weather or busy status
    if weather["temperature"] < 45 or "rain" in weather["weather"] or busy:
        items = MenuItem.objects.all()
        for item in items:
            # Convert base_price to float to avoid the Decimal * float error
            base_price_float = float(item.base_price)

            # Pass all required arguments to predict_price
            new_price = predict_price(
                model, 
                rain_encoder,  # Rain encoder used to encode the rain condition
                weather["temperature"],  # Current temperature
                weather["weather"],  # Rain condition (e.g., 'moderate')
                busy,  # Whether the restaurant is busy (1 for busy, 0 for not busy)
                base_price_float  # Convert base_price to float before passing it to the model
            )
            item.adjusted_price = round(new_price, 2)  # Update the adjusted price
            item.save()  # Save the updated menu item

    return HttpResponse("Prices updated successfully!")

# views.py


def compare_prices(request):
    # Fetch all items from DosaWorldMenu and VillageMenu
    dosa_world_items = DosaWorldMenu.objects.all()
    village_items = MenuItem.objects.all()

    # Prepare a list to store the items that are available in both restaurants
    matching_items = []

    for dosa_item in dosa_world_items:
        # Check if the item is available in both restaurants
        try:
            village_item = village_items.get(name=dosa_item.name)

            # Compare the prices and get the minimum price
            min_price = min(dosa_item.base_price, village_item.base_price)

            # Add the item with the lowest price to the list
            matching_items.append({
                'name': dosa_item.name,
                'village_price': village_item.base_price,
                'dosa_price': dosa_item.base_price,
                'min_price': min_price
            })

        except MenuItem.DoesNotExist:
            continue

    return render(request, 'base/compare_prices.html', {'matching_items': matching_items})
