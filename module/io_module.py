import csv

def csv_read(path):
	with open(path,encoding="utf-8_sig") as f:
		reader = csv.reader(f)
		l = [row for row in reader]
	return l


def csv_terget(path):
	with open(path,encoding="utf-8_sig") as f:
		reader = csv.reader(f)
		for row in reader:
			if row[3] == "":
				return row[2]
		return
		
def csv_write(path,message):
	with open(path,encoding="utf-8_sig") as in_file:
		with open(path+".out.csv","w") as out_file:

			reader = csv.reader(in_file)
			writer = csv.writer(out_file)

			for row in reader:
				if row[3] == "":
					writer.writerow([row[0],row[1],row[2],message])
					return
				else:
					writer.writerow(row)
			return
