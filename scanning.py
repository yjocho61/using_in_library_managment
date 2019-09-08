import csv


while True:
    c = 0
    name = input('')
    with open('save.csv', 'a', encoding = 'utf-8-sig') as f:
        with open('nmsbooklist.csv', newline='', encoding = 'utf-8-sig') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                try:
                    if row[2] == name:
                        #print(row)
                        print(row[4], '\n', row[5], '\n', row[6])
                        f.write('\n')
                        f.write(row[2])
                        c += 1
                except IndexError:
                  print(row)
            if c == 0:
                print('DOES NOT EXIST')
            elif c > 1:
                print('MORE THAN ONE BOOKS')
    print('===================================================')
