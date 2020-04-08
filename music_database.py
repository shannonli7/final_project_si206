import unittest
import sqlite3
import json
import os

def setupdatabase(database_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def create_artist_table(cur, conn):

    artist_uri = ["spotify:artist:3mIj9lX2MWuHmhNCA7LSCW", "spotify:artist:3IunaFjvNKj98JW89JYv9u", 
    "spotify:artist:2eam0iDomRHGBypaDQLwWI", "spotify:artist:5JZ7CnR6gTvEMKX4g70Amv", "spotify:artist:536BYVgOnRky0xjsPT96zl", 
    "spotify:artist:4Uc8Dsxct0oMqx0P6i60ea", "spotify:artist:0Ya43ZKWHTKkAbkoJJkwIB", "spotify:artist:6d4jrmreCmsenscuieJERc", 
    "0szWPxzzE8DVEfXFRCLBUb", "spotify:artist:163tK9Wjr9P9DmM0AVK7lm"]

    artists = ["The 1975", "The Japanese House", "Bleachers", "Lauv", 
    "Two Door Cinema Club", "Conan Gray", "The Wombats", "The Band CAMINO", 
    "Flor", "Lorde"]

    cur.execute("DROP TABLE IF EXISTS Artists")
    cur.execute("CREATE TABLE Artists (artist_uri TEXT PRIMARY KEY, artist_name TEXT)")
    for i in range(10):
        cur.execute("INSERT INTO Artists (artist_uri,artist_name) VALUES (?,?)",(artist_uri[i],artists[i]))
    conn.commit()

def create_followers_table(cur, conn):

    artist_uri = ["spotify:artist:3mIj9lX2MWuHmhNCA7LSCW", "spotify:artist:3IunaFjvNKj98JW89JYv9u", 
    "spotify:artist:2eam0iDomRHGBypaDQLwWI", "spotify:artist:5JZ7CnR6gTvEMKX4g70Amv", "spotify:artist:536BYVgOnRky0xjsPT96zl", 
    "spotify:artist:4Uc8Dsxct0oMqx0P6i60ea", "spotify:artist:0Ya43ZKWHTKkAbkoJJkwIB", "spotify:artist:6d4jrmreCmsenscuieJERc", 
    "0szWPxzzE8DVEfXFRCLBUb", "spotify:artist:163tK9Wjr9P9DmM0AVK7lm"]

    artists = ["The 1975", "The Japanese House", "Bleachers", "Lauv", 
    "Two Door Cinema Club", "Conan Gray", "The Wombats", "The Band CAMINO", 
    "Flor", "Lorde"]

    lst_followers = [3922606, 354715, 364344, 2589051, 1833816, 951347, 761801, 151465, 3648080, 5626478]
    cur.execute("DROP TABLE IF EXISTS Followers")
    cur.execute("CREATE TABLE Followers (artist_uri TEXT PRIMARY KEY, artist_name TEXT, followers INTEGER)")
    for i in range(10):
        cur.execute("INSERT INTO Followers (artist_uri,artist_name, followers) VALUES (?,?,?)",(artist_uri[i],artists[i], lst_followers[i]))
    conn.commit()

def create_track_price_table(cur, conn):
    artists = ["The 1975", "The Japanese House", "Bleachers", "Lauv", 
    "Two Door Cinema Club", "Conan Gray", "The Wombats", "The Band CAMINO", 
    "Flor", "Lorde"]

    track_prices1 = [1.29, 1.29, 1.29, 1.29, 1.29, 1.29, 1.99, 1.29, 1.99, 1.29]
    track_prices2 = [1.29, 1.29, 1.29, 1.29, 1.99, 1.29, 1.29, 1.99, 1.29, 1.29]
    track_prices3 = [1.29, 1.29, 1.99, 1.29, 1.00, 1.29, 1.29, 1.99, 1.29, 1.29]
    track_prices4 = [1.00, 1.29, 1.99, 1.29, 0.99, 0.99, 1.29, 1.99, 1.29, 1.29]
    track_prices5 = [1.29, 1.29, 1.29, 1.99, 1.29, 1.29, 1.00, 1.29, 1.29, 1.29]
    track_prices6 = [1.29, 1.99, 1.00, 1.29, 1.29, 1.99, 1.29, 1.29, 0.69, 1.29]
    track_prices7 = [1.29, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29]
    track_prices8 = [1.29, 1.29, 1.29, 0.99, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29]
    track_prices9 = [0.99, 1.29, 0.69, 1.29, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99]
    track_prices10 = [1.29, 1.29, 1.00, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29]

    tracks1 = ['Somebody Else', "It's Not Living (If It's Not With You)", 'Me & You Together Song', 'Love It If We Made It', 'The Birthday Party', 'Be My Mistake', 'TOOTIMETOOTIMETOOTIME', 'Sincerity Is Scary', 'Narcissist (feat. The 1975)', 'I Always Wanna Die (Sometimes)']
    tracks2 = ['Saw You In A Dream', 'Chewing Cotton Wool', 'Something Has to Change', "Maybe You're the Reason", 'Lilo', 'You Seemed so Happy', 'i saw you in a dream', 'Cool Blue', 'Landslide - Recorded At Spotify Studios NYC', 'Still']
    tracks3 = ['Rollercoaster', 'I Wanna Get Better', "Don't Take The Money", 'Goodmorning', 'Wake Me', "Let's Get Married", 'Like a River Runs', 'Wild Heart', 'I Miss Those Days', 'Entropy']
    tracks4 = 'I Like Me Better', 'Who (feat. BTS)', "i'm so tired...", "fuck, i'm lonely (with Anne-Marie)", 'Modern Loneliness', 'Mean It', 'Invisible Things', 'Make It Right (feat. Lauv)', 'Tattoos Together', 'Feelings']
    tracks5 = ['What You Know', 'Undercover Martyn', 'Something Good Can Work', 'Sun', 'Changing of the Seasons', 'I Can Talk', 'Are We Ready? (Wreck)', 'Sleep Alone', 'Talk - Single Edit', 'Next Year']
    tracks6 = ['Maniac', 'Crush Culture', 'Generation Why', 'The Story', 'Lookalike', 'Wish You Were Sober', 'Heather', 'Idle Town', 'The King', 'Comfort Crowd']
    tracks7 = ["Let's Dance to Joy Division", 'Kill the Director', 'Moving to New York', 'Turn', 'Tokyo - Vampires & Wolves', 'Cheetah Tongue', 'Lemon to a Knife Fight', 'Greek Tragedy', 'Pink Lemonade', 'Lethal Combination']
    tracks8 = ['2 / 14', 'Less Than I Do', 'See Through', 'Daphne Blue', 'My Thoughts On You', 'The Black and White', 'Know Me', 'Berenstein', 'Fool of Myself', 'Hush Hush']
    tracks9 = ['dancing around', 'back again', 'hold on', 'yellow (feat. MisterWives)', 'slow motion', 'warm blood', 'where do you go', 'heart', 'rely', 'slow motion']
    tracks9 = ['Royals', 'Team', 'Ribs', 'Green Light', 'Liability', 'Tennis Court', 'Supercut', 'Perfect Places', 'Homemade Dynamite - REMIX', 'The Love Club']

def create_recommendations_table(cur, conn):
    artists = ["The 1975", "The Japanese House", "Bleachers", "Lauv", 
    "Two Door Cinema Club", "Conan Gray", "The Wombats", "The Band CAMINO", 
    "Flor", "Lorde"]