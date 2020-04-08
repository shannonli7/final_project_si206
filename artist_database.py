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

def main():
    cur, conn = setupdatabase("music_database.db")
    create_artist_table(cur, conn)


if __name__ == "__main__":
    main()