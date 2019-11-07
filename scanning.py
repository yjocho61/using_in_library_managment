import csv


def Scan_print(id, book_info, exist = False):
    if row[2] == id:
        print(row[4], '\n', row[5], '\n', row[6])
        f.write('\n')
        f.write(row[2])
        exist = True
    return exist


while True:
    exist = False  #initialize the existence of the book
    book_id = input('')
    with open('save.csv', 'a', encoding = 'utf-8-sig') as f:
        with open('nmsbooklist.csv', newline='', encoding = 'utf-8-sig') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                exist = Scan_print(book_id, row)
                if exist == True:
                    break
            if exist == 0:
                print('DOES NOT EXIST')
    print('===================================================')
