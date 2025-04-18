import json

data = {
    "name": "John Doe",
    "age": 25,
    "city": "Dhaka",
    "is_student": False,
    "courses": ["Python", "Cyber Security"]
}

json_data = json.dumps(data, indent=4)  # Convert to JSON with indentation
print(json_data)
