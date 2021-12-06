from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

DOOR_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome('chromedriver.exe')
browser.get(DOOR_URL)
time.sleep(10)
def scrape():
  classes = ["V Mag. (mV)"	,"Proper name","Bayer designation","Distance (ly)","Spectral class","Mass (M☉)","Radius (R☉)"	,"Luminosity (L☉)"]
  star_data = []
  for i in range(0,428):
     soup = BeautifulSoup(browser.page_source,"html.parser")
     for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
     star_data.append(temp_list)
  with open('stars.csv','w') as f:
     writer = csv.writer(f)
     writer.writerow(classes)
     writer.writerows(star_data)
scrape()
