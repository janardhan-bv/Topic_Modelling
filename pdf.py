import csv
import PyPDF2
import nltk
from tika import parser
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

raw = parser.from_file('C://Users//bvjan//Documents//data.pdf')
my = raw['content']
#page1 = my.split()
#print(page1)

# pdfFileObj = open('C://Users//bvjan//Documents//data.pdf', 'rb')
# # pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# # number of pages in pdf
# print(pdfReader.numPages)
# # a page object
# pageObj = pdfReader.getPage(0)
# # extracting text from page.
# # this will print the text you can also save that into String
# page = pageObj.extractText()
# page1 = page.split()
# print(page1)

words = nltk.word_tokenize(my)
nltk.pos_tag(words)
print(words)
grammar = "NP: {<DT>?<JJ>*<NN>}"
parser = nltk.RegexpParser(grammar)
t = parser.parse(nltk.pos_tag(words))
[str(s.leaves()) for s in t.subtrees() if s.label() == "NP"]


# csv.register_dialect('myDialect', delimiter='/', quoting=csv.QUOTE_NONE)
# myfile = open('sample.csv', 'w')
# with myfile:
#     writer = csv.writer(myfile, dialect= 'myDialect')
#     writer.writerows(page1)
