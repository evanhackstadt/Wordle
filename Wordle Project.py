### Evan Hackstadt
### Wordle Project for coding practice

f = open('5_char_words.txt')
lines = f.readlines()
f.close()

def stripLast(str):
    outstr = ""
    for i in range(0, len(str)-1):
        outstr += str[i]
    return outstr

def checkWord(word, answer):
    print(word)
    if word == answer:
        giveFeedback(word, answer)
        return True
    else:
        giveFeedback(word, answer)
        return False
    
def giveFeedback(word, answer):
    compare = ""
    for i in range(5):
        if word[i] == answer[i]:
            compare += "G"
        else:
            present = False
            for letter in answer:
                if word[i] == letter:
                    present = True
            if present == True:
                compare += "Y"
            else:
                compare += "X"
    print(compare)



## Main Code

import random

dictionary=[]
for word in lines:
    dictionary.append(stripLast(word))

answer = dictionary[random.randrange(0, len(dictionary))]
print("Wordle: Enter a 5-letter word")
guess = input()

while checkWord(guess, answer) == False:
    guess = input()

# IMPROVEMENTS:
    # >5 letter word protection
    # not-in-word-list protection
    # optional hard mode (if letters already found wrong)
    # better visual feedback/instructions