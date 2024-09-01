num = int(input("Enter your number: "))

flag = 0

for i in range(2, num):
    if num % i == 0:
        flag = 1
        break

if flag == 1:
    print("Not prime")
else:
    print("Prime number")
