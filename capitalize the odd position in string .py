word = raw_input("")
word = list(word)
for i, ele in enumerate(word):
   if i % 2 !=0:
       word[i] = ele.upper()

print("".join(word))
