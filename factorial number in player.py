num = int(input(""))
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
print("The factorial ",num,"is",factorial)
