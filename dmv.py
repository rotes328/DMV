import urllib.request
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime
from datetime import date


def wait(howlong, locations_list = []):
    if howlong < 1 or howlong > 60:
        print("Error")
        pass
    x = 0
    y = 0
    list = ["[|]", "[/]", "[-]", "[\]"]
    while y < ((howlong * 2) + 1):
        time.sleep(0.5)
        print("\r{} {}".format(list[x], locations_list), end="")
        x = (x + 1) % 4
        y += 1


def get_seconds():
    while True:
        a = input("Run how often in seconds (1-60, q to Quit)? ")
        if a.lower() == "q" or a.lower() == "quit":
            exit()
        try:
            int_a = int(a)
            if 1 <= int_a <= 60:   # return if valid, this leaves the while loop
                return int_a
        except ValueError:         # catch specific errors
            print("Interval must be an integer between 1 and 60.")


def get_attempts():
    while True:
        a = input("Run for how many attempts (1-960)? ")
        if a.lower() == "q" or a.lower() == "quit":
            exit()
        try:
            int_a = int(a)
            if 1 <= int_a <= 960:   # return if valid, this leaves the while loop
                return int_a
        except ValueError:         # catch specific errors
            print("Interval must be an integer between 1 and 960.")


def get_log():
    while True:
        a = input("Log to CSV? (y/n)? ")
        if a.lower() == "q" or a.lower() == "quit":
            exit()
        try:
            if a.lower() == "y" or a.lower() == "yes":
                return True
            elif a.lower() == "n" or a.lower() == "no":
                return False
        except:
            print("Please answer yes or no (q to quit).")


def writetofile(out, loclist):
    try:
        with open(out, "a") as f:
            f.write(json.dumps(loclist))
            f.write('\n')
    except:
        print("Error logging to file.")
        pass


class Scraper:

    def __init__(self, site):
        self.site = site


    def scrape(self, output_file, log, locations_list = []):
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
        if log == True:
            try:
                with open(self.outputfile, "a") as f:
                    f.write(json.dumps(self.locations))
                    f.write('\n')
            except:
                print("Write to file failed.")
                pass


class ProcessData:

    def __init__(self, site):
        self.site = site


    def process(self, interval, attempts, output_file, log, locations_list = []):
        self.interval = interval
        self.attempts = attempts
        self.output_file = output_file
        self.locations_list = locations_list
        self.log = log
        for i in range (attempts):
            Scraper(self.site).scrape(self.output_file, self.log, self.locations_list)
            if i < (attempts-1):
                wait(interval, self.locations_list)


#Variables:
loclist = ["Bakers Basin", "Oakland", "Bayonne", "Paterson", "Camden", "Rahway", "Cardiff", "Randolph", "Delanco", \
    "Rio Grande", "Eatontown", "Salem", "Edison", "S. Plainfield", "Flemington", "Toms River", "Freehold", "Vineland", \
    "Lodi",  "Wayne", "Newark", "W. Deptford", "N. Bergen"]
today = date.today()
timenow = datetime.now()
d1 = today.strftime("%b-%d-%Y")
d2 = timenow.strftime("%H%M")
output = "outputfile" + d1 + "-" + d2 + ".csv"
website = "https://www.state.nj.us/mvc/locations/agency.htm"


def main():

    print("\nDMV Scraper Version 3 by Mike Rotella 10-10-2020\n")
    a = get_seconds()
    b = get_attempts()
    log = get_log()
    print("Proccessing every {} seconds for {} attempts.\n".format(a, b))

    if log == True:
        writetofile(output, loclist)

    print("   ",loclist)
    print("-"*280)
    dmv = ProcessData(website)
    dmv.process(a, b, output, log, loclist)


if __name__ == "__main__":
    main()
