# Pin = input("Enter Pin 4 or 6 Characters :")

def valid(txt):
    print(txt)

    if txt.isnumeric() == True:
        sum = 0
        for x in txt:
            sum += 1
        # print(sum)
        if sum == 4 or sum == 6:
            return True
        else:
            return False
    else:
        return False


### Test ###
# if valid(Pin):
#     print("OK!")
# else:
#     print("Invalid")
