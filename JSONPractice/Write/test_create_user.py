from json_write import read_json, write_json    
# JSON read/write functions import chestunnam

data = read_json()                                     
# Complete JSON dictionary read chestunnam

payload = data["user_create"]                          
# user_create object ni payload ga use chestunnam

response = {                                           
    # API response simulation
    "id": 101
}

data["user_create"]["id"] = response["id"]             
# Response ID ni existing JSON dictionary lo update chestunnam

write_json(data)                                       
# Updated dictionary ni JSON file lo overwrite chestunnam

print("User ID :", response["id"])                     
# Updated ID print chestunnam