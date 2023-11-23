import datetime as date
import pywhatkit as pw
import wikipedia as wiki
import pyjokes
import spotipy
import webbrowser


username = 'USERNAME'
clientID = 'CLIENTID'
clientSecret = 'CLIENTSECRET'
redirect_uri = 'http://example.com'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()


class Abilities():
    def __init__(self, task):
        self.instruct = task
        self.ideas = {
            'greeting': {
                'hello': 'Hello! How can I help you?',
                'hi': 'Hi there!',
                'hey': 'Hey! What can I do for you?',
                "what's up": "Hey, what's up?",
            },
            'time': {
                'what time is it': f"The time is {date.datetime.now().strftime('%I:%M %p')}.",
                'what day is it': f"The day is {date.datetime.now().strftime('%A')}.",
                "what is today's date": f"Today's date is {date.datetime.now().strftime('%c')}.",
            },
            'end': {
                'goodbye':'Goodbye, sir',
                'terminate':"Til we meet again, sir",
                'see you later':'Another time, sir'
            },
            'play': {
                    'youtube': {
                        'play': 'Playing YouTube video...',
                    },
                    'spotify': {
                        'play': 'Playing YouTube video...',
                    },
            },
            'search': {
                'wiki': "Of course",
            },
            'funny':{
                'joke':'Hahaha'
            }
        }

    def work(self):
        instruct_lower = self.instruct.lower()

        for key, phrases in self.ideas.items():
            if 'play' in instruct_lower:
                if 'youtube' in instruct_lower:
                    search_query = instruct_lower.replace('claude', '').replace('claudia', '').replace('play', '').replace('on youtube', '').strip()
                    pw.playonyt(search_query)
                    response = f"Playing YouTube video: {search_query}"
                    return response
                elif 'spotify' in instruct_lower:
                    search_query = instruct_lower.replace('claude', '').replace('claudia', '').replace('play', '').replace('on spotify', '').strip()
                    results = spotifyObject.search(search_query, 1, 0, "track")
                    songs_dict = results['tracks']
                    song_items = songs_dict['items']
                    song = song_items[0]['external_urls']['spotify']
                    webbrowser.open(song)
            elif 'search' in instruct_lower and 'wiki' in instruct_lower:
                search_query = instruct_lower.replace('claude', '').replace('claudia', '').replace('search', '').replace('on wiki', '').strip()
                info = wiki.summary(search_query, 1)
                response = f"Here you go: {info}"
                return response
            elif 'joke' in instruct_lower:
                response = f"Sure, {pyjokes.get_joke()}"
                return response
            elif instruct_lower in phrases:
                response = phrases[instruct_lower]
                return response
            else:
                for phrase in phrases:
                    if phrase in instruct_lower:
                        response = phrases[phrase]
                        return response

        return "I'm sorry, i did not quite understand, can u repeat your command."


