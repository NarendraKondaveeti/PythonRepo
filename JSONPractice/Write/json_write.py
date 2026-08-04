import json                                            
# json = Python built-in module, JSON data ni Python dictionary/list ga convert chestundi

JSON_FILE = "users.json"                      
# JSON file path

def read_json():     # JSON read function
    with open(JSON_FILE) as file: 
        # open() = Python built-in function, with = automatic file close
        return json.load(file)                         
    # json.load() = JSON file ni dictionary ga convert chestundi

def write_json(data):   # JSON write function
    with open(JSON_FILE, "w") as file:                 
        # "w" = Write mode, existing file overwrite chestundi
        json.dump(data, file, indent=4)                
        # json.dump() = Dictionary ni JSON file lo write chestundi, 
        # indent=4 = readable format