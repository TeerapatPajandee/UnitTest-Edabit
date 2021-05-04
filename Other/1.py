text = "the United State of America"
textdict = text.split(' ')
print(textdict)
result = ""
for i in textdict:
    print(i)
    if (i[0].isupper()):
        result += i[0]

print(result)