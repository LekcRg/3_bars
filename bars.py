import json
import sys
from math import sqrt


def load_data(path_to_file):
    with open(path_to_file, "r") as file:
        return json.load(file)


def get_biggest_bar(data):
    seats_count = []

    for bars in data['features']:
        if bars['properties']['Attributes']['SeatsCount'] > 0:
            seats_count.append(bars['properties']['Attributes']['SeatsCount'])

    biggest_bar = max(seats_count)

    for bars in data['features']:
        if bars['properties']['Attributes']['SeatsCount'] == biggest_bar:
            print("Name of bar: " + bars['properties']['Attributes']['Name'] + "\n" +
                  "Address: " + bars['properties']['Attributes']['Address'])


def get_smallest_bar(data):
    seats_count = []

    for bars in data['features']:
        if bars['properties']['Attributes']['SeatsCount'] > 0:
            seats_count.append(bars['properties']['Attributes']['SeatsCount'])

    smallest_bar = min(seats_count)

    for bars in data['features']:
        if bars['properties']['Attributes']['SeatsCount'] == smallest_bar:
            print("Name of bar: " + bars['properties']['Attributes']['Name'] + "\n" +
                  "Address: " + bars['properties']['Attributes']['Address'])


def get_closest_bar(data, longitude, latitude):
    distance = []
    bar_number = 0

    for bar in data['features']:
        distance.append(sqrt((bar['geometry']['coordinates'][0] - latitude) ** 2 +
                             (bar['geometry']['coordinates'][1] - longitude) ** 2))

    for bar_distance in distance:
        if bar_distance == min(distance) and bar_number != 150:
            print("Name of bar: " + data['features'][bar_number]['properties']['Attributes']['Name'] + "\n" +
                  "Address: " + data['features'][bar_number]['properties']['Attributes']['Address'])
        bar_number += 1


bars_info = load_data("bars_info.json")
if __name__ == '__main__':
    if sys.argv[1] == "get_biggest_bar":
        get_biggest_bar(bars_info)

    if sys.argv[1] == "get_smallest_bar":
        get_smallest_bar(bars_info)

    if sys.argv[1] == "get_closest_bar":
        get_closest_bar(bars_info, float(sys.argv[2]), float(sys.argv[3]))
