import fitz
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk import pos_tag
from string import punctuation
import re

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


pdf_document = "article5.pdf"
doc = fitz.open(pdf_document)
# print("number of pages: %i" % doc.pageCount)

# print(doc.metadata)
text = ""
for i in range(0, doc.pageCount):
    cur_page = doc.loadPage(i)
    text = text+cur_page.getText("text")
# print(text)
# words = word_tokenize(page1text)
text = re.sub("-\n", '', text)  # убираем  переносы
test_string = filter(lambda i: i not in punctuation, text)  # убираем  знаки препинания
test_string = "".join(test_string)
words = re.split('\\s', test_string)  # парсим по пробелам и зн. табуляции
stop_words = set(stopwords.words("english"))  # стоп-слова
# print(punctuation)
sense_words = [word for word in words if not word in punctuation and not word in stop_words]  # !! убрать первое условие
# print(sense_words)
sense_words = [w.lower() for w in sense_words]
lemmatizer = WordNetLemmatizer()
lemmatized = []
word_pos = pos_tag(sense_words)
for p in word_pos:
    part = get_wordnet_pos(p[1])
    try:
        if part != '' and len(part) > 0:
            lem = lemmatizer.lemmatize(p[0], pos=part)
            lemmatized.append(lem)
            # print(p[0], lem)
        else:
            lemmatized.append(lemmatizer.lemmatize(p[0]))
    except KeyError:
        print("ERROR", part, p[0])
# print(lemmatized)
freq = nltk.FreqDist(lemmatized)
print(freq.most_common(30))