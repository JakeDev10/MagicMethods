import csv

class Astronaut:
    def __init__(self, name, flightHr, status):
        self.name = name
        self.flightHr = flightHr
        self.status = status

    def __gt__(self, other):
        return self.flightHr > other.flightHr

    def __ge__(self, other):
        return self.flightHr >= other.flightHr

    def __eq__(self, other):
        return self.flightHr == other.flightHr

    def __str__(self):
        return f"{self.name}, {self.status}"

f = open("astronauts.csv")
astroDictionary = csv.DictReader(f)
dictList = list(astroDictionary)
f.close()

astroList = []

#Populates list with Astronaut objects
for x in range(0,len(dictList)):
    astroList.append(Astronaut(dictList[x]["Name"], dictList[x]["Space Flight (hr)"], dictList[x]["Status"]))

