import os
import json

file_path = os.path.join("..", "json", "users.json")

def read_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def process_data_and_filter_by_age(data):
    filtered_users = [user for user in data if user.get('age' , 0) > 30]
    return filtered_users
        

data = read_from_json(file_path)
results = process_data_and_filter_by_age(data)
print(results)


# Write a function that filters and returns users who are older than 30 from the user.json file.
