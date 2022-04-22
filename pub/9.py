import sqlite3

connection = sqlite3.connect('ds_DB.sl3', 5)
cur = connection.cursor()
#cur.execute("INSERT INTO first_table (name) VALUES ('Nick');")

#cur.execute("INSERT INTO first_table (name) VALUES ('Bogdan');")

#cur.execute("INSERT INTO first_table (name) VALUES ('Kats');")

#cur.execute("UPDATE first_table SET name='Kate' WHERE rowid=3;")

#cur.execute("DELETE FROM first_table WHERE rowid = 1")
cur.execute("CREATE TABLE weather (date TEXT);")
cur.execute("CREATE TABLE weather (weather TEXT);")
#connection.commit()
#res = cur.fetchall()
#print(res)
#print(type(res))
connection.close()
