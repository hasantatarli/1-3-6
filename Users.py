import pymongo
from datetime import date
from datetime import datetime
import mongo_credential


class User:
    def __init__(self):
        client = pymongo.MongoClient(mongo_credential.mongo_url)
        db = client['Vocabulary']
        users = db["Users"]

        self.db = db
        self.users = users

    def add_user(self, firstName, lastName, userName, password, email ):
        document = {
            'FirstName': firstName,
            'LastName': lastName,
            'UserName': userName,
            'Password': password,
            'Email': email
        }

        return self.users.insert_one(document)
    
    def get_all_user(self):
        results = self.users.find({})

        for result in results:
            print(result, results[result])