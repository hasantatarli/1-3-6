import pymongo
from datetime import date
from datetime import datetime
import mongo_credential


class Language:
    def __init__(self):
        client = pymongo.MongoClient(mongo_credential.mongo_url)
        db = client['Vocabulary']
        languages = db["Languages"]

        self.db = db
        self.languages = languages 


    def add_language(self, langName, addedBy):
        document = {
            'Language': langName,
            'AddedBy': addedBy,
            'DateAdded' : datetime.now()
        }
        return self.languages.insert_one(document)
    

    def get_all_languages(self):
        results = self.languages.find({},{"_id":0, "Language":1})

        for datas in results:
            print("######################")
            for data in datas:
                print(data.rjust(15,' ') ," : ", datas[data])
                

            print("######################")

    def get_language(self, language):
        results = self.languages.find({},{"_id":1, "Language":1})

        for datas in results:
            print("######################")
            for data in datas:
                print(data.rjust(15,' ') ," : ", datas[data])
                

            print("######################")
    
    def get_languageId(self, language):
        results = self.languages.find_one({"Language":language},{"_id":1})

        # for datas in results:
        #     print("######################")
        #     for data in datas:
        #         print(data.rjust(15,' ') ," : ", datas[data])
                

        #     print("######################")
        return results

    def delete_language():
        pass

    def update_language():
        pass