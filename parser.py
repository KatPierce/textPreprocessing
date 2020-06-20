import fitz
import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk import pos_tag
from string import punctuation
import re
import pymorphy2
from langdetect import detect
import gbd_connector


# https://stackoverflow.com/questions/15586721/wordnet-lemmatization-and-pos-tagging-in-python
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''


# def rus_text_preprocessing(sense):
#     morph_analyzer = pymorphy2.MorphAnalyzer()
#     for word in sense:
#         lem = morph_analyzer.parse(word)[0].normal_form
#         print(word, lem)
#         lemmatized.append(lem)
#     return lemmatized
#
#
# def eng_text_preprocessing(sense):
#     lemmatizer = WordNetLemmatizer()
#     word_pos = pos_tag(sense)
#     for p in word_pos:
#         part = get_wordnet_pos(p[1])
#         try:
#             if part != '' and len(part) > 0:
#                 lem = lemmatizer.lemmatize(p[0], pos=part)
#                 lemmatized.append(lem)
#                 print(p[0], lem)
#             else:
#                 lemmatized.append(lemmatizer.lemmatize(p[0]))
#         except KeyError:
#             print("ERROR", part, p[0])
#     return lemmatized


# pdf_document = "article5.pdf"
# try:
#     doc = fitz.open(pdf_document)
# except Exception as e:
#     print("Не удалось открыть файл. Проверьте корректность ввода.")
#     exit(1)
# text = ""
# for i in range(0, doc.pageCount):
#     cur_page = doc.loadPage(i)
#     text = text + cur_page.getText("text")
# # print(text)
# lang = detect(text)
# lang_flag = False
# if lang == "ru":
#     stop_words = set(stopwords.words("russian"))
#     lang_flag = True
# elif lang == "en":
#     stop_words = set(stopwords.words("english"))
# else:
#     print("Данная статья нуждается в переводе на английский/русский язык.")
#     exit(1)
#
# text = re.sub(r'-\n', '', text)  # убираем  переносы
# text = re.sub(r'\s{2,}', ' ', text)  # убираем  переносы
#
# KEYWORD_TOKENIZER = RegexpTokenizer(r'\b[\w.\/,-]+\b|[-.,\/()]')
# words = KEYWORD_TOKENIZER.tokenize(text)
#
# sense_words = [word for word in words if not word in stop_words and not word in punctuation]
# print(sense_words)
# sense_words = [w.lower() for w in sense_words]
# lemmatized = []
# if lang_flag:
#     rus_text_preprocessing(sense_words)
# else:
#     eng_text_preprocessing(sense_words)
#
# freq = nltk.FreqDist(lemmatized)
# print(freq.most_common(5))

tagger = gbd_connector.GBDConnector("bolt://localhost:7687", "neo4j", "asdasdasd1")
tagger.print_tags("Болсуновская")
tagger.close()
