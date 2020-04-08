import unittest
import sqlite3
import json
import os

def setupdatabase(database_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+database_name)
    cur = conn.cursor()
    return cur, conn

def create_artist_table(cur, conn):

    artist_uri = ["spotify:artist:3mIj9lX2MWuHmhNCA7LSCW", "spotify:artist:3IunaFjvNKj98JW89JYv9u", 
    "spotify:artist:2eam0iDomRHGBypaDQLwWI", "spotify:artist:5JZ7CnR6gTvEMKX4g70Amv", "spotify:artist:536BYVgOnRky0xjsPT96zl", 
    "spotify:artist:4Uc8Dsxct0oMqx0P6i60ea", "spotify:artist:0Ya43ZKWHTKkAbkoJJkwIB", "spotify:artist:6d4jrmreCmsenscuieJERc", 
    "spotify:artist:0szWPxzzE8DVEfXFRCLBUb", "spotify:artist:163tK9Wjr9P9DmM0AVK7lm"]

    artists = ["The 1975", "The Japanese House", "Bleachers", "Lauv", 
    "Two Door Cinema Club", "Conan Gray", "The Wombats", "The Band CAMINO", 
    "Flor", "Lorde"]

    cur.execute("DROP TABLE IF EXISTS Artists")
    cur.execute("CREATE TABLE Artists (artist_uri TEXT PRIMARY KEY, artist_name TEXT)")
    for i in range(10):
        cur.execute("INSERT INTO Artists (artist_uri,artist_name) VALUES (?,?)",(artist_uri[i],artists[i]))
    conn.commit()

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

def create_recommendations_table(filename, cur, conn):
    filobj = open(filename)
    filedata = filobj.read()
    filobj.close()
    json_data = json.loads(filedata)
    cur.execute("DROP TABLE IF EXISTS Recommendations")
    cur.execute("CREATE TABLE Recommendations (artist_name TEXT, recommended_artist TEXT)")

    for dictionary in json_data:
        artist_name = dictionary ["name"]
        recommended_artists = dictionary ["recommendations"]
        for i in range(10):
            cur.execute("INSERT INTO Recommendations (artist_name, recommended_artist) VALUES (?,?)",(artist_name,recommended_artists[i]))
 
    conn.commit()

def main():
    cur, conn = setupdatabase("music_database.db")
    create_artist_table(cur, conn)
    create_followers_table("data.json", cur, conn)
    create_track_price_table("data.json", cur, conn)
    create_recommendations_table("data.json", cur, conn)

if __name__ == "__main__":
    main()