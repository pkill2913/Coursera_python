#!/usr/bin/python3

import re
import sys
import csv

lineasfile = sys.argv[1]

def openfile_errors(lineasfile):
    with open(lineasfile) as f:
        conteo = {}
        i = 0
        for line in f:
            pattern = "([A-Z]+) ([a-zA-Z \.\']+) " 
            response = re.search(pattern,line)
            if response.group(1) == "ERROR":
                var_value = conteo.get(response.group(2))
                if var_value is None:
                    var_value = 0
                conteo[response.group(2)] = var_value + 1
        conteo_values = sorted(conteo.values(),reverse=True)
        conteo_sorted = {}
        for i in conteo_values:
            for k in conteo.keys():
                if conteo[k] == i:
                    conteo_sorted[k] = conteo[k]
        return conteo_sorted
def list_csv(conteo_sorted):
    list_errors = []
    for error, count in conteo_sorted.items():
        dict_new = {}
        dict_new["Error"] = error
        dict_new["Count"] = count
        list_errors.append(dict_new)
    return list_errors

def create_csv(list_errors):
    names_field = ['Error', 'Count']
    with open('error_message.csv', 'w') as error_message:
        writer = csv.DictWriter(error_message, fieldnames=names_field)
        writer.writeheader()
        writer.writerows(list_errors)

create_csv(list_csv(openfile_errors(lineasfile)))    
