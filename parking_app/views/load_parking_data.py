import csv
from django.core.management.base import BaseCommand
from parking_app.models import ParkingLot, RegisteredUser

class Command(BaseCommand):
    help = 'Load parking lot and user data from CSV files'

    def handle(self, *args, **kwargs):
        self.load_parking_lot_data()
        self.load_user_data()

    def load_parking_lot_data(self):
        with open('path/to/ParkingDB OSM.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ParkingLot.objects.create(
                    name=row['name'],
                    latitude=row['latitude'],
                    longitude=row['longitude'],
                    description=row['description']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded parking lot data'))

    def load_user_data(self):
        with open('path/to/ParkingDB Users.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                RegisteredUser.objects.create(
                    username=row['username'],
                    email=row['email'],
                    points=row['points'],
                    is_banned=row['is_banned'],
                    warnings=row['warnings'],
                    report=row['report']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded user data'))
