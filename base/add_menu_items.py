# scripts/add_menu_items.py
from base.models import MenuItem

def add_menu_items():
    menu_items = [
        {"name": "Rasam", "base_price": 4.95},
        {"name": "Sambar", "base_price": 4.95},
        {"name": "Mulligatawny Soup", "base_price": 4.95},
        {"name": "Garden Soup", "base_price": 4.95},
        {"name": "Kachumbar Salad", "base_price": 4.95},
        {"name": "Garden Salad", "base_price": 4.95},
        {"name": "Veg Manchow Soup", "base_price": 4.95},
        {"name": "Tomato Soup", "base_price": 4.95},
        {"name": "Idly", "base_price": 5.95},
        {"name": "Masala Idly", "base_price": 7.95},
        {"name": "Mini Idly", "base_price": 5.95},
        {"name": "Ghee Fried Idly", "base_price": 7.95},
        {"name": "Chilli Idly", "base_price": 7.95},
        {"name": "Idly in Sambar Bowl", "base_price": 6.95},
        {"name": "Idly in Rasam Bowl", "base_price": 6.95},
        {"name": "Medu Vada", "base_price": 5.95},
        {"name": "Medu Vada in Sambar Bowl", "base_price": 5.99},
        {"name": "Masala Vada", "base_price": 5.95},
        {"name": "Spring Rolls", "base_price": 5.95},
        {"name": "Paneer Pakoda", "base_price": 6.95},
        {"name": "Samosa", "base_price": 4.95},
        {"name": "Bhel Puri", "base_price": 6.95},
        {"name": "Samosa Chat", "base_price": 6.95},
        {"name": "Veg Hakka Noodles", "base_price": 9.95},
        {"name": "Veg Fried Rice", "base_price": 9.95},
        {"name": "Sada Dosa", "base_price": 8.95},
        {"name": "Masala Dosa", "base_price": 9.95},
        {"name": "Mysore Masala Dosa", "base_price": 9.95},
        {"name": "Onion Rava Masala Dosa", "base_price": 11.95},
        {"name": "South Indian Thali", "base_price": 15.95},
        {"name": "North Indian Thali", "base_price": 15.95},
        {"name": "Roti", "base_price": 3.95},
        {"name": "Dum Biryani", "base_price": 11.95},
        {"name": "Veg Pullav", "base_price": 9.95},
        {"name": "Jeera Rice", "base_price": 9.95},
        {"name": "Lemon Rice", "base_price": 9.95},
        {"name": "Tamarind Rice", "base_price": 9.95},
        {"name": "Vangi Bhath", "base_price": 9.95},
        {"name": "B.B.B Bishibilabath", "base_price": 9.95},
        {"name": "Tomato Rice", "base_price": 9.95},
        {"name": "Coconut Rice", "base_price": 9.95},
        {"name": "Yogurt Rice", "base_price": 9.95},
        {"name": "Gulab Jamun", "base_price": 4.95},
        {"name": "Rasamalai", "base_price": 4.95},
        {"name": "Kheer", "base_price": 4.95},
        {"name": "Semiya Payasam", "base_price": 4.95},
        {"name": "Badam Halwa", "base_price": 5.95},
        {"name": "Kulfi Malai", "base_price": 4.95},
        {"name": "Halwa with Ice Cream", "base_price": 6.95},
        {"name": "Soda- Coke, D. Coke, Thumps up, Limca sprite, Ginger / Water", "base_price": 2.95},
        {"name": "Lassi-Mango", "base_price": 4.95},
        {"name": "Hot Drink-Madras Coffee", "base_price": 2.95},
        {"name": "Shakes -Vennila", "base_price": 4.95},
        {"name": "D. Coke", "base_price": 1.95},
        {"name": "Sprite", "base_price": 1.95},
        {"name": "Ginger", "base_price": 1.95},
        {"name": "water", "base_price": 1.95},
        {"name": "Lassi- Sweet", "base_price": 4.95},
        {"name": "Lassi- Salted", "base_price": 4.95},
        {"name": "Lassi- Chaas", "base_price": 4.95},
        {"name": "Hot Drink-Masala Tea", "base_price": 2.95},
        {"name": "Hot Drink- Herbal Tea", "base_price": 2.95},
        {"name": "Shakes - Mango", "base_price": 4.95},
        {"name": "Shakes -Chikoo", "base_price": 4.95},
    ]

    for item in menu_items:
        MenuItem.objects.get_or_create(
            name=item["name"], 
            defaults={
                "base_price": item["base_price"], 
                "adjusted_price": item["base_price"]
            }
        )
    print("Menu items added successfully!")
