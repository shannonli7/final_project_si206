import unittest
import sqlite3
import json
import os

def setupdatabase(database_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+database_name)
    cur = conn.cursor()
    return cur, conn

def create_recommendations_table(filename, cur, conn):
    filobj = open(filename)
    filedata = filobj.read()
    filobj.close()
    json_data = json.loads(filedata)
    cur.execute("DROP TABLE IF EXISTS Recommendations")
    cur.execute("CREATE TABLE Recommendations (artist_name TEXT, recommended_artist TEXT)")
    
    for num in range(8,10):
        dictionary = json_data[num]
        artist_name = dictionary ["name"]
        recommended_artists = dictionary ["recommendations"]
        for i in range(10):
            cur.execute("INSERT INTO Recommendations (artist_name, recommended_artist) VALUES (?,?)",(artist_name,recommended_artists[i]))
 
    conn.commit()

def main():
    cur, conn = setupdatabase("music_database.db")
    create_recommendations_table("data.json", cur, conn)

if __name__ == "__main__":
    main()