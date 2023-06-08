"""OVAJ KOD JE JOŠ U FAZI TESTIRANJA!
   RADI SE NA SPAJANJU KODA SA MYSQL BAZOM I IZMJENI LINKOVA DA POVLAĆE I DRUGE ŽANROVE (Trenutno samo 'Pop')."""
from bs4 import BeautifulSoup
from requests import get as get_website
import mysql.connector
from time import sleep


def get_site(year):
	response = get_website(f'https://playback.fm/charts/top-100-songs/{year}')
	soup = BeautifulSoup(response.text, 'html.parser')

	song_name = soup.find_all(class_='song')
	artist_name = soup.find_all(class_='artist')

	song_list = [song.text.strip() for idx, song in enumerate(song_name) if idx % 2 == 0]
	artist_list = [artist.text.strip() for artist in artist_name]

	return song_list, artist_list

def insert_into_database():
	data = ('test1', 'test2', '1234', 1234, 'test3', 'test.link')
	query = "INSERT INTO songs (artist, song, year, `rank`, genre, yt_link) VALUES (%s, %s, %s, %s, %s, %s);"

	mydb = mysql.connector.connect(
		host='localhost',
		user='root',
		password='0000',
		database='test_db')

	cursor = mydb.cursor()
	# cursor.execute(query, data)
	cursor.execute('SELECT * FROM songs;')
	result = cursor.fetchall()
	mydb.commit()

	cursor.close()
	mydb.close()


''' "format_link" funkcija služi za formatiranje linka na kojem se nalaze Youtube linkovi
	od pjesama, no pošto je dohvaćanje Youtube linkova trenutno teško izvedivo preko BeautifulSoup/Selenium
	biblioteka, u bazu se spremaju samo formatirani linkovi i funkcija stoji tu za buduće potrebe.'''
# ***************************************************************************************************
def format_link(year, artist, song):
	url = f'https://playback.fm/charts/top-100-songs/video/{year}/'
	artist, song = artist.split(' '), song.split(' ')
	for word in artist:
		cleaned_artist = word.strip(" ,&'-!?()").replace("'", "").replace("-", "").replace(".", "")
		if cleaned_artist != "": url += cleaned_artist + '-'
	for word in song:
		cleaned_song = word.strip(" ,&'-!?()").replace("'", "").replace("-", "").replace(".", "")
		if cleaned_song != "": url += cleaned_song + '-'
	return url[0:-1]
# ***************************************************************************************************

master_list = []
for n in range(1900, 1920):  # Promjeni na '2021 + 1' kada kod bude spreman za bazu'
	songs, artists = get_site(n)
	for i in range(1, len(songs[:3]) + 1):  # Namjerno limitirano na 2 prikaza (songs[:2]) radi jednostavnijeg pregleda
		formatted_link = format_link(n, artists[i-1], songs[i-1])
		master_list.append((artists[i-1], songs[i-1], n, i, 'Pop', formatted_link))
	master_list.append('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
	sleep(0.1)

print(len(master_list))
for x in master_list:
	print(x)

