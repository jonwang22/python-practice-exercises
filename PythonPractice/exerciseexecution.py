txt = input()

#your code goes here
words = txt.split()

longword = ''
for word in words:
    if len(word) > len(longword):
        longword = word

print(longword)
