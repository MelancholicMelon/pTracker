from django.shortcuts import render, redirect
import datetime
import csv
import cv2
import numpy as np
import os

def survey(request):
    if request.method == 'POST':
        file_path = "./database/parkingDB_user.csv"

        name = request.POST.get('name', '')
        latitude = request.POST.get('latitude', '')
        longitude = request.POST.get('longitude', '')

        cars_checked = 'cars' in request.POST
        bike_checked = 'bike' in request.POST
        motor_checked = 'motor' in request.POST
        gentsuki_checked = 'gentsuki' in request.POST

        cars = '1' if cars_checked else '0'
        bike = '1' if bike_checked else '0'
        motor = '1' if motor_checked else '0'
        gentsuki = '1' if gentsuki_checked else '0'

        price = request.POST.get('price', '')
        unit_of_time = request.POST.get('unit_of_time', '')
        review = request.POST.get('review', '')
        current_free_spot = request.POST.get('current_free_spot', '')
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # variables for point calculation
        file_path_userDB = "./database/userDB.csv"
        tmp_path = './database/userDB.csv.tmp'
        file_path_user = './database/current_user_data.csv'
        userDB_header = ["UserType Flag","ID","Username","Password","Phone Number","Points"]

        uploader = request.POST.get('current_user', '')
        point = 5
        data_user = []
        new_data_user = []

        # Determine the new data_id by counting existing rows
        data_id = 0
        if os.path.exists(file_path):
            with open(file_path, mode='r', newline='') as parkDB:
                csv_reader = csv.reader(parkDB)
                data_id = sum(1 for row in csv_reader)

        image_path = "./database/images/"
        os.makedirs(image_path, exist_ok=True)
        file_name = f"{data_id}.png"
        full_image_path = os.path.join(image_path, file_name)

        # Initialize new_row
        new_row = [
            data_id, name, latitude, longitude,
            cars, bike, motor, gentsuki,
            price, unit_of_time, review, current_free_spot, timestamp, uploader, full_image_path
        ]

        # Handle image upload
        if 'image' in request.FILES:
            uploaded_image = request.FILES['image']
            opencv_image = cv2.imdecode(np.frombuffer(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)
            cv2.imwrite(full_image_path, opencv_image)
        else:
            full_image_path = "None"

        # Update new_row with the actual image path
        new_row[-1] = full_image_path

        # Write the new row to the CSV file
        with open(file_path, mode='a', newline='') as parkDB:
            csv_writer = csv.writer(parkDB)
            csv_writer.writerow(new_row)
            
        # calculate point and update
        if full_image_path != 'None':
            point = 15

        with open(file_path_userDB, mode="r", newline="") as userDB:
            csv_reader = csv.reader(userDB)
            next(csv_reader)

            for row in csv_reader:
                data_user.append(row)
        
        for row in data_user:
            if row[2] == uploader:
                row[5] = int(row[5]) + point
                line = row
            new_data_user.append(row)
        
        with open(tmp_path, mode="w", newline='') as temp:
            csv_writer = csv.writer(temp)
            csv_writer.writerow(userDB_header)
            csv_writer.writerows(new_data_user)
        
        os.replace(tmp_path, file_path_userDB)

        with open(file_path_user, mode="w", newline="") as userdata:
            csv_writer = csv.writer(userdata)
            csv_writer.writerow(line)
        
        request.session['point'] = point
        
        return redirect('survey_success')
    
    else:
        return render(request, 'survey.html')

def survey_success(request):
    file_path = './database/parkingDB_user.csv'
    last_row = None
    points_awarded = request.session.get('point')


    if os.path.exists(file_path):
        with open(file_path, mode='r', newline='') as parkDB:
            csv_reader = csv.reader(parkDB)
            for row in csv_reader:
                last_row = row

    if last_row:
        context = {
            'name': last_row[1],
            'latitude': last_row[2],
            'longitude': last_row[3],
            'car': last_row[4],
            'bike': last_row[5],
            'motor': last_row[6],
            'gentsuki': last_row[7],
            'price': last_row[8],
            'unit_of_time': last_row[9],
            'review': last_row[10],
            'current_free_spot': last_row[11],
            'timestamp': last_row[12],
            'points_awarded' : points_awarded,
        }
    else:
        context = {
            'error_message': 'No data'
        }

    return render(request, 'survey_success.html', context)
