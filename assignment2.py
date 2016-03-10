#user/bin/python
import MySQLdb
import csv
import argparse
import sys


connection = MySQLdb.connect(host='localhost', port=3306, user='codaxtr_user', passwd='c0d@xtr', db='codaxtr')
cursor = connection.cursor()
cursor.execute("select p.id, p.fullname, u.id,u.unresolved_party_type_name from party p inner join unresolved_party_type u on u.id=p.id order by p.id limit 100;")


records_tuple = cursor.fetchall()
	


wf = open('preemas_csv.csv', 'w')
csv_writer = csv.writer(wf, delimiter =',', quotechar='"')
for record in records_tuple:
	csv_writer.writerow(list(record))

wf.close()
