import json

my_dict = {
            'name': 'Sulav',
            'age': 23
        }

json_string = json.dumps(my_dict, indent=4)

print("Serializing dictionary to JSON....")
print(json_string)

decoded_json = json.loads(json_string)

print("Deserializing JSON back to dictionary")
print(decoded_json)
