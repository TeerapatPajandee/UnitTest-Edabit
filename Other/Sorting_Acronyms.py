loop = int(input("Enter number : "))

text = []
show = []
tmp2 = ''

def findUpper(text):
  tmp = ''
  for x in text:
    if(x.isupper()):
      tmp += x
  return(tmp)

def cutString(text):
  tmp = ''
  for x in text:
    for c in x:
      tmp += c
      break
  return(tmp)

for x in range(loop):
  tmp = input('Enter sentences ' + str(x+1) + ' : ').split(' ')
  tmp = cutString(tmp)
  text.append(tmp2.join(tmp))

for x in text:
  show.append(findUpper(x))

show.sort(key=lambda item: (-len(item), item))
print(show)