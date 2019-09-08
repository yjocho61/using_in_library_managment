import time
import requests
from bs4 import BeautifulSoup

def category(num):
    for label in num:
        if label.isdigit():
            return label

def login():
    usercode = input('帳號:')
    password = input('密碼:')

    payload = {'usercode':usercode,'password':password,'Image11.x':'0','Image11.y':'0'}
    rs = requests.session()
    res = rs.post('http://hylib.ksml.edu.tw/Login', data = payload)

    soup = BeautifulSoup(res.text,'html.parser')
    informs = soup.select('tr td')
    if len(informs) > 0:
        print(informs[5].text)
        return login()
    else:
        return rs

def hist(url, rs):
    res = rs.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    informs = soup.select('td')


    hist = dict()
    hist2 = dict()
    w = []

    k = len(informs)
    i = 34

    while True:
        if k > i:
            t = informs[i + 4].text
            c = category(t)
            u = informs[i].text, c
            print(u[0], t)
            if c not in hist:
                hist[c] = 1
            else:
                hist[c] += 1
            if c not in hist2:
                w.append(u)
                hist2[c] = 1
            elif c in hist2 and u not in w:
                w.append(u)
                hist2[c] += 1

            i += 15
        else:
            break
        
    for key in hist:
        print(key, '類:', hist[key], '冊,', hist2[key], '人')

def findlending(date, rs):
    url1 = 'http://hylib.ksml.edu.tw/cir/History.do?selectReaderName=&selectReaderCode=&selectReaderTypeId=&selectBarcode=&selectCollectionId=&selectOrgId=-1&selectHoldKeepSiteId=62&selectLendKeepSiteId=0&selectReturnKeepSiteId=0&selectReaderSystemId=-1&selectReaderGradeId=-1&selectReaderClassId=-1&selectStartLend=' + date + '&selectEndLend=' + date + '&selectStartReturn=&selectEndReturn=&lendfileListType=on&&sort=&numPerPage=100&action=actionView&id=&whichPage=1&displayFlag=true&selectyeartype=1'
    print('借書:')
    hist(url1, rs)

    url2 = 'http://hylib.ksml.edu.tw/cir/History.do?selectReaderName=&selectReaderCode=&selectReaderTypeId=&selectBarcode=&selectCollectionId=&selectOrgId=-1&selectHoldKeepSiteId=62&selectLendKeepSiteId=0&selectReturnKeepSiteId=0&selectReaderSystemId=-1&selectReaderGradeId=-1&selectReaderClassId=-1&selectStartLend=&selectEndLend=&selectStartReturn=' + date + '&selectEndReturn=' + date + '&sort=&numPerPage=100&action=actionView&id=&whichPage=1&displayFlag=true&selectyeartype=1'
    print('===============')
    print('還書:')
    hist(url2, rs)
    print('=========================')


rs = login()

date = time.strftime('%Y-%m-%d', time.localtime())
print('=========================')
print('今日(', date, '):')
findlending(date, rs)


while True:
    date = input('日期(20XX-XX-XX):')
    findlending(date, rs)



