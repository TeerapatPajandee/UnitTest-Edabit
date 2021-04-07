def binary_to_decimal(binary):
    sum = 0
    position = 7
    for each in binary:
        if each == 1:
            sum += (2**position)
            position -= 1
        else:
            position -= 1
            continue
    print(binary ," -> ",sum)
    return sum


# binary_to_decimal([1, 1, 1, 1, 1, 1, 1, 1])
# a = 0b11111111
# print(a)