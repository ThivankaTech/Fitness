# This code is written by S.P.D Thivanka Saranatha

import urllib.request  as urllib2
from bs4 import BeautifulSoup


# Page link
quote_page = 'https://www.yamu.lk/events'

# Fetch resourses from web
page = urllib2.urlopen(quote_page)

#Parse through fetch resourses using parse tree
soup = BeautifulSoup(page,'html.parser')

# Print the title
print (soup.title.string)

soup.a



#all_links =soup.find_all("a")
#for link in all_links:
	#print (link.get("href"))
	


yamu = soup.find_all(id="tab-this-week")



eventday= yamu[0].find_all(class_="text-center question-label")
event= yamu[0].find_all(class_="sub-q question-unanswered")
eventName = yamu[0].find_all(class_="col-xs-10")

location= yamu[0].find_all(class_="text-muted list-inline")
print(len(eventday))
for i in range(len(eventday)):
	more=location[i].find_all('li')
	#data2= yamu[0].get_text()
	datax= eventday[i].get_text()
	data = event[i].get_text() 
	data3=eventName[i].get_text()
	#data4= location2[0].get_text()
	
	
	print("Date:",datax)
	print("details:",eventName[i].h3.get_text())
	
	if (more[0]):
		print("location:",more[0].get_text())
	else:
		print("no starting date mentioned")
	if len(more) == 2:
		print("time:",more[1].get_text())
	else:
		print("no starting time mentoined")