import tkinter as tk
import requests
from bs4 import BeautifulSoup

# Function to fetch lyrics using Genius API
def fetch_lyrics(song_name):
    # Replace with your Genius API key
    genius_token = 'YOUR_GENIUS_API_KEY_HERE'
    headers = {'Authorization': 'Bearer ' + genius_token}

    # Search for the song
    search_url = 'https://api.genius.com/search'
    params = {'q': song_name}
    response = requests.get(search_url, params=params, headers=headers)
    response_json = response.json()

    # Get the URL of the first search result (assuming it's the correct song)
    song_url = response_json['response']['hits'][0]['result']['url']

    # Scrape lyrics from the song's Genius page
    page = requests.get(song_url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find('div', class_='lyrics').get_text()

    return lyrics.strip()

# Function to handle button click
def get_lyrics():
    song_name = entry.get()
    lyrics = fetch_lyrics(song_name)
    text.delete('1.0', tk.END)  # Clear previous lyrics
    text.insert(tk.END, lyrics)

# GUI setup
root = tk.Tk()
root.title("Song Lyrics Extractor")

# Entry for user to input song name
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Button to fetch lyrics
button = tk.Button(root, text="Get Lyrics", command=get_lyrics)
button.pack(pady=5)

# Text widget to display lyrics
text = tk.Text(root, wrap=tk.WORD, width=50, height=20)
text.pack(padx=10, pady=10)

root.mainloop()
