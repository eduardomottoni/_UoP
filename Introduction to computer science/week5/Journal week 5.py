prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter == "Q" or letter == "O":
            letter += 'u'
    #Aditional aproach based on textbook slice (chapter 8.4)
    if letter == prefixes[5] or letter == prefixes[7]:
       letter += 'u'
    #Validated
    print(letter + suffix)

string = 'Computer Science'
print(string[:16])
