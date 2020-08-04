import csv

def csv_read(path):
	with open(path,encoding="utf-8_sig") as f:
		reader = csv.reader(f)
		return reader

def csv_terget(path):
	with open(path,encoding="utf-8_sig") as f:
		reader = csv.reader(f)
		for row in reader:
			if row[3] == "":
				return row[2]
		return
		
