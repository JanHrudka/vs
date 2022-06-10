#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Pomocné knihovny
import argparse
from csv import reader

parser = argparse.ArgumentParser()
parser.add_argument('--input', default = 'mzdy.csv', type = str, help = 'Input file')

def get_data_from_file(args):
    """ Načtení dat """
    data = {}
    with open(args.input, newline='') as csv_file:
        spam_reader = reader(csv_file, delimiter=';', quotechar="'")
        for i, row in enumerate(spam_reader):
            if i != 0:
                # print(row[1], row[-1])
                data[row[1]] = row[-1]
    return data

def main(args):
    """ Hlavní funkce """
    data = get_data_from_file(args)
    for x in sorted(data, key=data.get, reverse=True):
        print(x, data[x])

if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    main(args)
