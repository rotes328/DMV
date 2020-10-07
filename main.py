import urllib.request
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime
from datetime import date

class Scraper:

    def __init__(self, site):
        self.site = site


    def scrape(self, output_file, locations_list = []):
        self.outputfile = output_file
        self.locations = locations_list
        r = urllib.request.urlopen(self.site)
        html = r.read()
        soup = BeautifulSoup(html, 'html.parser')
        tabledmv = soup.select('font[color="red"]')[1:]
        for tag in tabledmv:
            texttag = tag.get_text()
            texttagnew = texttag.replace("    ", " ")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            if texttagnew in self.locations:
                loc = self.locations.index(texttagnew)
                self.locations[loc] = current_time
        print(self.locations)
        with open(self.outputfile, "a") as f:
            f.write(json.dumps(self.locations))
            f.write('\n')


class ProcessData:

    def __init__(self, site):
        self.site = site


    def process(self, interval, max_interval, output_file, locations_list = []):
        self.interval = interval
        self.max_interval = max_interval
        self.output_file = output_file
        self.locations_list = locations_list
        for i in range (max_interval):
            Scraper(self.site).scrape(self.output_file, self.locations_list)
            time.sleep(interval)


loclist = ["Bakers Basin", "Oakland", "Bayonne", "Paterson", "Camden", "Rahway", "Cardiff", "Randolph", "Delanco", "Rio Grande", "Eatontown", "Salem", "Edison", "S. Plainfield", "Flemington", "Toms River", "Freehold", "Vineland", "Lodi",  "Wayne", "Newark", "W. Deptford", "N. Bergen"]
today = date.today()
d1 = today.strftime("%b-%d-%Y")
output = "outputfile" + d1 + ".csv"
website = "https://www.state.nj.us/mvc/locations/agency.htm"

print("DMV Scraper Version 2 by Mike Rotella 10-07-2020")
print(loclist)

with open(output, "a") as f:
    f.write(json.dumps(loclist))
    f.write('\n')

ProcessData(website).process(1, 3, output, loclist)
