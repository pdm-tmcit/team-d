import csv

with open('/〇〇.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)