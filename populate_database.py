import requests
from pymongo import MongoClient


db_client = MongoClient()
database = db_client['nobel']

for collection_name in ('prizes', 'laureates'):
    print(f'Fetching collection of {collection_name}..')
    response = requests.get(f'http://api.nobelprize.org/v1/{collection_name[:-1]}.json')
    records = response.json()[collection_name]

    print(f'Saving collection of {collection_name}..')
    database[collection_name].insert_many(records)