import csv

def is_authenticated(request):
    file_path = './database/current_user_data.csv'
    user_data = []

    with open(file_path, mode = 'r', newline='') as userData:
        csv_reader = csv.reader(userData)
        for row in csv_reader:
            user_data = row
        
        if user_data:
            current_user={
                'user_flag': user_data[0],
                'user_id': user_data[1],
                'username': user_data[2],
                'phonenumber': user_data[4],
                'points': user_data[5]
            }
        else:
            current_user={}

    return {'current_user':current_user}