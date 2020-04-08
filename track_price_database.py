import unittest
import sqlite3
import json
import os

def setupdatabase(database_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+database_name)
    cur = conn.cursor()
    return cur, conn
   
def create_track_price_table(filename, cur, conn):
    filobj = open(filename)
    filedata = filobj.read()
    filobj.close()
    json_data = json.loads(filedata)
    cur.execute("DROP TABLE IF EXISTS trackprice")
    cur.execute("CREATE TABLE trackprice (artist_name TEXT, track_name TEXT, track_price INTEGER)")

    for dictionary in json_data:
        artist_name = dictionary ["name"]
        track_name = dictionary ["tracks"]
        track_price = dictionary ["trackprice"]
        for i in range(10):
            cur.execute("INSERT INTO trackprice (artist_name, track_name, track_price) VALUES (?,?,?)",(artist_name, track_name[i], track_price[i]))
    conn.commit()

def main():

    create_track_price_table("data.json", cur, conn)

if __name__ == "__main__":
    main()