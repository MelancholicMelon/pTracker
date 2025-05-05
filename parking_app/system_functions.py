from .models import RegisteredUser, ParkingLot
from django.core.exceptions import ObjectDoesNotExist
import csv

def deduct_points(user: RegisteredUser, points: int) -> bool:
    try:
        user.points -= points
        user.save()
        return True
    except ObjectDoesNotExist:
        return False

def award_points(user: RegisteredUser, points: int) -> bool:
    try:
        user.points += points
        user.save()
        return True
    except ObjectDoesNotExist:
        return False

def view_points(user: RegisteredUser) -> int:
    try:
        return user.points
    except ObjectDoesNotExist:
        return 0

def autoban(user: RegisteredUser) -> bool:
    try:
        user.is_banned = True
        user.save()
        return True
    except ObjectDoesNotExist:
        return False

def send_warnings(user: RegisteredUser) -> bool:
    try:
        # Implement warning sending logic
        user.warnings += 1
        user.save()
        return True
    except ObjectDoesNotExist:
        return False

def process_image(image) -> bool:
    try:
        # Implement image processing logic
        return True
    except Exception as e:
        return False

def issue_warning(user: RegisteredUser) -> str:
    try:
        # Implement warning issuing logic
        return "Warning issued"
    except ObjectDoesNotExist:
        return "User not found"

def audit_user(user: RegisteredUser) -> str:
    try:
        # Implement user audit logic
        return f"Audit report for {user.username}"
    except ObjectDoesNotExist:
        return "User not found"

def generate_user_report(user: RegisteredUser) -> str:
    try:
        # Implement user report generation logic
        return f"Report for {user.username}"
    except ObjectDoesNotExist:
        return "User not found"

def generate_parking_report(parking: ParkingLot) -> str:
    try:
        # Implement parking report generation logic
        return f"Report for parking lot {parking.name}"
    except ObjectDoesNotExist:
        return "Parking lot not found"


def load_parking_data_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ParkingLot.objects.create(
                name=row['Name'] if row['Name'] != 'n/a' else None,
                latitude=row['Latitude'],
                longitude=row['Longitude'],
                description=None
            )