import csv
from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

password = os.environ.get("MONGO_PWD")

con_str = f"mongodb+srv://sill0:{password}@cluster0.skrqstu.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(con_str)
db = client['silldatabase']
collection = db['movies']

with open('titles_cleaned.csv', 'r', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        collection.insert_one(row)