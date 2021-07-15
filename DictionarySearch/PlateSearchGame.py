#program will be able to search the 3 letters of the licence plate and do the word game search to see if there are any words

#currently only gonna use a english dictionary

#   UPGRADES:
#       can add place names as well, once I have the normal dictionary working
#       can concatenate and edit the dictionary .csv files to help the search
#       can make the code search more efficient

import pandas as pd

#for fixing the csv
#   # A, 0
#   old = df['Word'][0][0]
#   for i in range(len(df['Word'])):
#       if (df['Word'][i][0].upper() != 'b'.upper()):
#           old = df['Word'][i][0]
#           print(str(old) + " " + str(i))


#this works, but only with the letter B right now


letters = input("Enter the 3 letters to be searched: ")

df = pd.read_csv(letters[0].upper() + 'word.csv')

working_words = []

for i in range(len(df['Word'])):

    if ((df['Word'][i][len(df['Word'][i])-2]) == letters[2].lower()):   #this is working
        for j in range(1, len(df['Word'][i])-2):
            if ((df['Word'][i][j]) == letters[1].lower()):
                if(df['Word'][i][0].lower() == letters[0].lower()): #this is just to double check since there can be wrong words in the .csv files
                    working_words.append(df['Word'][i])
                    break
                
if 0 == len(working_words):
    print("There are no word that has the combination!")
    exit(1)
temp = working_words[0]
word_count = 0
for i in range(len(working_words)):
    if (working_words[i] == temp):
        temp = working_words[i]
        continue
    print(working_words[i])
    temp = working_words[i]
    word_count += 1

print("total possible words: " + str(word_count) + " using the letters " + letters.upper())
