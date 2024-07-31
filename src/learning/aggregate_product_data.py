import os
import json

file_path = os.path.join("..", "json", "stock_catalog.json")

def read_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def sum_of_stock(data):
    total_sum = 0
    for product in data.get("products", []):
       total_sum += product.get("price", 0)
    return sum
        

stock_data = read_from_json(file_path)
total_stock_value = sum_of_stock(stock_data)
print(total_stock_value)