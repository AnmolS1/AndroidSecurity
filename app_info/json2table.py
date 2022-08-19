import json
from HashTable import HashTable

# load the data into a json object
data = json.load(open('doc.json'))

# look at the data
# print(json.dumps(app_list, indent=4))

# create hashtable object
app_table = HashTable(len(data))

# put all the data in the hashtable
for app in data:
	app_table.set(app['_id'], app)

print(app_table.hash_table[0][0])

# print(app_table)