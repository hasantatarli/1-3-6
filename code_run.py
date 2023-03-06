import Words
import Languages
import WordMatches
import Users
# Parameters: language,word,word_type, spelling,translate_lang, meaning, usage, addedby
# voc = Words.Vocabulary()
# voc.add_word_new("Türkçe","Kitap","Noun", "buuk",  "German","Buch", "I bought a new book to learn English from beginning","htatarli")


lang = Languages.Language()
word = Words.Word()
wordMatch = WordMatches.WordMatch()
user = Users.User()
# lang.add_language("Türkçe","htatarli")
# lang.add_language("English","htatarli")
# lang.add_language("German","htatarli")
# lang.add_language("Spanish","htatarli")

#lang.get_all_languages()

# result = lang.get_languageId("Türkçe")
# langId = result.get("_id")


#word.add_word_new("Kitap", "İsim", "basılı ya da el yazılı kâğıt yaprakların ciltli ya da ciltsiz olarak bir araya getirilmiş biçimi","Baştan ingilizce öğrenmek için yeni bir kitap aldım",langId,"htatarli")

#sourceWord = word.get_wordID("Book")
#targetWord = word.get_wordID("Kitap")

# print(sourceWord["_id"],sourceWord["Word"],targetWord["_id"],targetWord["Word"])

#wordMatch.add_match(sourceWord["_id"],sourceWord["LanguageId"],targetWord["_id"],targetWord["LanguageId"],"htatarli")






# lng = 'English'
# wrd = 'Abandon'
# wrd_type = 'Verb'
# spelling = 'Ebendın'
# tr_meaning = 'Terk Etmek, Bırakmak'
# eng_meaning = ''
# usage = 'He had to abandon his car on the side of the road because it had run out of gas.'
# first_learning = None
# first_rpt = None
# scd_rpt = None
# trd_rpt = None

# add_word (language=lng,word= wrd,word_type=wrd_type,spelling=spelling,turkish_meaning=tr_meaning,english_meaning= eng_meaning,usage=usage,first_learning_date=first_learning,first_repeat=first_rpt,second_repeat=scd_rpt,third_repeat=trd_rpt)

# get_word('English','Abandon')

# add_from_csv("Vocabulary.csv") 
# delete_word()

#get_all_words()

# This function gets all daily words: 1 - New Words, 2- First Repeat Words, 3- Second Repeat Words, 4- Third Repeat Words
# Total Maximum 20 Words to memorize.

# voc.get_all_words()
# print("-------------- New Words ------------------")
# voc.get_new_words()
# print("-------------- First Repeat ------------------")
#voc.get_first_repeat_words()
# print("-------------- Second Repeat ------------------")
# voc.get_second_repeat_words()
# print("-------------- Third  Repeat ------------------")
# voc.get_third_repeat_words()
# voc.get_new_words()

# voc.add_from_csv("Vocabulary.csv")

# lang = None #"English"
# word = "Book"
# filter = {}
# new_values = {} 

# if (lang != None):
#     filter.update({"Language":lang})
# if (word != None):
#     filter.update({"Word":word})


# voc.update_word(lang="English",word="book",nw_wt="Noun",nw_usa="I bought a new book to learn English from beginning")
# add_word_new(self,language,translate_lang, word,word_type, spelling,meaning, usage):

user.add_user('Hasan','Tatarlı','htatarli','1234','hasantatarli@gmail.com')

user.get_all_user()