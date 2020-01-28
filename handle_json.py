import json

pathname = './data.json'

default = [
	{
		'name': 'user',
		'password': 'pass'
	},
	{
		'name': 'test',
		'password': 'test1234'
	}
]

# Write
# with open(pathname, 'w') as file:
# 	# Escribe el json en el archivo
# 	json.dump(default, file, indent=2)

# Read
with open(pathname) as file:

	response = json.load(file);
	print(response[0])