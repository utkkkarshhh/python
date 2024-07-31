import os
import json

json_file_path = os.path.join('..', 'json', 'user.json')

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def process_data(data):
    first_user = data["users"][0]
    return first_user["name"], first_user["id"]
    

data = read_json_file(json_file_path)
result = process_data(data)
print(result)
