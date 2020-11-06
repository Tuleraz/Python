import json
# Do task_1

with open('data_schema.json') as json_file: 
    json_schema = json.load(json_file) # загружаем схему в объект (dictionary)
with open('input_text.txt') as input_text:

def rootList(root, level):
    for key in root:
        if( not (type(root[key]) == type({}))): print("    " * level, key, "->", root[key])
        else: print("    " * level, key)
        if type(root[key]) is dict:
            level+=1
            rootList(root[key], level)

rootList(json_schema, 0)

