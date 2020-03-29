import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

genie_chart = soup.select('table.list-wrap > tbody > tr > td.info')

i = 0
for music in genie_chart:
    title = music.select('a.title.ellipsis')
    artist = music.select('a.artist.ellipsis')
    i += 1
    title = title[0].text.strip()
    artist = artist[0].text
    print(i, title, '-', artist)