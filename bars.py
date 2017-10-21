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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("data", help="path to json file")
    parser.add_argument("get_function", help="what will need do", type=str)
    parser.add_argument("-lon", "--longitude", help="longitude",
                        required=False, type=float)
    parser.add_argument("-lat", "--latitude", help="latitude", required=False,
                        type=float)
    args = parser.parse_args()
    bars_info = load_json(args.data)['features']
    if args.get_function == "biggest_bar":
        print("Самый большой бар\nНазвание: {name}\nАдрес: {address}\n"
              .format(name=get_biggest_bar(bars_info)
                      ['properties']['Attributes']['Name'],
                      address=get_biggest_bar(bars_info)['properties']
                      ['Attributes']['Address']))
    if args.get_function == "smallest_bar":
        print("Самый маленький бар\nНазвание: {name}\nАдрес: {address}\n"
              .format(name=get_smallest_bar(bars_info)
                      ['properties']['Attributes']['Name'],
                      address=get_smallest_bar(bars_info)
                      ['properties']['Attributes']['Address']))
    if args.get_function == "closest_bar":
        try:
            print("Самый близкий бар\nНазвание: {name}\nАдрес: {address}\n"
                  .format(name=get_closest_bar(bars_info, args.longitude,
                                               args.latitude)['properties']
                                                             ['Attributes']
                                                             ['Name'],
                          address=get_closest_bar(bars_info, args.longitude,
                                                  args.latitude)['properties']
                                                                ['Attributes']
                                                                ['Address']))
        except TypeError:
            print("Введите широту и долготу после вызова функции:\n"
                  "-lon <longitude> -lat <latitude>")
