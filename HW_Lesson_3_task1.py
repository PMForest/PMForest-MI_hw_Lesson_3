from pymongo import MongoClient
from pprint import pprint

MONGO_URL = '127.0.0.1:27017'


with MongoClient(MONGO_URL) as client:
    MONGO_DB = 'vacancy_db'
    vacancy_db = client[MONGO_DB]
    vacancy_db.print_salary(300_000)


vacancy_db.collection.update_one({'vacancy_link':
                                  'https://hh.ru/search/vacancy?clusters=true&'\
                                  'enable_snippets=true&salary=&st=searchVacancy&text=python'},
                                 )
objects = vacancy_db.collection.find().limit(1)
for obj in objects:
    pprint(obj)
    vacancy_db.search_job(client)
    objects = vacancy_db.collection.find().limit(1)
    for obj in objects:
        pprint(obj)