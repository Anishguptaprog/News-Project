from fastapi import FastAPI
from models import TestDB
from mongoengine import connect
import json
import requests
import logging
app = FastAPI()

try:
    connect(host="mongodb+srv://anishajaygupta21:LI8c8acZMAATaSQk@cluster0.l5gigm6.mongodb.net/hrms?retryWrites=true&w=majority")

    # If the response was successful, no Exception will be raised

except Exception as err:
    logging.error('Other error occurred', exc_info=True)
    # fetching data in json format


@app.get("/")
def home():
    return {"message": "Hello World"}


@app.get("/get_all_data")
def get_all_data():
    stud = json.loads(TestDB.objects().to_json())
    # stud_list = json.loads(stud)
    # return {"studs": stud}
    print("2")
    return stud
