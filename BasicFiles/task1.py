import os
from pprint import pprint
from posixpath import dirname, split
from collections import OrderedDict


def load_file():
    dir = os.getcwd()
    with open(f'{dir}/BasicFiles/recipes.txt', 'r') as file:
        data = {}
        for line in file:
            meal = line.strip()
            counter = int(file.readline())
            _lingrid_list = []
            for item in range(counter):
                ingridient_name, quantity, uom = file.readline().strip("\n").split("|")
                _lingrid_list.append(
                    {'ingridient name': ingridient_name, 'quantity': quantity, 'unit of measurment': uom}
                )
            data[meal] = _lingrid_list
            file.readline()
    return data


def get_shop_list_by_dishes(dishes, person_count):
    data = {}
    ingridients = load_file()
    for dish in dishes:
        if dish in ingridients:
            for ingrid in ingridients[dish]:
                if data.values() in ingrid:
                    data[ingrid['ingridient name']] += {'measure': ingrid['unit of measurment'], 
                    'quantity': int(ingrid['quantity']) * person_count}
                elif ingrid['ingridient name'] in data:
                    data[ingrid['ingridient name']]['quantity'] = \
                        int(data[ingrid['ingridient name']]['quantity']) + (int(ingrid['quantity']) * person_count)
                else:
                    data[ingrid['ingridient name']] = {'measure': ingrid['unit of measurment'], 
                    'quantity': int(ingrid['quantity']) * person_count}
    return data


def parser_txt(files):
    dir = os.getcwd()
    dir = dir + '/BasicFiles/'
    data = []
    for file in files:
        file_data = {}
        lines = []
        with open(f'{dir}{file}.txt', 'r', encoding='utf-8') as data_file:
            counter = 0
            for line in data_file:
                lines.append(line.strip())
                counter += 1
            data.append({'File name': f'{file}.txt', f'counter{file}': counter, 'data files': lines})
    #test = OrderedDict(data)
    return data


pprint(load_file())
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))
pprint(parser_txt(["1", '2', "3"]))