import csv

a = ('/Users/sakukou/Documents/学校/2020年長期休暇/プログラム設計法/village_g93.csv')

def csv_read(a):
	with open(a) as f:
		reader = csv.reader(f)
		l = [row for row in reader]

	return l

b = csv_read(a)
print(b)