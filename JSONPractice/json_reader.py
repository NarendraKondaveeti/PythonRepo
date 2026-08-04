import json                                   
# json = Python built-in module, JSON data ni Python object ga convert chestundi

def read_json():                              # Common reusable function
    with open("testdata.json") as file:  
        # open() = Python built-in function, with = automatic file close
        return json.load(file)             
    # json.loads() = JSON string ni dictionary ga convert chestundi

"""
file = open("testdata.json")
data = json.loads(file.read())
file.close()
"""