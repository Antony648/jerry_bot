import requests,sys,webbrowser,bs4
#from ytmusicapi import YTMusic
from youtubesearchpython import VideosSearch

'''def request_for_web(prompt:str):
    res=requests.get("https://google.com/search?q="+prompt)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,"html.parser")
    linkElements=soup.select('.r a')'''

def search_song(song_name:str):
    try:
        vedios_search=VideosSearch(song_name,limit=1)
        results=vedios_search.result()
        vedio_url=results['result'][0]['link']
        webbrowser.open(vedio_url)
    except:
        print("error")
#search_song("vivaldi winter")