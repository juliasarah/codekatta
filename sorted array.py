a=[]
n=int(input(""))
for i in range(1,n+1):
    b=input("")
    a.append(b)
a.sort(key=len)
print(a)
