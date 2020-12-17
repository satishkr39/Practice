import csv

handle = open("flowers.csv")

reader = csv.reader(handle)

for item in reader:
    print(item)

