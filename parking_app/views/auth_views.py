# parking_app/views/auth_views.py
from django.shortcuts import render, redirect
from django.contrib import messages
import csv

def register(request):
    if request.method == 'POST':
        file_path = "./database/userDB.csv"

        user_data = []

        flag = 1
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        phonenumber = request.POST.get('phonenumber', '')
        point = 0

        with open(file_path, mode = 'r', newline='') as userDB:
            csv_reader = csv.reader(userDB)
            user_list = list(csv_reader)

        usernames = [row[2] for row in user_list]
        numbers = [row[4] for row in user_list]

        if username in usernames or phonenumber in numbers:
            messages.info(request,"User with input username and phone number already exists!")
            return render(request, 'register.html')
        else:
            user_id = len(user_list)
            new_row = [flag, user_id, username, password, phonenumber, point]

            with open(file_path, mode='a', newline='') as userDB:
                csv_writer = csv.writer(userDB)
                csv_writer.writerow(new_row)
            
            messages.info(request,"Register Successed!")

            return redirect('index')
        
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
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
            #messages.success(request, "Successfully Logged In!")

            with open(file_path_user, mode='a', newline='') as userData:
                csv_writer = csv.writer(userData)
                csv_writer.writerow(user_data)
        
            return redirect('map_page')
        else:
            messages.info(request, 'No such user exists')
            return render(request, 'login.html')
    
    return render(request, 'login.html')

def logout_view(request):
    file_path = './database/current_user_data.csv'

    with open(file_path, 'w') as user_data:
        pass

    return redirect('index')

def account_manage(request):
    file_path_userDB = './userDB.csv'
    return render(request, 'account_manage.html')

def forgot_password(request):
    if request.method == 'POST':
        file_path = './database/userDB.csv'
        username = request.POST.get('username', '')

        usernames = []
        with open(file_path, mode='r', encoding='utf-8-sig') as userDB:
            csv_reader = csv.reader(userDB)
            header = next(csv_reader)
            username_index = header.index('Username')
        
            for row in csv_reader:
                usernames.append(row[username_index])

        if username in usernames:
            request.session['username'] = username
            return redirect('set_new_pw')
        else:
            messages.info(request, "No such user")
    return render(request, "forgot_password.html")

def set_new_pw(request):
    username = request.session.pop("username", '')

    if request.method == 'POST':
        username = request.POST.get('username', '')
        new_password = request.POST.get("password", '')
        file_path = './database/userDB.csv'
        tmp_path = './database/userDB.csv.tmp'
        header = ['UserType Flag','ID','Username','Password','Phone Number','Points']
        user_data = []

        with open(file_path, 'r', newline='', encoding='utf-8') as userDB:
            csv_reader = csv.reader(userDB)
            next(csv_reader)
            for row in csv_reader:
                user_data.append(row)
    
        for row in user_data:
            if row[2] == username:
                row[3] = new_password
                break
        
        with open(tmp_path, mode="w", newline="") as temp:
            csv_writer = csv.writer(temp)
            csv_writer.writerow(header)
            csv_writer.writerows(user_data)
        
        import os
        os.replace(tmp_path, file_path)
        return redirect('index')
    
    return render(request,'set_new_pw.html', {'username':username} )
        