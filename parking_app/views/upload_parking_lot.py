from django.shortcuts import render
from django.http import JsonResponse
from parking_app.models import ParkingLot
from parking_app.forms import ParkingLotForm

def upload_parking_lot(request):
    if request.method == 'POST':
        form = ParkingLotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ParkingLotForm()
    return render(request, 'parking_app/upload_parking_lot.html', {'form': form})
