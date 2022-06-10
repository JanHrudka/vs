#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Pomocné knihovny
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', default = 'mzdy.csv', type = str, help = 'Input file')

def get_data_from_files(args):
    """ Načtení dat """
    plochy = {}
    with open('staty_plochy.log', 'r') as file_to_read:
        lines = file_to_read.readlines()
    for line in lines:
        plochy[line.strip().split(':')[0]] = float(line.strip().split(':')[1].strip())
    # print(plochy)

    lidi = {}
    with open('staty_lidi.log', 'r') as file_to_read:
        lines = file_to_read.readlines()
    for line in lines:
        lidi[line.strip().split(':')[0]] = int(line.strip().split(':')[1].strip())
    # print(lidi)

    return plochy, lidi

def marge(plochy, obyvatele):
    """ Spojení slovníků a případné dopočtení hustoty """
    states = {}
    for state in plochy.keys():
        state_info = {}
        state_info['plocha'] = plochy[state]
        if state in obyvatele.keys():
            state_info['obyvatele'] = obyvatele[state]
            state_info['hustota'] = obyvatele[state] / plochy[state]
        else:
            state_info['obyvatele'] = '?'
            state_info['hustota'] = -1
        states[state] = state_info
    for state in obyvatele.keys():
        if state not in plochy.keys():
            state_info = {}
            state_info['obyvatele'] = obyvatele[state]
            state_info['plocha'] = '?'
            state_info['hustota'] = -1
            states[state] = state_info
    return states

def sort_it(states):
    """ Pomocná funkce k uspořádání """
    sorted_data = {}
    for_sort = {}
    for key in states:
        for_sort[key] = states[key]['hustota']
    for x in sorted(for_sort, key=for_sort.get, reverse=True):
        # print(x, states[x])
        if states[x]['hustota'] == -1:
            states[x]['hustota'] = '?'
        sorted_data[x] = states[x]
    return sorted_data

def write_to_file(data):
    """ Zapsání do souboru """
    with open('stay_lidi_plocha_hustota.log', 'w') as file_to_write:
        for point in data.keys():
            # print(point, end='\t')
            file_to_write.write(point + ': ' + str(data[point]['obyvatele']) + ', ' + str(data[point]['plocha']) + ', ' + str(data[point]['hustota']) + '\n')
            # print(data[point]['obyvatele'], end='\t')
            # print(data[point]['plocha'], end='\t')
            # print(data[point]['hustota'], end='\t')
            # print()

def main(args):
    """ Hlavní funkce """
    plochy, obyvatele = get_data_from_files(args)
    states = marge(plochy, obyvatele)
    states = sort_it(states)
    write_to_file(states)

if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    main(args)
