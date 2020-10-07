import urllib.request
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime
from datetime import date
import sys

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


    def process(self, interval, attempts, output_file, locations_list = []):
        self.interval = interval
        self.attempts = attempts
        self.output_file = output_file
        self.locations_list = locations_list
        for i in range (attempts):
            Scraper(self.site).scrape(self.output_file, self.locations_list)
            if i < (attempts-1):
                time.sleep(interval)


loclist = ["Bakers Basin", "Oakland", "Bayonne", "Paterson", "Camden", "Rahway", "Cardiff", "Randolph", "Delanco", "Rio Grande", "Eatontown", "Salem", "Edison", "S. Plainfield", "Flemington", "Toms River", "Freehold", "Vineland", "Lodi",  "Wayne", "Newark", "W. Deptford", "N. Bergen"]
today = date.today()
timenow = datetime.now()
d1 = today.strftime("%b-%d-%Y")
d2 = timenow.strftime("%H%M")
output = "outputfile" + d1 + "-" + d2 + ".csv"
website = "https://www.state.nj.us/mvc/locations/agency.htm"

#Defaults:
interval_in_seconds = 1
attempts = 3

def intro(a, b):
    print("DMV Scraper Version 2 by Mike Rotella 10-07-2020")
    print("Proccessing every {} seconds for {} attempts.".format(a, b))
    return

try:
    if __name__ == "__main__":
        a = int(sys.argv[1])
        b = int(sys.argv[2])
except:
    a = interval_in_seconds
    b = attempts

with open(output, "a") as f:
    f.write(json.dumps(loclist))
    f.write('\n')

if len(sys.argv) == 3 and a > 0 and a < 61 and b > 0 and b < 481:
    intro(a, b)
    print(loclist)
    ProcessData(website).process(a, b, output, loclist)
else:
    a = interval_in_seconds
    b = attempts
    intro(a, b)
    print("\nUse arguments [inteval in seconds between 1 and 60] [attempts between 1 and 480] to change defaults.\n")
    print(loclist)
    ProcessData(website).process(a, b, output, loclist)
