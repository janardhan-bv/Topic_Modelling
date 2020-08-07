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
# ****************************************************************************************************
import xlsxwriter
from nltk.corpus import wordnet
synonyms = []
# workbook = xlsxwriter.Workbook('Example2.xlsx')
# worksheet1 = workbook.add_worksheet()

row = 0

for t in t5:
    column = 1
    for syn in wordnet.synsets(t):
        for l in syn.lemmas():
            synonyms.append(l.name())
            print(l.name())
            worksheet.write(row, column, l.name())
            column += 1
#        print("end of 1st inner most")
#    print("end of 2nd for")
    print(set(synonyms))
    row += 1

workbook.close()
# *********************************************************************************