import urllib.request  as urllib2
from bs4 import BeautifulSoup
import csv
import numpy as np
import pandas as pd
import re

quote_page = 'https://www.yamu.lk/events'

page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page,'html.parser')


print (soup.title.string)

soup.a

class event:
    def __init__(self,Day,Month,Name,Location,Time):
        self.Day = Day
        self.Month = Month
        self.Name= Name
        self.Location= Location
        self.Time = Time

    def as_dict(self):
        return {'Day': self.Day, 'Month': self.Month, 'Name': self.Name,'Location': self.Location,'Time':self.Time}

eventlist = []




#all_links =soup.find_all("a")
#for link in all_links:
	#print (link.get("href"))
	


yamu = soup.find_all(id="tab-this-week")


eventday= yamu[0].find_all(class_="list-group-item searchItem")


# print(eventday)

for i in range(len(eventday)):

    monthday=eventday[i].find_all(class_="text-center question-label")
    month = eventday[i].find_all(class_="sub-q question-unanswered")
    nameofevent  = eventday[i].find_all(class_="col-xs-10")
    # location     = eventday[i].find_all(class_="glyphicon glyphicon-map-marker")
    # time =        eventday[i].find_all(class_="glyphicon glyphicon-time")
    timelocation = eventday[i].find_all(class_= "text-muted row")
    # print("Monthday",monthday)
    # print("nameofevent",nameofevent)
   
    

    


    if len(monthday)<1:
        eventdayNoPrint= eventdayNolatest
        monthprint = monthlatest
        nameofeventlastest = nameofevent[0].h3.get_text()
        timelocationprint= nameofevent[0].find_all('li')

        # nameofeventprint = nameofeventlastest
     
        # timelocationprint=timelocationprintlatest
        
    else:
        eventdayNolatest= monthday[0].get_text()
        eventdayNoPrint=monthday[0].get_text()
        monthlatest = month[0].get_text()
        monthprint=  month[0].get_text()
        nameofeventlastest = nameofevent[0].h3.get_text()
        # nameofeventprint= nameofevent[0].h3.find_all(class_="glyphicon glyphicon-map-marker")
        
        # timelocationprintlatest=  timelocation[0].get_text()
        timelocationprint= nameofevent[0].find_all('li')

        # locationprintlatest = location[0].get_text()
        # locationprint= location[0].get_text()
        # timeprintlatest = time[0].get_text()
        # timeprint = time[0].get_text()

    
    # print("Day of the month", eventdayNoPrint)
    # print("Month", monthprint)
    # print("Name of the event",nameofeventlastest)
    # print("location of the event",timelocationprint[0].get_text())
    # print("time of the event",timelocationprint[1].get_text())
    
    eventlist.append(event(eventdayNoPrint.strip(),monthprint.strip(),nameofeventlastest.strip(),timelocationprint[0].get_text().strip(),re.sub(r"\s+", "", timelocationprint[1].get_text(), flags=re.UNICODE)))





df = pd.DataFrame([x.as_dict() for x in eventlist])
# df2= pd.DataFrame([vars(e) for e in eventlist])  


print(df)
df.to_csv('eventstest.csv', encoding='utf-8', index=False)
# df.to_csv('eventstest.csv', sep='\t', encoding='utf-8')
# df.to_csv('eventstest.csv')

    # if len(more)<1:
    #     more=eventday[i-1].find_all("text-center question-label")

    # more2=eventday[i].find_all('li')
    # #data2= yamu[0].get_text()
    # datax= more.get_text()
    # data = event[i].get_text() 
    # data3=eventName[i].get_text()
    # #data4= location2[0].get_text()


    # print("Date:",datax)
    # print("details:",eventName[i].h3.get_text())

    # if (more[0]):
    # 	print("location:",more2[0].get_text())
    # else:
    # 	print("no starting date mentioned")
    # if len(more) == 2:
    # 	print("time:",more[1].get_text())
    # else:
    # 	print("no starting time mentoined")

