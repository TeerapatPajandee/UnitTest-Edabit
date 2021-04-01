# a() = input(print("Enter the binary number :"))
# print(a)


# a = 0b11111111
# print(a)

# x = list(map(int, input("Enter Binary : ").split()))
# print("List of Bianry: ", x)

# num = int(input("Enter Binary : "))
# sum = 0
# i = 0
# while num != 0:
#     rem = num % 10
#     sum += rem * pow(2, i)
#     num = int(num / 10)
#     i += 1
# print("Decimal Number : ", sum)
# sum = 0

A = list(input("Enter Binary : ").split())
print(A)
sum = 0
count = 0
for i in A:
    if A[count] != 0:
        rem = int(A[count]) % 10
        sum += rem * pow(2, i)
        A[count] = int(A[count] / 10)
        count += 1

print("Dec : ")
