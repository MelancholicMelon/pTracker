from django.shortcuts import render, redirect, get_object_or_404
from ..models import ParkingLot, Review
from django.contrib.auth.decorators import login_required

@login_required
def add_review(request, id):
    parking_lot = get_object_or_404(ParkingLot, id=id)
    if request.method == 'POST':
        rating = request.POST['rating']
        comment = request.POST['comment']
        review = Review(user=request.user, parking_lot=parking_lot, rating=rating, comment=comment)
        review.save()
        return redirect('parking_detail', id=id)
    return render(request, 'add_review.html', {'parking_lot': parking_lot})