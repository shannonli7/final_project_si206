import json
import requests

artist_song_info = [{'The 1975': ['Somebody Else', "Its Not Living If It's Not With You", 'Me and You Together Song', 'Love It If We Made It', 'The Birthday Party', 'Be My Mistake', 'TOOTIMETOOTIMETOOTIME', 'Sincerity Is Scary', 'Narcissist feat. The 1975', 'I Always Wanna Die Sometimes']}, 
{'The Japanese House': ['Saw You In A Dream', 'Chewing Cotton Wool', 'Something Has to Change', "Maybe You're the Reason", 'Lilo', 'You Seemed so Happy', 'i saw you in a dream', 'Cool Blue', 'Landslide', 'Still']}, 
{'Bleachers': ['Rollercoaster', 'I Wanna Get Better', "Don't Take The Money", 'Goodmorning', 'Wake Me', "Let's Get Married", 'Like a River Runs', 'Wild Heart', 'I Miss Those Days', 'Entropy']}, 
{'Lauv': ['I Like Me Better', 'Who feat. BTS', "i'm so tired", "fuck i'm lonely with Anne-Marie", 'Modern Loneliness', 'Mean It', 'Invisible Things', 'Make It Right feat. Lauv', 'Tattoos Together', 'Feelings']}, 
{'Two Door Cinema Club': ['What You Know', 'Undercover Martyn', 'Something Good Can Work', 'Sun', 'Changing of the Seasons', 'I Can Talk', 'Are We Ready? Wreck', 'Sleep Alone', 'Talk', 'Next Year']}, 
{'Conan Gray': ['Maniac', 'Crush Culture', 'Generation Why', 'The Story', 'Lookalike', 'Wish You Were Sober', 'Heather', 'Idle Town', 'The King', 'Comfort Crowd']}, 
{'The Wombats': ["Lets Dance to Joy Division", 'Kill the Director', 'Moving to New York', 'Turn', 'Tokyo Vampires and Wolves', 'Cheetah Tongue', 'Lemon to a Knife Fight', 'Greek Tragedy', 'Pink Lemonade', 'Lethal Combination']}, 
{'The Band CAMINO': ['2 14', 'Less Than I Do', 'See Through', 'Daphne Blue', 'My Thoughts On You', 'The Black and White', 'Know Me', 'Berenstein', 'Fool of Myself', 'Hush Hush']}, 
{'flor': ['dancing around', 'back again', 'hold on', 'yellow feat. MisterWives', 'slow motion', 'warm blood', 'where do you go', 'heart', 'rely', 'slow motion']}, 
{'Lorde': ['Royals', 'Team', 'Ribs', 'Green Light', 'Liability', 'Tennis Court', 'Supercut', 'Perfect Places', 'Homemade Dynamite', 'The Love Club']}]


def create_baseurl_itunes(artist_info):
    baseurl = "https://itunes.apple.com/search?"
    list_urls = []
    for dic in artist_info:
        for element in dic:
            if " " in element:
                count = element.count(" ")
                band_name = element.replace(" ", "+", count)
            else:
                band_name = element
            for song in dic[element]:
                if " " in song:
                    count = song.count(" ")
                    song_title = song.replace(" ", "+", count)
                else:
                    song_title = song
                params = "term=" + str(band_name) + "&term=" + str(song_title) +"&media=music"
                url = baseurl + params
                list_urls.append((element, url))
    return list_urls

def api_request(url_list):
    song_responses = []
    for url in url_list:
        response = requests.get(url[1])
        data = response.text
        data_fix = json.loads(data)
        for result in data_fix["results"]:
            if url[0] == result["artistName"]:
                song_responses.append(result)

    return song_responses

def get_track_price(response_list):
    track_info = []
    for response in response_list:
        if "trackPrice" in response:
            track_price = response["trackPrice"]
        else:
            track_price = 1
        track_name = response["trackName"]
        track_artist = response["artistName"]
        track_info.append((track_artist, track_name, track_price))
            
    return track_info
    
    
trial = create_baseurl_itunes(artist_song_info)
trial2 = api_request(trial)
trial3 = get_track_price(trial2)

print(trial3)

