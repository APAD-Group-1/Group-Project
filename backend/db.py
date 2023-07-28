import pymongo
from dotenv import load_dotenv
import os
import certifi

load_dotenv()
DB_STRING = os.getenv("DB_STRING")

ca=certifi.where()

# establish connection and create database
client = pymongo.MongoClient(DB_STRING, tlsCAFile=ca)
db = client['pythonTest']

# input user data to users collection
user_col = db['users']
users = [
    {'_id': 'jf123', 'fname': 'Jacob', 'lname': 'Foster', 'email': 'jacob@jacob.com', 'password': '$2b$12$DRtA2TBI8D8mDHoV9G8vLe/DoQMJqMup6/7Ds76GqEkwqLb44MNIe', 'salt': '$2b$12$DRtA2TBI8D8mDHoV9G8vLe', 'projects': [1]},
    {'_id': 'ev123', 'fname': 'Enrique', 'lname': 'Villarreal', 'email': 'erique@enrique.com', 'password': '$2b$12$AGQui/lR.BvSIWv2VHerzO417NHYJ.B9FBUkp5NjJ94U3GJmXt5jW', 'salt': '$2b$12$AGQui/lR.BvSIWv2VHerzO', 'projects': []},
    {'_id': 'sg123', 'fname': 'Srishti', 'lname': 'Gupta', 'email': 'srishti@srishti.com', 'password': '$2b$12$HQOxvV47s89hT6wiGlheTeqhcXPVU/hpuvsW4Hy6hipYrayE6kEku', 'salt': '$2b$12$HQOxvV47s89hT6wiGlheTe', 'projects': []},
    {'_id': 'ab123', 'fname': 'Aishwarya', 'lname': 'Bhosle', 'email': 'aishwarya@aishwarya.com', 'password': '$2b$12$9fxyE9FKVymet6/pOGZUFOkNQ.qmpBbVGhl4xhpxsbopLYjIB3Gue', 'salt': '$2b$12$9fxyE9FKVymet6/pOGZUFO', 'projects': []},
    {'_id': 'sy123', 'fname': 'Suhas', 'lname': 'Yogish', 'email': 'suhas@suhas.com', 'password': '$2b$12$F7RhEeuuhP32AiS2FYDXbe0MdgKTrEenkg8JB7LogDlOjZPTzWL5e', 'salt': '$2b$12$F7RhEeuuhP32AiS2FYDXbe', 'projects': []}
]

proj_col = db['projects']
projects = [
    {'_id': 1, 'name': 'First Project', 'description': 'This is the first project', 'users': ['jf123'], 'creator': 'jf123', 'hardware': []}
]

hardware_col = db['hardware']
hardware = [
    {'_id': 1, 'name': 'Hardware Set 1', 'checkedOut': 0, 'projects': [], 'capacity': 1000},
    {'_id': 2, 'name': 'Hardware Set 2', 'checkedOut': 0, 'projects': [], 'capacity': 1000},
    {'_id': 3, 'name': 'Hardware Set 3', 'checkedOut': 0, 'projects': [], 'capacity': 1000},
    {'_id': 4, 'name': 'Hardware Set 4', 'checkedOut': 0, 'projects': [], 'capacity': 1000},
    {'_id': 5, 'name': 'Hardware Set 5', 'checkedOut': 0, 'projects': [], 'capacity': 1000}
]

user_col.insert_many(users)
hardware_col.insert_many(hardware)
proj_col.insert_many(projects)