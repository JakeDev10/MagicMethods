import csv
import random

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

#Lists mutable properties
print(vars(astroList[0]))

#Does a random comparison of space flight hours
rand1 = random.choice(astroList)
rand2 = random.choice(astroList)
print(f"Does {rand1} have more flight hours than {rand2}? ", rand1 > rand2)

#Prints all astronatus
for x in range(0, len(astroList)):
    print(astroList[x])