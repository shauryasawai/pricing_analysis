from venv import create
from django.core.management.base import BaseCommand
from base.models import DosaWorldMenu  # Change this to the correct path of your model
import json

class Command(BaseCommand):
    help = 'Loads the Dosa menu into the database'

    def handle(self, *args, **kwargs):
        menu_items  = [
    {"name": "Garden Salad", "base_price": 4.99},
    {"name": "Katchumber Salad", "base_price": 4.99},
    {"name": "Rasam Soup", "base_price": 4.99},
    {"name": "Tomato Soup", "base_price": 4.99},
    {"name": "Mulligatawny Soup", "base_price": 4.99},
    {"name": "Spinach Soup", "base_price": 4.99},
    {"name": "Vegetable Soup", "base_price": 4.99},
    {"name": "Batata Vada, Samosa, Pakora & Bajjia", "base_price": 13.99},
    {"name": "Papadam", "base_price": 1.99},
    {"name": "Masala Spiced Cashew Nuts", "base_price": 5.99},
    {"name": "Behl Puri", "base_price": 5.99},
    {"name": "Paneer Pakora", "base_price": 6.99},
    {"name": "Gobi Manchurian", "base_price": 7.99},
    {"name": "Paneer Manchurian", "base_price": 8.99},
    {"name": "Alu Tikki", "base_price": 5.99},
    {"name": "Idli", "base_price": 5.99},
    {"name": "Idli in Rasam Bowl", "base_price": 6.99},
    {"name": "Idli in Sambar Bowl", "base_price": 6.99},
    {"name": "Mini Idli", "base_price": 5.99},
    {"name": "Mini Idli in Rasam Bowl", "base_price": 6.99},
    {"name": "Mini Idli in Sambar Bowl", "base_price": 6.99},
    {"name": "Ghee Fried Idli", "base_price": 6.99},
    {"name": "Idli Vada", "base_price": 5.99},
    {"name": "Idli Vada in Rasam Bowl", "base_price": 6.99},
    {"name": "Idli Vada in Sambar Bowl", "base_price": 6.99},
    {"name": "Medu Vada", "base_price": 5.99},
    {"name": "Medu Vada in Rasam Bowl", "base_price": 6.99},
    {"name": "Medu Vada in Sambar Bowl", "base_price": 6.99},
    {"name": "Dahi Vada", "base_price": 5.99},
    {"name": "Alu Chaat", "base_price": 5.99},
    {"name": "Chana Chaat", "base_price": 5.99},
    {"name": "Samosa Chaat", "base_price": 6.99},
    {"name": "Papri Chaat", "base_price": 6.99},
    {"name": "Alu Papri Chaat", "base_price": 6.25},
    {"name": "Rava Dosa", "base_price": 10.25},
    {"name": "Rava Masala Dosa", "base_price": 11.99},
    {"name": "Onion Rava Dosa", "base_price": 12.99},
    {"name": "Onion Rava Masala Dosa", "base_price": 13.99},
    {"name": "Mysore Rava Masala Dosa", "base_price": 13.99},
    {"name": "Rava Masala Dosa with Chili & Gunpowder", "base_price": 14.99},
    {"name": "Paneer Rava Masala Dosa", "base_price": 14.99},
    {"name": "Coconut Rava Masala Dosa", "base_price": 14.99},
    {"name": "Special Dosa World Rava Dosa", "base_price": 15.99},
    {"name": "Sada Dosa", "base_price": 9.99},
    {"name": "Set Dosa", "base_price": 7.99},
    {"name": "Set Masala Dosa", "base_price": 10.99},
    {"name": "Masala Dosa", "base_price": 10.99},
    {"name": "Ghee Sada Dosa", "base_price": 8.99},
    {"name": "Ghee Masala Dosa", "base_price": 11.99},
    {"name": "Paper Dosa", "base_price": 11.99},
    {"name": "Paper Masala Dosa", "base_price": 12.99},
    {"name": "Plain Uttapam", "base_price": 9.99},
    {"name": "Coconut Uttapam", "base_price": 11.99},
    {"name": "Paneer Uttapam", "base_price": 12.99},
    {"name": "Mushroom Uttapam", "base_price": 12.99},
    {"name": "Mixed Vegetable Uttapam", "base_price": 12.99},
    {"name": "Chili Cheese Uttapam", "base_price": 12.99},
    {"name": "Alu Palak", "base_price": 12.99},
    {"name": "Chana Masala", "base_price": 12.99},
    {"name": "Palak Paneer", "base_price": 13.99},
    {"name": "Malai Kofta", "base_price": 13.99},
    {"name": "North Indian Thali", "base_price": 19.99},
    {"name": "South Indian Thali", "base_price": 19.99},
    {"name": "Chapati", "base_price": 5.99},
    {"name": "Pulka", "base_price": 4.99},
    {"name": "Paratha", "base_price": 5.99},
    {"name": "Stuffed Paratha", "base_price": 7.99},
    {"name": "Poori", "base_price": 7.99},
    {"name": "Pulav", "base_price": 9.99},
    {"name": "Biryani", "base_price": 9.99},
    {"name": "Curd Rice", "base_price": 8.99},
    {"name": "Thums Up", "base_price": 3.00},
    {"name": "Fanta", "base_price": 3.00},
    {"name": "Mango Lassi", "base_price": 6.75}
    ]
        for item in menu_items:
            if not DosaWorldMenu.objects.filter(name=item['name']).exists():
                DosaWorldMenu.objects.create(
                    name=item['name'],
                    base_price=item['base_price']
                    )
                self.stdout.write(self.style.SUCCESS(f'Successfully added {item["name"]}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'{item["name"]} already exists'))