import sqlite3
import networkx

con = sqlite3.connect('streaming-markets.db')
cur = con.cursor()
cmd = "select Close, High, Low from Streaming"
cur.execute(cmd)

rows = cur.fetchall()

while True:

    for row in rows:
        print(row[1])

    con.close()
