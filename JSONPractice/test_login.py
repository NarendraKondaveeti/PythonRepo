from json_reader import read_json       
# read_json() function import chestunnam

data = read_json()                            
# Complete JSON dictionary read chestunnam

username = data["login"]["username"]          # Without Nested data access
password = data["login"]["password"]          # Without Nested data access

print(username)                               # admin
print(password)                               # Admin@123