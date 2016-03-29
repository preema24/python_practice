import MySQLdb
import csv
import argparse
import pdb
import sys
 
connection = MySQLdb.connect(host='localhost', port=3306, user='codaxtr_user', passwd='c0d@xtr', db='codaxtr')
cursor = connection.cursor ()
offset=0

while True:
	q="select p.id,p.fullname,u.id,u.unresolved_party_type_name from party p inner join unresolved_party_type u on u.id=p.id \
	order by p.id limit 1000 offset %s" %offset
	cursor.execute(q)
	data = cursor.fetchall ()
	if not data:
		break
		for record in data:
			wf = open('preemas_csv.csv', 'w')
			csv_writer = csv.writer(wf, delimiter =',', quotechar='"')
			csv_writer.writerow(record)
			wf.close()
offset=offset+1000
cursor.close ()
connection.close()
sys.exit()
