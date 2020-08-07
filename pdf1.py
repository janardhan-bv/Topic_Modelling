# import csv
# import PyPDF2
# import nltk
# from tika import parser
# from spacy.en import English
#
# #nltk.download('punkt')
# #nltk.download('averaged_perceptron_tagger')
# #from nltk.corpus import brown
# #nltk.download('brown')
#
# raw = parser.from_file('C://Users//bvjan//Documents//data.pdf')
# my = raw['content']
# print(my)

import re

mylist = ["dog", "cat", "catwild", "thundercat", "cow", "hooo"]
r = re.compile(".*cat")
newlist = list(filter(r.match, mylist)) # Read Note
print(newlist)

