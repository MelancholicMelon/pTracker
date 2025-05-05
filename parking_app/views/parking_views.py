from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from ..models import ParkingLot
import csv

'''
def index(request):
    parking_lots = ParkingLot.objects.all()
    return render(request, 'index.html', {'parking_lots': parking_lots})
'''
def index(request):
    if request.method == 'POST':
        if request.POST.get('login') == 'guest_login':

            file_path = './database/current_user_data.csv'
            new_line = [0, "None", "Guest", "None", "None", "None"]

            with open(file_path, mode='a', newline='') as userData:
                csv_writer = csv.writer(userData)
                csv_writer.writerow(new_line)
            messages.success(request, "You Now Logged in as Guest!")
            return redirect('map_page')
        
        elif request.POST.get('login') == 'registered_user_login':
            file_path_db = "./database/userDB.csv"
            file_path_user = './database/current_user_data.csv'

            user_list = []
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')

            with open(file_path_db, mode='r', newline='') as userDB:
                csv_reader = csv.reader(userDB)
                user_list = list(csv_reader)
            
            user_data = None
            for row in user_list:
                if row[2] == username and row[3] == password:
                    user_data = row
                    break
            
            if user_data:
                messages.success(request, "Successfully Logged In!")

                with open(file_path_user, mode='a', newline='') as userData:
                    csv_writer = csv.writer(userData)
                    csv_writer.writerow(user_data)
        
                return redirect('map_page')
            else:
                messages.info(request, 'No such user exists')
                return render(request, 'index.html')
    return render(request, 'index.html')

def parking_detail(request, id):
    parking_lot = get_object_or_404(ParkingLot, id=id)
    reviews = parking_lot.review_set.all()
    return render(request, 'parking_detail.html', {'parking_lot': parking_lot, 'reviews': reviews})

def map_page(request):
    return render(request, 'map_page.html')