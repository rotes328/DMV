import urllib.request
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime

class Scraper:

    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        soup = BeautifulSoup(html, 'html.parser')
        tabledmv = soup.select('font[color="red"]')[1:]
        for tag in tabledmv:
            texttag = tag.get_text()
            texttagnew = texttag.replace("    ", " ")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            if texttagnew in locations:
                loc = locations.index(texttagnew)
                locations[loc] = current_time
        print(locations)
        with open("outputfile.csv", "a") as f:
            f.write(json.dumps(locations))
            f.write('\n')


locations = ["Bakers Basin", "Oakland", "Bayonne", "Paterson", "Camden", "Rahway", "Cardiff", "Randolph", "Delanco",
                 "Rio Grande", "Eatontown", "S. Plainfield", "Flemington", "Toms River", "Freehold", "Vineland", "Lodi",
                 "Wayne", "Newark", "W. Deptford", "N. Bergen"]

with open("outputfile.csv", "a") as f:
    f.write(json.dumps(locations))
    f.write('\n')

for i in range (210):
    website = "https://www.state.nj.us/mvc/locations/agency.htm"
    Scraper(website).scrape()
    time.sleep(60)
