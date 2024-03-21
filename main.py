import random
from pymongo import MongoClient
import local_settings

client = MongoClient(
    host=local_settings.DATABASE['host'], port=local_settings.DATABASE['port'])

mongodb_database = client[local_settings.DATABASE['name']]

collections = mongodb_database.list_collection_names()

if 'phones' in collections:
    phone_collection = mongodb_database.get_collection('phones')
else:
    phone_collection = mongodb_database['phones']

cities = ['Tehran', 'Mashhad', 'Shiraz', 'Tabriz', 'Ahvaz']

phones_data = []
for _ in range(25):
    rand_int = random.randint(1, 99)
    rand_int_mobile = random.randint(10000000, 99999999)
    new_phone = dict(first_name=f"first_name_{rand_int}", last_name=f"last_name_{rand_int}",
                     mobile=f"091{rand_int_mobile}", city=random.choice(cities))
    phones_data.append(new_phone)

result = phone_collection.insert_many(phones_data)

# print last_name and mobile where city=Shiraz
myquery = {"city": "Shiraz"}

phones = phone_collection.find(myquery)

for i, phone in enumerate(phones):
    print(i, " => ", phone["last_name"], " => ", phone["mobile"])
