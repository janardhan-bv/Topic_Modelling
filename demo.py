import csv

filename = "C://Users//bvjan//Documents//book1.csv"
fields = [5]
rows = [101]

with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    # extracting field names through first row
    fields = next(csvreader)
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
        # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))
    # printing the field names
print('Field names are:' + ', '.join(field for field in fields))

filename1 = "C://Users//bvjan//Documents//book2.csv"
fields1 = [7]
rows1 = [1300]

with open(filename1, 'r') as csvfile1:
    # creating a csv reader object
    csvreader1 = csv.reader(csvfile1)
    # extracting field names through first row
    fields1 = next(csvreader1)
    # extracting each data row one by one
    for row in csvreader1:
        rows.append(row)
        # get total number of rows
    print("Total no. of rows: %d" % (csvreader1.line_num))
    # printing the field names
print('Field names are:' + ', '.join(field for field in fields1))

