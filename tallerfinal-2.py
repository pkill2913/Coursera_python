#!/usr/bin/python3

import re
import sys
import csv

lineasfile = sys.argv[1]

#
#list_value = [0,0]

def openfile_users(lineasfile):
    dict_users = {}
    with open(lineasfile) as f:
        conteo = {}
        i = 0
        for line in f:
            pattern = "([A-Z]+).*\(([\w\.]+)\)$" 
            response = re.search(pattern,line)
            if response.group(1) == "INFO":
                list_value = dict_users.get(response.group(2))
                if list_value is None:
                    list_value = [0,0]
                list_value[0] += 1
                dict_users[response.group(2)] = list_value
            elif response.group(1) == "ERROR":
                list_value = dict_users.get(response.group(2))
                if list_value is None:
                    list_value = [0,0]
                list_value[1] += 1
                dict_users[response.group(2)] = list_value
        users_items = dict_users.items()
        users_sorted = sorted(users_items)
        return users_sorted

def users_dic(users_sorted):
    userdir = {}
    users_list = []
    i = 0
    for value in users_sorted:
        userdir = {}
        userdir['Username'] = users_sorted[i][0]
        userdir['INFO'] = users_sorted[i][1][0]
        userdir['ERROR'] = users_sorted[i][1][1]
        users_list.append(userdir)
        i += 1
    return users_list

def create_csv_users(users_list):
    names_field = ['Username', 'INFO', 'ERROR']
    with open('user_statistics.csv', 'w') as user_statistics:
        writer = csv.DictWriter(user_statistics, fieldnames=names_field)
        writer.writeheader()
        writer.writerows(users_list)

create_csv_users(users_dic(openfile_users(lineasfile)))    


