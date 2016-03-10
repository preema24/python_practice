#user/bin/python
import MySQLdb
import csv
import argparse
import sys


connection = MySQLdb.connect(host='localhost', port=3306, user='codaxtr_user', passwd='c0d@xtr', db='codaxtr')
cursor = connection.cursor()
cursor.execute("select p.id, p.fullname, u.id,u.unresolved_party_type_name from party p inner join unresolved_party_type u on u.id=p.id order by p.id ")


records_tuple = cursor.fetchall()
	

for i in party
	if i == 0:
		wf += open('preemas_csv.csv', 'w',newline='')
		csv_writer = csv.writer(wf, delimiter =',', quotechar='"')
		for record in records_tuple:
			csv_writer.writerow(list(record))
	if i == 1000:
		wf += open('preemas_csv1.csv', 'w',newline='')
		csv_writer = csv.writer(wf, delimiter =',', quotechar='"')
		for record in records_tuple:
			csv_writer.writerow(list(record))
wf.close()
