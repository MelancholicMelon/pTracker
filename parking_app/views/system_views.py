from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from ..system_functions import *
from ..models import ParkingLot  # Import ParkingLot model

def deduct_points_view(request):
    user = request.user
    points = int(request.GET.get('points', 0))
    success = deduct_points(user, points)
    return JsonResponse({'success': success})

def award_points_view(request):
    user = request.user
    points = int(request.GET.get('points', 0))
    success = award_points(user, points)
    return JsonResponse({'success': success})

def view_points_view(request):
    user = request.user
    points = view_points(user)
    return JsonResponse({'points': points})

def autoban_view(request):
    user = request.user
    success = autoban(user)
    return JsonResponse({'success': success})

def send_warnings_view(request):
    user = request.user
    success = send_warnings(user)
    return JsonResponse({'success': success})

def process_image_view(request):
    # Assume image is passed in request.FILES
    image = request.FILES['image']
    success = process_image(image)
    return JsonResponse({'success': success})

def issue_warning_view(request):
    user = request.user
    message = issue_warning(user)
    return JsonResponse({'message': message})

def audit_user_view(request):
    user = request.user
    report = audit_user(user)
    return JsonResponse({'report': report})

def generate_user_report_view(request):
    user = request.user
    report = generate_user_report(user)
    return JsonResponse({'report': report})

def generate_parking_report_view(request):
    parking_id = int(request.GET.get('parking_id', 0))
    parking = ParkingLot.objects.get(id=parking_id)
    report = generate_parking_report(parking)
    return JsonResponse({'report': report})

def load_parking_data_view(request):
    # Assuming the CSV file is stored in a static directory
    file_path = '/static/parking_app/data/ParkingDB_OSM.csv'
    load_parking_data_from_csv(file_path)
    return HttpResponse("Parking data loaded successfully.")