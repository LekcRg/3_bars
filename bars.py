import json
import sys
from math import sqrt


def load_json(path_to_file):
    with open(path_to_file, "r", encoding='utf-8') as file:
        return json.load(file)


def get_biggest_bar(json_data):
    return max(json_data, key=lambda bar: bar['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(json_data):
    return min(json_data, key=lambda bar: bar['properties']['Attributes']['SeatsCount'])


def get_closest_bar(json_data, longitude, latitude):
    return min(json_data, key=lambda bar: sqrt((bar['geometry']['coordinates'][0] - latitude) ** 2 +
                                               (bar['geometry']['coordinates'][1] - longitude) ** 2))


if __name__ == '__main__':
    bars_info = load_json(sys.argv[1])['features']
    if sys.argv[2] == "biggest_bar":
        print("Самый большой бар\nНазвание: {name}\nАдрес: {address}\n"
              .format(name=get_biggest_bar(bars_info)['properties']['Attributes']['Name'],
                      address=get_biggest_bar(bars_info)['properties']['Attributes']['Address']))
    if sys.argv[2] == "smallest_bar":
        print("Самый маленький бар\nНазвание: {name}\nАдрес: {address}\n"
              .format(name=get_smallest_bar(bars_info)['properties']['Attributes']['Name'],
                      address=get_smallest_bar(bars_info)['properties']['Attributes']['Address']))
    if sys.argv[2] == "closest_bar":
        print("Самый близкий бар\nНазвание: {name}\nАдрес: {address}\n"
              .format(name=get_closest_bar(bars_info, float(sys.argv[3]),
                                           float(sys.argv[4]))['properties']['Attributes']['Name'],
                      address=get_closest_bar(bars_info, float(sys.argv[3]),
                                              float(sys.argv[4]))['properties']['Attributes']['Address']))
