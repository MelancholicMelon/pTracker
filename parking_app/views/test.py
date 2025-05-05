import csv

file_path = "./database/userDB.csv"
tmp_path = './database/userDB.csv.tmp'
file_path_user = './database/current_user_data.csv'
header = ["UserType Flag","ID","Username","Password","Phone Number","Points"]
username = "Wonil"

data = []
new_data = []

with open(file_path, mode="r", newline='') as userDB:
    csv_reader = csv.reader(userDB)
    next(csv_reader)

    for row in csv_reader:
        data.append(row)

for row in data:
    if row[2] == username:
        row[5] = int(row[5]) + 5
        line = row
    new_data.append(row)

with open(tmp_path, mode="w", newline="") as temp:
    csv_writer = csv.writer(temp)
    csv_writer.writerow(header)
    csv_writer.writerows(new_data)

import os
os.replace(tmp_path, file_path)

with open(file_path_user, mode='w', newline='') as userdata:
    csv_writer = csv.writer(userdata)
    csv_writer.writerow(line)