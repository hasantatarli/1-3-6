import pymongo
import datetime
import mongo_credential

client = pymongo.MongoClient(mongo_credential.mongo_url)

db = client['Vocabulary']
vocabularies = db["Vocabularies"]


def add_word(language, word, spelling, turkish_meaning, english_meaning, word_type,usage, first_learning_date, first_repeat, second_repeat, third_repeat):
    document = {
        'Language': language,
        'Word': word,
        'Word Type':word_type,
        'Spelling':spelling,
        'Turkish Meaning': turkish_meaning,
        'English Meaning': english_meaning,
        'Usage':usage,
        'First Learning Date': first_learning_date,
        'First Repeat':first_repeat,
        'Second Repeat' : second_repeat,
        'Third Repeat' : third_repeat,
        'Date added' : datetime.datetime.now()
    }
    return vocabularies.insert_one(document)



def delete_word():
    return 0

def update_word():
    return 0

def get_word(language, word):
    results = vocabularies.find({'Language':language, 'Word':word},{"_id":0, "First Learning Date":0, "First Repeat":0,"Second Repeat":0,"Third Repeat":0,"Date added":0})

    for datas in results:
        print("######################")
        for data in datas:
            print(data.rjust(15,' ') ," : ", datas[data])

        print("######################")



def get_all_words():
    return 0


def get_daily_words():
    return 0

lng = 'English'
wrd = 'Abandon'
wrd_type = 'Verb'
spelling = 'Ebendın'
tr_meaning = 'Terk Etmek, Bırakmak'
eng_meaning = ''
usage = 'He had to abandon his car on the side of the road because it had run out of gas.'
first_learning = None
first_rpt = None
scd_rpt = None
trd_rpt = None

# add_word (language=lng,word= wrd,word_type=wrd_type,spelling=spelling,turkish_meaning=tr_meaning,english_meaning= eng_meaning,usage=usage,first_learning_date=first_learning,first_repeat=first_rpt,second_repeat=scd_rpt,third_repeat=trd_rpt)

get_word('English','Abandon')
