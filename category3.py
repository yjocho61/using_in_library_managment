import csv



def is_number(str):
  try:
    if str=='NaN':
      return False
    float(str)
    return True
  except ValueError:
    return False


def classifying(n):
  fin = open('nmsbooklist.csv', 'r')
  m = len(n)
  d = dict()
  d2 = dict()
  a = []
  for element in fin:
      t = element.split(',')
      if t[2][1] != 'J':
          u = t[2].split(' ')
          for member in u:
              if len(member) >= 3 and is_number(member):
                  if member[:m] == n:
                    d[member] = d.get(member, 0) + 1
                    k = u.index(member)
                    try:
                      j = (member, u[k + 1][:1])
                      d2[j] = d2.get(j, 0) + 1
                    except IndexError:
                      print(u)
                  break
  for key in d2:
    a.append(key)
  a.sort()
  for element in a:
    print(element, ':', d2[element])
  return d



while True:
  c = 0
  s = []
  n = input('number = ')
  d = classifying(n)
  print('===========================')
  for key in d:
    s.append(key)
  s.sort()
  for element in s:
    print(element, ':', d[element])
    c += d[element]
    if c >= 50:
      print('=======','remainder:', c - 50,'=======')
      c = 0
  print('==============================================================')
