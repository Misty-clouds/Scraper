import httpx
from selectolax.parser import HTMLParser


url= "https://www.eventbrite.com/d/nigeria--lagos/business--events/?page=1"
headers= {'Authorization':'Bearer NJ7LKGNHP64J6C7NJD6W'}


response= httpx.get(url,headers=headers)
html= HTMLParser(response.text)

events = html.css('ul.SearchResultPanelContentEventCardList-module__eventList___2wk-D li')

for event in events:
    print(event.css_first("h3").text())
    #time
    time= event.css_first("Tomorrow • 10:00 AM CDT")
    print(time.text())
