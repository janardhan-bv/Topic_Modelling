import nltk
from tika import parser
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import brown

nltk.download('brown')

raw = parser.from_file('C://Users//bvjan//Documents//data.pdf')
my = raw['content']
print(my)

words = nltk.word_tokenize(my)
t1 = nltk.pos_tag(words)
print(t1)

train = {}
train['tag'] = t1
t5 = ([t[0] for t in train['tag'] if ((t[1] == 'NN') or (t[1] == 'NNS'))])
print(t5)
for t in t5:
    if not (len(t) > 2):
        t5.remove(t)
print(t5)

# ********************************************************************************
import xlsxwriter

workbook = xlsxwriter.Workbook('Example2.xlsx')
worksheet = workbook.add_worksheet()

# Start from the first cell.
# Rows and columns are zero indexed.
row = 0
column = 0

content = t5
# iterating through content list
for item in content:
    # write operation perform
    worksheet.write(row, column, item)

    # incrementing the value of row by one
    # with each iteratons.
    row += 1

#workbook.close()

# ********************************************************************************************

# from PyDictionary import PyDictionary
#
# dictionary=PyDictionary(t5)
#
# print (dictionary.getSynonyms())

# ****************************************************************************************
# import requests
# from bs4 import BeautifulSoup
#
# def synonyms(term):
#     response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
#     soup = BeautifulSoup(response.text, 'html.parser')
#     soup.find('section', {'class': 'synonyms-container'})
#     return [span.text for span in soup.findAll('a', {'class': 'css-18rr30y'})]  # class = .css-7854fb for less relevant
#
# print(synonyms("reticulum"))

# ************************************************************************************

# from nltk.corpus import wordnet
# for t in t5:
#     syns = wordnet.synsets(t)
#     syns
#     print(syns)
from nltk.corpus import wordnet
synonyms = []

for t in t5:
    print(t)
    for syn in wordnet.synsets(t):
        for l in syn.lemmas():
            synonyms.append(l.name())
        print("end of 1st inner most")
    print("end of 2nd for")
    print(set(synonyms))
