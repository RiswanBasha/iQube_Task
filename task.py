
'''
This is the basic code for creating a table and db . Just for showcase purpose..
'''


import sqlite3
conn = sqlite3.connect("csv.db")
cur=conn.cursor()

sql="""
    CREATE TABLE CsvTable(
        Id INTEGER,
        Date TEXT,
        Attachments TEXT,
        primary key(Id)
    )"""

cur.execute(sql)
print("CSV Db created")

conn.commit()
conn.close()