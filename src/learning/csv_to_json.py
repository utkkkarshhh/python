import os, json, csv

file_path = os.path.join("..","json","my_csv.csv")
output_path = os.path.join(".", "log", "csv_to_json.json")

def read_csv(file_path):
    with open (file_path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader) #
        data = []
        for row in csv_reader:
            data.append(row)
        return data
    
def read_csv_as_dict(file_path):
    with open(file_path, "r", newLine='') as file:
        csv_reader = csv.DictReader(file)
        data = []
        for row in csv_reader:
    
def write_to_json(data):
    with open(output_path, 'w') as json_file:
        json.dump(data, json_file, indent = 4)
    

result = read_csv(file_path)
print(result)

