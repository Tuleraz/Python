import json, glob

def rootList(root, level):
    for key in root:
        if( not (type(root[key]) is dict)): 
            print("    " * level, key, "->", root[key])
        else: 
            print("    " * level, key)
            level+=1
            rootList(root[key], level)

print(glob.glob("*.json"), "\nPlease, type file name from list:")
try:
   with open(str(input())) as json_file: 
        json_schema = json.load(json_file)
except IOError:
    print("Error: File does not appear to exist.")
else:
    rootList(json_schema, 0)

