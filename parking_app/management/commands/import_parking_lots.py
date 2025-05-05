# import_random_parking_lots.py

import random
import string
from django.core.management.base import BaseCommand
from parking_app.models import ParkingLot  # Replace 'yourapp' with your actual app name

class Command(BaseCommand):
    help = 'Generates 100 random parking lot entries and saves them to the database'

    def handle(self, *args, **kwargs):
        for _ in range(100):
            # Generate random data for each field
            name = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 15)))
            latitude = random.uniform(-90, 90)
            longitude = random.uniform(-180, 180)
            vehicle_type = random.choice(['Car', 'Bicycle', 'Motorcycle', 'Gentsuki'])
            price = round(random.uniform(5.0, 50.0), 2)
            unit_of_time = random.choice(['30', '45', '60'])
            reviews = 'Random review text'
            current_free_spot = random.randint(0, 20)

            # Create a ParkingLot object and save it to the database
            parking_lot = ParkingLot.objects.create(
                name=name,
                latitude=latitude,
                longitude=longitude,
                vehicle_type=vehicle_type,
                price=price,
                unit_of_time=unit_of_time,
                reviews=reviews,
                current_free_spot=current_free_spot
            )

            self.stdout.write(self.style.SUCCESS(f'Successfully created ParkingLot ID {parking_lot.id}'))
