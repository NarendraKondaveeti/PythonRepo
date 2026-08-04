from JSONPractice.Write.json_write import read_json       # read_json() function import chestunnam

data = read_json()                            # Complete JSON dictionary read chestunnam

firstname = data["user_create"]["firstname"]              # Normal key
lastname = data["user_create"]["lastname"]                # Normal key

city = data["user_create"]["address"]["city"]             # Nested Dictionary access

state = data["user_create"]["address"]["state"]           # Nested Dictionary access

role1 = data["user_create"]["roles"][0]                   # List first value
role2 = data["user_create"]["roles"][1]                   # List second value

print(firstname)
print(city)
print(role1)