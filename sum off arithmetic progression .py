def sumOfAP(a,d,n) :
    sum = 0
    i = 0
    while i < n :
        sum = sum + a
        a = a + d
        i = i + 1
    return sum
n = 3
d = 1
a = 1
print (sumOfAP(a,d,n))
 
