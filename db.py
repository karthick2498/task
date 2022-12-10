import cx_Oracle
con = cx_Oracle.connect('task1/admin123@127.0.0.1/xe')
print(con)
cur = con.cursor()
cur.execute('select * from elg1')
print(cur.fetchall())
con.commit()
con.close()
