import pymongo
from datetime import date
from datetime import datetime
import mongo_credential

class Word:
    def __init__(self):
        client = pymongo.MongoClient(mongo_credential.mongo_url)
        db = client['Vocabulary']
        vocabularies = db["Vocabularies"]
        words = db["Words"]

        self.db = db
        self.vocabularies = vocabularies
        self.words = words

    def add_from_csv(self, txt_file):
        with open(txt_file,"r", encoding="UTF-8") as f:
            lines = f.readlines()

            for line in lines:
                lng = line.split("|")[0]
                wrd = line.split("|")[1]
                wrd_type = line.split("|")[2]
                spl = line.split("|")[3]
                tr = line.split("|")[4]
                eng = line.split("|")[5]
                exp = line.split("|")[6].replace("\n","")
                # for column in columns:
                #     # lng = column[0]
                #     # word  = column[1]
                print(lng,wrd,wrd_type,spl,exp)

                self.add_word(lng,wrd,spl,tr,eng,wrd_type,exp)
                    #print(lng,word)

    #def add_word(self,language, word, spelling, turkish_meaning, english_meaning, word_type,usage, first_learning_date, first_repeat, second_repeat, third_repeat):
    def add_word(self,language, word, spelling, turkish_meaning, english_meaning, word_type,usage):
        document = {
            'Language': language,
            'Word': word,
            'Word Type':word_type,
            'Spelling':spelling,
            'Turkish Meaning': turkish_meaning,
            'English Meaning': english_meaning,
            'Usage':usage,
            # 'First Learning Date': first_learning_date,
            # 'First Repeat':first_repeat,
            # 'Second Repeat' : second_repeat,
            # 'Third Repeat' : third_repeat,
            'Date added' : datetime.now()
        }
        return self.word.insert_one(document)

    def add_word_new(self,word, word_type, definition, usage,  languageId,  addedby):
        word = {
                'Word' : word,
                'WordType':word_type,
                'Definition':definition,
                'UsageExample':usage,
                'LanguageId' :  languageId,
                'DateAdded':datetime.now(),
                'AddedBy':addedby
                }
        
        return self.words.insert_one(word)
    
    def get_wordID(self,word):
        result = self.words.find_one({"Word" : word})

        return result


    def delete_word(self):
        self.vocabularies.delete_many({})

    def update_word(self, lang, word,wt=None, spl=None, tm=None, em=None, usa=None, nw_lang=None,nw_word=None,nw_wt=None, nw_spl=None, nw_tm=None, nw_em=None, nw_usa=None):
        filter = {}
        new_values = {}
           

        if (lang != None):
            filter.update({"Language":lang})
        if (word != None):
            filter.update({"Word":word})            
        if (wt != None):
            filter.update({"Word Type":wt})
        if (spl != None):
            filter.update({"Spelling":spl})
        if (tm != None):
            filter.update({"Turkish Meaning":tm})
        if (em != None):
            filter.update({"English Meaning":em})  
        if (usa != None):
            filter.update({"Usage":usa})                                                                                                                                                                                              

        if (nw_lang != None):
            new_values.update({"Language":nw_lang})
        if (nw_word != None):
            new_values.update({"Word":nw_word})            
        if (nw_wt != None):
            new_values.update({"Word Type":nw_wt})
        if (nw_spl != None):
            new_values.update({"Spelling":nw_spl})
        if (nw_tm != None):
            new_values.update({"Turkish Meaning":nw_tm})
        if (nw_em != None):
            new_values.update({"English Meaning":nw_em})  
        if (nw_usa != None):
            new_values.update({"Usage":nw_usa})

        new_values = { "$set": new_values  }
        
        
        print(filter)
        print(new_values)
        result = self.vocabularies.update_one(filter,new_values)
        
    def update_first_learning_date(self,language, word):
        filter = {"Language": language, "Word": word}
        new_values = { "$set": {'First Learning Date': datetime.combine(date.today(),datetime.min.time())} }

        result = self.vocabularies.update_one(filter,new_values)

    def update_first_repeat_date(self,language, word):
        filter = {"Language": language, "Word": word, }
        new_values = { "$set": {'First Repeat': datetime.combine(date.today(),datetime.min.time())} }

        result = self.vocabularies.update_one(filter,new_values)

    def update_second_repeat_date(self,language, word):
        filter = {"Language": language, "Word": word}
        new_values = { "$set": {'Second Repeat': datetime.combine(date.today(),datetime.min.time())} }

        result = self.vocabularies.update_one(filter,new_values)

    def update_third_repeat_date(self,language, word):
        filter = {"Language": language, "Word": word}
        new_values = { "$set": {'Third Repeat': datetime.combine(date.today(),datetime.min.time())} }

        result = self.vocabularies.update_one(filter,new_values)




    def get_word(self,language, word):
        results = self.vocabularies.find({'Language':language, 'Word':word},{"_id":0, "First Learning Date":0, "First Repeat":0,"Second Repeat":0,"Third Repeat":0,"Date added":0})

        for datas in results:
            print("######################")
            for data in datas:
                print(data.rjust(15,' ') ," : ", datas[data])
                

            print("######################")



    def get_all_words(self):
        results = self.vocabularies.find({},{"_id":0, "First Learning Date":0, "First Repeat":0,"Second Repeat":0,"Third Repeat":0,"Date added":0})
        
        for datas in results:
            print("######################")
            for data in datas:
                print(data.rjust(15,' ') ," : ", datas[data])

            print("######################")



    # Daily New Words
    # Criteria: First Learning Date is null
    def get_new_words(self):
        results = self.vocabularies.aggregate([{ '$match': { 'First Learning Date': None, 'Word': 'book'}}, {'$sample': {'size': 5}}])

        for datas in results:
            print("######################")
            print(datas)
            lang = datas.get("Language")
            word = datas.get("Word")
            
            for data in datas:
                print(data.rjust(20,' ') ," : ", datas[data])


            self.update_first_learning_date(lang,word)    
            
            print("######################")


    # Daily Firstly repeat words
    # Criteria: First Learning Date is not null, First Repeat is null and First Learning Date
    def get_first_repeat_words(self):
        #results = self.vocabularies.aggregate([{'$match': { 'First Learning Date': { '$ne' : True}, 'First Repeat' : None }}, {'$sample': {'size': 5}}])
        results = self.vocabularies.aggregate([
        {
            '$match': {
                'First Learning Date': {
                    '$ne': None
                }, 
                'First Repeat': None,
                'Word':'book'
            }
        }, {
            '$project': {
                '_id': 0, 
                'Language': 1, 
                'Word': 1, 
                'Word Type': 1, 
                'Spelling': 1, 
                'Turkish Meaning': 1, 
                'English Meaning': 1, 
                'Usage': 1, 
                'First Learning Date': 1, 
                'First Repeat': 1, 
                'Second Repeat': 1, 
                'Third Repeat': 1, 
                'daysince': {
                    '$divide': [
                        {
                            '$subtract': [
                                datetime.combine(date.today(),datetime.min.time()) , '$First Learning Date'
                            ]
                        }, (1000*60*60*24)
                   ]
                }
            }
        }, 
        {
            '$match': {
                'daysince': { "$gt": 0, "$lte":1}
            }
        },
        {
          '$sample': {'size': 5}  
        }])

        for datas in results:
            print("######################")
            print(datas)
            lang = datas.get("Language")
            word = datas.get("Word")
            
            for data in datas:
                print(data.rjust(20,' ') ," : ", datas[data])

            self.update_first_repeat_date(lang,word)    
            
            print("######################")
        

    def get_second_repeat_words(self):
        results = self.vocabularies.aggregate([
        {
            '$match': {
                'First Learning Date': {
                    '$ne': None
                }, 
                'First Repeat': {
                    '$ne': None
                }, 
                'Second Repeat' : None
            }
        }, {
            '$project': {
                '_id': 0, 
                'Language': 1, 
                'Word': 1, 
                'Word Type': 1, 
                'Spelling': 1, 
                'Turkish Meaning': 1, 
                'English Meaning': 1, 
                'Usage': 1, 
                'First Learning Date': 1, 
                'First Repeat': 1, 
                'Second Repeat': 1, 
                'Third Repeat': 1, 
                'daysince': {
                    #'$trunc': {
                        '$divide': [
                            {
                                '$subtract': [
                                    datetime.combine(date.today(),datetime.min.time()) , '$First Learning Date'
                                ]
                            }, (1000*60*60*24) 
                        ]
                    #}
                }
            }
        }, {
            '$match': {
                'daysince': { "$gt": 2, "$lte":3}
            }
        },
        {'$sample': {'size': 5}}])

        for datas in results:
            print("######################")
            print(datas)
            lang = datas.get("Language")
            word = datas.get("Word")
            
            for data in datas:
                print(data.rjust(20,' ') ," : ", datas[data])

            self.update_second_repeat_date(lang,word)    
            
            print("######################")

    def get_third_repeat_words(self):
        results = self.vocabularies.aggregate([
        {
            '$match': {
                'First Learning Date': {
                    '$ne': None
                }, 
                'First Repeat': {
                    '$ne': None
                }, 
                'Second Repeat' : {
                    '$ne': None
                }, 
                'Third Repeat': None
            }
        }
        , {
            '$project': {
                '_id': 0, 
                'Language': 1, 
                'Word': 1, 
                'Word Type': 1, 
                'Spelling': 1, 
                'Turkish Meaning': 1, 
                'English Meaning': 1, 
                'Usage': 1, 
                'First Learning Date': 1, 
                'First Repeat': 1, 
                'Second Repeat': 1, 
                'Third Repeat': 1, 
                'daysince': {
                    
                        '$divide': [
                            {
                                '$subtract': [
                                    datetime.combine(date.today(),datetime.min.time()) , '$First Learning Date'
                                ]
                            }, (1000*60*60*24) 
                        ]
                   
                }
            }
        }
        , {
            '$match': {
                'daysince': { "$gt": 5, "$lte":6}
            }
        }
        ,{'$sample': {'size': 5}}
        ])

        for datas in results:
            print("######################")
            print(datas)
            lang = datas.get("Language")
            word = datas.get("Word")
            
            for data in datas:
                print(data.rjust(20,' ') ," : ", datas[data])

            self.update_third_repeat_date(lang,word)    
            
            print("######################")
