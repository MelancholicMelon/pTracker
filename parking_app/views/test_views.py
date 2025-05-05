from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from ..models import RegisteredUser, ParkingLot

def test_leave_comment(request, user_id, parking_id):
    user = get_object_or_404(RegisteredUser, id=user_id)
    parking = get_object_or_404(ParkingLot, id=parking_id)
    success = user.leave_comment(parking)
    return JsonResponse({'success': success})

def test_report_info(request, user_id, parking_id):
    user = get_object_or_404(RegisteredUser, id=user_id)
    parking = get_object_or_404(ParkingLot, id=parking_id)
    success = user.report_info(parking)
    return JsonResponse({'success': success})

def test_upload_parking(request, user_id):
    user = get_object_or_404(RegisteredUser, id=user_id)
    # Assuming we create a new parking lot for testing
    parking = ParkingLot.objects.create(name="Test Parking", latitude=0.0, longitude=0.0, description="Test Description")
    success = user.upload_parking(parking)
    return JsonResponse({'success': success, 'parking_id': parking.id})

def test_edit_parking(request, user_id, parking_id):
    user = get_object_or_404(RegisteredUser, id=user_id)
    parking = get_object_or_404(ParkingLot, id=parking_id)
    success = user.edit_parking(parking)
    return JsonResponse({'success': success})

def test_leave_review(request, user_id, parking_id):
    user = get_object_or_404(RegisteredUser, id=user_id)
    parking = get_object_or_404(ParkingLot, id=parking_id)
    success = user.leave_review(parking, rating=5.0, comment="Great parking!")
    return JsonResponse({'success': success})

def test_page(request):
    return render(request, 'test_page.html')