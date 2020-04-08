import unittest
import sqlite3
import json
import os

def setupdatabase(database_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+database_name)
    cur = conn.cursor()
    return cur, conn

def create_followers_table(filename, cur, conn):
    filobj = open(filename)
    filedata = filobj.read()
    filobj.close()
    json_data = json.loads(filedata)

    cur.execute("DROP TABLE IF EXISTS Followers")
    cur.execute("CREATE TABLE Followers (artist_uri TEXT PRIMARY KEY, artist_name TEXT, followers INTEGER)")
    for dictionary in json_data:
        artist_uri = dictionary ["artist_uri"]
        artist_name = dictionary ["name"]
        followers = dictionary ["followers"]
        cur.execute("INSERT INTO Followers (artist_uri,artist_name, followers) VALUES (?,?,?)",(artist_uri,artist_name, followers))
    conn.commit()


def main():
    cur, conn = setupdatabase("music_database.db")
    create_followers_table("data.json", cur, conn)

if __name__ == "__main__":
    main()
