def rem_vowel(string):
    vowels = ('a', 'e', 'i', 'o', 'u') 
    for x in string.lower():
        if x in vowels:
            string = string.replace(x, "")
            revstring = string[::-1];

    print(revstring)

string = raw_input("")
rem_vowel(string)
