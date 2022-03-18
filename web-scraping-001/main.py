import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/2000-08-12"
# question = input('what year would you like to travel to ? Type the date in this format YYY-MM-DD')
responses = requests.get(URL)
data_soup = responses.text

soup = BeautifulSoup(data_soup, "html.parser")
print(soup.prettify())
x = soup.find_all(name="h3", limit=100)
for y in x:
    a = y.getText().strip()
    print(a)


# all_songs = soup.find_all(name="h3", class_="title")
song_titles = soup.find(name="h3").getText().strip()
print(song_titles)
# [title.getText() for (soup.find_all("h3")) in ]

# print(song_titles.getText())
#
# # title = song.find(name="a").getText()
# # print("----------------------------")
# # print(title)
# best100songs = []
# all_songs_title = soup.find_all("h3")
# for title in all_songs_title:
#     best100songs.append(soup.getText())
# print(best100songs)
#
# # # print(songtitle)
# best100songs = []
# for title in song_titles:
#     titles = (title.getText())
#     pass
