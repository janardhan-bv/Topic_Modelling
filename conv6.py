import nltk
import pandas as pd
import xlrd
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
t5 = ([t[0] for t in train['tag'] if ((t[1] == 'NN') or (t[1] == 'NNS') or (t[1] == 'VBG') or (t[1] == 'VBD'))])
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
row = 1
column = 0

content = t5
# iterating through content list
for item in content:
    # write operation perform
    worksheet.write(row, column, item)

    # incrementing the value of row by one
    # with each iteratons.
    row += 1

# ****************************************************************************************************
from nltk.corpus import wordnet
synonyms = []

row = 1

for t in t5:
    column = 3
    for syn in wordnet.synsets(t):
        for l in syn.lemmas():
            synonyms.append(l.name())
            worksheet.write(row, column, l.name())
            column += 1
    row += 1

#workbook.close()

# workbook1 = xlrd.open_workbook('Example2.xlsx')
# t6 = workbook1.sheet_by_name('Sheet1')
# print(t6.cell(0,0).value)

# *********************************************************************************
#workbook = xlsxwriter.Workbook('Example2.xlsx')
#worksheet = workbook.add_worksheet()
row = 1
name = 'name'
number = 'number'
prob = 'probablity'
worksheet.write('A1', name)
worksheet.write('B1', number)
worksheet.write('C1', prob)
x = len(t5)
a = []
for i in range(1, 2):
    count = 0
    column = 1
    print(t5[i])

    #worksheet.write(row, column, t5[i])
    for k in range(i+1, 3):
        print("Value=",k)
        if t5[i] == t5[k]:
            count += 1
        else:
            for j in range(3,20):
                if t5[i] ==t6.cell(k,j).value:
                    t5[k] =t6.cell(k,j).value
                    count +=1
                    break

    worksheet.write(row, column, count)
    worksheet.write(row, column+1, count/x)
    row += 1
    a.append(count)
#print(a)
workbook.close()

# *******************************************************************
import pandas as pd

file_df = pd.read_excel("Example3.xlsx")

# Keep only FIRST record from set of duplicates
file_df_first_record = file_df.drop_duplicates(subset=["name"], keep="first")
file_df_first_record.to_excel("Records.xlsx", index=False)

# **********************************************************************

