num=int(input(""))
sum=0
while num > 0:
    a = num % 10
    sum = sum + (a ** 2)
    num //= 10
print(sum)
