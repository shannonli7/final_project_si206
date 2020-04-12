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

    cur.execute("CREATE TABLE IF NOT EXISTS Artists (artist_uri TEXT PRIMARY KEY, artist_name TEXT)")
    for i in range(10):
        #insert of ignore prevents duplicate keys
        cur.execute("INSERT OR IGNORE INTO Artists (artist_uri,artist_name) VALUES (?,?)",(artist_uri[i],artists[i]))
    conn.commit()

def create_followers_table(filename, cur, conn):
    filobj = open(filename)
    filedata = filobj.read()
    filobj.close()
    json_data = json.loads(filedata)

    cur.execute("CREATE TABLE IF NOT EXISTS Followers (artist_uri TEXT PRIMARY KEY, artist_name TEXT, followers INTEGER)")
    for dictionary in json_data:
        artist_uri = dictionary ["artist_uri"]
        artist_name = dictionary ["name"]
        followers = dictionary ["followers"]
        cur.execute("INSERT OR IGNORE INTO Followers (artist_uri,artist_name, followers) VALUES (?,?,?)",(artist_uri,artist_name, followers))
    conn.commit()

#limited to 20 data added each time, REFRESH DATABASE AFTER EXECUTING THE FILE, and 20 data will be added each
def create_track_price_table(filename, cur, conn):
    filobj = open(filename)
    filedata = filobj.read()
    filobj.close()
    json_data = json.loads(filedata)
    cur.execute("CREATE TABLE IF NOT EXISTS trackprice (artist_name TEXT, track_name TEXT, track_price INTEGER)")

    count = 0
    index = 0
    
    while count < 2:
        if index >= 10:
            print("Delete music_database.db and run again!")
            exit()
        artist_name = json_data[index]["name"]
        track_name = json_data[index]["tracks"]
        # print(index)
        # print(track_name)
        track_price = json_data[index]["trackprice"]
        #say we have The 1975 set to artist_name, we check the table and it is there, we proceed
        #to go to the next artist by the if row statement
        #if not there, we should grab data and insert it
        cur.execute("SELECT artist_name FROM trackprice WHERE artist_name = ?" , (artist_name, ))
        row = cur.fetchone()

        #the 1975 is here already, so we go to the next artist and its already there, so move on, which is why
        #index does not have a limit, and only count
        if row:
            index += 1
            continue

        else:
            for i in range(10):
                cur.execute("INSERT INTO trackprice (artist_name, track_name, track_price) VALUES (?,?,?)",(artist_name, track_name[i], track_price[i]))
            #we want to to go the next artist and we also want to increment count for data purposes
            count += 1
            index += 1

        
    conn.commit()

def create_recommendations_table(filename, cur, conn):
    filobj = open(filename)
    filedata = filobj.read()
    filobj.close()
    json_data = json.loads(filedata)
    #if we add rec for 2 artist, we add only 20 items (At A TIME)

    #create table is not exists b/c we don't want to lose the data or overwrite the data
    #only clear table if it does not exist
    cur.execute("CREATE TABLE IF NOT EXISTS Recommendations (artist_name TEXT, recommended_artist TEXT)")

    #counter -> don't add data for more than two artist (or more than 20 recs)
    count = 0
    #index for the data read in cache file (data.json) and move from one artist to the next in the list of dictionary
    index = 0
    
    while count < 2:
        if index >= 10:
            print("Delete music_database.db and run again!")
            exit()
        #move to next artist when data has been added
        artist_name = json_data[index]["name"]
        recommended_artists = json_data[count]["recommendations"]
        #check if artist name detail if in rec table already
        cur.execute("SELECT artist_name FROM Recommendations WHERE artist_name = ?" , (artist_name, ))
        #if we find data, then we already added the 10 
        #if we find one row, or one of the artist name, it is implied that we have the other 9 data has been added
        row = cur.fetchone()
        #only update counter when data is added to database

        if row:
            #go to the next artist -> index
            #make sure data is added -> counter
            index += 1
            continue
        #no artist found, we add all the recommended data for that artist
        else:
            #insert all recommended artist and go to counter to the next artist
            for i in range(10):
                cur.execute("INSERT INTO Recommendations (artist_name, recommended_artist) VALUES (?,?)",(artist_name,recommended_artists[i]))
            #data has been added
            count += 1
            #move to the next artist
            index += 1
    conn.commit()

def average_track_price(in_filename, cur, conn, out_filename):
    
    #Selecting the artist name that exists on every page in the database and the trackprice from the track price apge
    cur.execute("SELECT Artists.artist_name, trackprice.track_price FROM Artists LEFT JOIN trackprice ON Artists.artist_name = trackprice.artist_name ORDER BY Artists.artist_name")
    database_info = cur.fetchall()

    #opening original file to match up artist names witha rtist name in the database - just to double check we are getting correct artists
    filobj = open(in_filename)
    filedata = filobj.read()
    filobj.close()
    json_data = json.loads(filedata)
    #list of artist names
    artists = []
    for d in json_data:
        artists.append(d["name"])

    if len(database_info) == 100:
        #adding up track prices for each artist and counting how many tracks there are for eacha rtist 
        #then averaging the track price per artist
        average_per_artist = []   
        for artist in artists:
            total_trackprice = 0 
            track_count = 0
            for tup in database_info:
                if tup[0] == artist:
                    total_trackprice += tup[1]
                    track_count += 1
            average = total_trackprice / track_count
            average_per_artist.append((artist, average))

        #print(average_per_artist)
        #write the information to a file
        out_file = open(out_filename, "w")
        for t in average_per_artist:
            out_file.write("{},{}\n".format(t[0],t[1]))
        out_file.close()
    else:
        pass
    
    

def main():
    cur, conn = setupdatabase("music_database.db")
    create_artist_table(cur, conn)
    create_followers_table("data.json", cur, conn)
    create_track_price_table("data.json", cur, conn)
    create_recommendations_table("data.json", cur, conn)
    average_track_price("data.json", cur, conn, "average_track_price_per_artist.txt")

if __name__ == "__main__":
    main()