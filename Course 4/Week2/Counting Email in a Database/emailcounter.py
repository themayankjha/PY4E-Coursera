#!/usr/bin/python3

import sqlite3
import re
con=sqlite3.connect("email.sqlite")
cur=con.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")
filename=input("Enter name of the file")
if len(filename)<1 :
	filename="mbox.txt"
filehandle=open(filename)
for line in filehandle:
	if not line.startswith('From: '): continue
	for org in re.findall('[a-zA-Z0-9.]@([a-zA-Z0-9.]+)',line):
		cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
		row = cur.fetchone()
		if row is None:
			cur.execute('INSERT INTO Counts (org, count)VALUES (?, 1)', (org,))
		else:
			cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))
con.commit()
print("*******Saved To Database*******")
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()
