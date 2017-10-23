import json
import argparse
from math import sqrt


def load_json(path_to_file):
    with open(path_to_file, "r", encoding='utf-8') as file:
        return json.load(file)


def get_biggest_bar(json_data):
    return max(json_data,
               key=lambda bar: bar['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(json_data):
    return min(json_data,
               key=lambda bar: bar['properties']['Attributes']['SeatsCount'])


def get_closest_bar(json_data, longitude, latitude):
    return min(json_data, key=lambda bar: sqrt(
        (bar['geometry']['coordinates'][0] - latitude) ** 2 +
        (bar['geometry']['coordinates'][1] - longitude) ** 2))


def add_parser():
    new_parser = argparse.ArgumentParser()
    new_parser.add_argument("data", help="path to json file")
    new_parser.add_argument("get_function", help="what will need do", type=str)
    new_parser.add_argument("-lon", "--longitude", help="longitude",
                            required=False, type=float)
    new_parser.add_argument("-lat", "--latitude", help="latitude",
                            required=False, type=float)
    return new_parser


if __name__ == '__main__':
    parser = add_parser()
    args = parser.parse_args()
    bars_info = load_json(args.data)['features']
    if args.get_function == "biggest_bar":
        print("Самый большой бар\nНазвание: {name}\nАдрес: {address}\n"
              .format(name=get_biggest_bar(bars_info)
                      ['properties']['Attributes']['Name'],
                      address=get_biggest_bar(bars_info)['properties']
                      ['Attributes']['Address']))
    elif args.get_function == "smallest_bar":
        print("Самый маленький бар\nНазвание: {name}\nАдрес: {address}\n"
              .format(name=get_smallest_bar(bars_info)
                      ['properties']['Attributes']['Name'],
                      address=get_smallest_bar(bars_info)
                      ['properties']['Attributes']['Address']))
    elif args.get_function == "closest_bar" and args.latitude is not None\
            and args.longitude is not None:
        print("Самый близкий бар\nНазвание: {name}\nАдрес: {address}\n"
              .format(name=get_closest_bar(bars_info, args.longitude,
                                           args.latitude)['properties']
                                                         ['Attributes']
                                                         ['Name'],
                      address=get_closest_bar(bars_info, args.longitude,
                                              args.latitude)['properties']
                                                            ['Attributes']
                                                            ['Address']))
    elif args.get_function == "closest_bar" and args.latitude is None\
            and args.longitude is None:
        parser.error("Введите широту и долготу\n")
