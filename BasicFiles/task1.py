import os
import json

dir = os.path.abspath(os.curdir)
dir = os.getcwd()
print(dir)
recipes_list = []
tmp_list = []
with open(f'{dir}/BasicFiles/recipes.txt', 'r') as file:
    for line in file:
        line = line[:-1]
        #line = line.split("|")
        #line = line.split("\n")
        
        if line:
            tmp_list.append(line)
            count = 0
            value = []
            key = []
            for list in tmp_list:
                print(isinstance(list, str))
                if len(list) > 1 and not isinstance(list, int):
                    value.append(list.split('|'))
                elif isinstance(list, int):
                    count = list
                    print(count)
                elif len(list) == 1 and isinstance(list, str):
                    key.append(list)
                else:
                    pass
            
            #print(value)
            print(key)
            
#print(recipes_list)
#recipes_dict = {}
#for rec in recipes_list:
    #count = 0
    #print(len(rec))
    #print(recipes_dict)

