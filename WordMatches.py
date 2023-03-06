import pymongo
from datetime import date
from datetime import datetime
import mongo_credential


class WordMatch:
    def __init__(self):
        client = pymongo.MongoClient(mongo_credential.mongo_url)
        db = client['Vocabulary']
        wordMatch = db["WordMatches"]

        self.db = db
        self.wordMatch = wordMatch


    def add_match(self, sourceWord,targetWord, sourceLang, targetLang, addedBy):
        document = {
            'SourceWordID': sourceWord,
            'TargetWordID':targetWord,
            'SourceLanguageID':sourceLang,
            'TargetLanguageID':targetLang,
            'AddedBy': addedBy,
            'DateAdded' : datetime.now()
        }
        return self.wordMatch.insert_one(document)
    

    # def get_all_match(self):
    #     results = self.matchs.find({},{"_id":0, "match":1})

    #     for datas in results:
    #         print("######################")
    #         for data in datas:
    #             print(data.rjust(15,' ') ," : ", datas[data])
                

    #         print("######################")

    # def get_match(self, match):
    #     results = self.matchs.find({},{"_id":1, "match":1})

    #     for datas in results:
    #         print("######################")
    #         for data in datas:
    #             print(data.rjust(15,' ') ," : ", datas[data])
                

    #         print("######################")
    
    # def get_matchId(self, match):
    #     results = self.matchs.find_one({"match":match},{"_id":1})

    #     # for datas in results:
    #     #     print("######################")
    #     #     for data in datas:
    #     #         print(data.rjust(15,' ') ," : ", datas[data])
                

    #     #     print("######################")
    #     return results

    # def delete_match():
    #     pass

    # def update_match():
    #     pass