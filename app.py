from pymongo import MongoClient
import random
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

password = os.environ.get("MONGO_PWD")

con_str = f"mongodb+srv://sill0:{password}@cluster0.skrqstu.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(con_str)
db = client['silldatabase']
collection = db['movies']


def get_random_movie():
    count = collection.count_documents({})
    random_index = random.randint(0, count - 1)
    random_movie = collection.find().limit(1).skip(random_index)[0]
    return {
        'title': random_movie['title'],
        'genres': random_movie['genres'],
        'runtime': random_movie['runtime'],
        'imdb_score': random_movie['imdb_score']
    }

def main():
    random_movie = get_random_movie()
    print('Randomly selected movie:', random_movie['title'])
    print('genres:', random_movie['genres'])
    print('runtime:', random_movie['runtime'])
    print('imdb_score:', random_movie['imdb_score'])

if __name__ == '__main__':
    main()