# Author: przewnic
# Write stations and lines to  csv file
# Script just to create example testing files

import csv
from random import randint

stations = []
number_of_stations = 100
for i in range(number_of_stations):
    x = i*100 % 1000
    y = int((i/10)//1)*100
    stations.append(("S"+str(100+i), randint(1, 3), x, y))
path = "tram_system_stations.csv"
with open(path, "w", newline="") as file:
    stations_writer = csv.DictWriter(
            file, ["station_name", "tram_wait", "x", "y"], delimiter=';'
        )
    stations_writer.writeheader()
    for station in stations:
        stations_writer.writerow(
            {
                "station_name": station[0],
                "tram_wait": station[1],
                "x": station[2],
                "y": station[3]
            }
        )


lines = []
lines.append((1, list(range(90, 99)), "CIRCLE"))
lines.append((2, list(range(0, 3))+list(range(12, 23)), "STRAIGHT"))
lines.append((3, list(range(23, 26))+list(range(2, 3))+list(range(26, 32)), "STRAIGHT"))
lines.append((4, list(range(32, 35))+list(range(3, 4))+list(range(35, 40)), "STRAIGHT"))
lines.append((5, list(range(40, 44))+list(range(4, 5))+list(range(44, 52)), "STRAIGHT"))
lines.append((6, list(range(52, 68)), "CIRCLE"))
lines.append((7, list(range(68, 75)), "STRAIGHT"))
lines.append((8, list(range(75, 86)), "CIRCLE"))
lines.append((9, list(range(86, 90)), "STRAIGHT"))
lines.append((10, list(range(1, 11)), "STRAIGHT"))


path = "tram_system_lines.csv"
with open(path, "w", newline="") as file:
    lines_writer = csv.DictWriter(
            file, ["line_number", "stations", "type"], delimiter=';'
        )
    lines_writer.writeheader()
    for line in lines:
        lines_writer.writerow(
            {
                "line_number": line[0],
                "stations": line[1],
                "type": line[2],
            }
        )
