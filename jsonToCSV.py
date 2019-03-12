import json
import csv

with open("C:/Users/abc/Desktop/DataDump.json") as file:
    data = json.load(file)

with open("C:/Users/abc/Desktop/datatweets.csv", "w") as file:
    csv_file = csv.writer(file)
    for item in data:
        csv_file.writerow([item['id'], item['text']] + item['user'].values())
