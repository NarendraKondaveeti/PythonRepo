from json_write import read_json          
# JSON read function import chestunnam

data = read_json()  # Updated JSON dictionary read chestunnam

expected_id = data["user_create"]["id"]  # JSON lo update ayina ID read chestunnam

existing_users = [                                     # Existing users simulation
    {"id": 99},
    {"id": 100},
    {"id": 101},
    {"id": 102}
]

ids = [user["id"] for user in existing_users]          
# List Comprehension = Existing users nundi ID list create chestundi

assert expected_id in ids                              
# assert = Expected ID existing users lo undo ledo verify chestundi

print("User Verification Passed")# Verification success message