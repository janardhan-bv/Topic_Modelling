import csv
import PyPDF2
import nltk
from tika import parser
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import brown
nltk.download('brown')
import xlsxwriter

raw = parser.from_file('C://Users//bvjan//Documents//data.pdf')
my = raw['content']
print(my)

words = nltk.word_tokenize(my)
t1 = nltk.pos_tag(words)
print(t1)

# t2 = nltk.corpus.brown.tagged_words(tagset='NN')
# print(t2)
# grammar = "NP: {<DT>?<JJ>*<NN>}"
# parser = nltk.RegexpParser(grammar)
# t = parser.parse(nltk.pos_tag(words))
# [str(s.leaves()) for s in t.subtrees() if s.label() == "NP"]

train = {}
train['tag'] = t1
t5 = ([t[0] for t in train['tag'] if ((t[1] == 'NN') or (t[1] == 'NNS'))])
print(t5)
for t in t5:
    if not (len(t)>2):
        t5.remove(t)
print(t5)

#new_list = t5
# with xlsxwriter.Workbook('test.xlsx') as workbook:
#     worksheet = workbook.add_worksheet()
#
#     for row_num, data in enumerate(new_list):
#         worksheet.write_row(row_num, 0, data)

#csv.register_dialect('myDialect', delimiter='/', quoting=csv.QUOTE_NONE)
# myfile = open('sample.csv', 'w')
# with myfile:
#     writer = csv.writer(myfile, lineterminator='\n')
#     writer.writerows(t5)

