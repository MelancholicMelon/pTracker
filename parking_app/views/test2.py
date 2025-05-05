import csv
import random

file_path = "./database/ParkingDB_OSM.csv"
file_path_2 = "./database/ParkingDB_OSM2.csv"
header = ["ID", "Name", "Latitude", "Longitude", "Car", "Bicycle", "Motorcycle", "Gentsuki", "Price", "Unit of Time", "Review", "Current Free Spot", "Uploader", "Timestamp", "Image Path"]

park_data = []
new_data = []

with open(file_path, mode="r", encoding="utf-8") as db:
    csv_reader = csv.reader(db)
    next(csv_reader)

    for row in csv_reader:
        park_data.append(row)

for row in park_data:
    new_data.append([row[0], row[1], row[2], row[3], "None", "None", "None", "None", "None", "None","None", random.randint(0, 10), "None", "None", "None"])

with open(file_path_2, mode="w", newline="", encoding="utf-8") as new:
    csv_writer = csv.writer(new)
    csv_writer.writerow(header)
    csv_writer.writerows(new_data)