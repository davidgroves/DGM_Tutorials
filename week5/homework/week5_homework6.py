# Week5, Homework6

wordlist = open("words.txt", "r")

for word in wordlist:
    stripped_word = word.rstrip()
    if stripped_word == stripped_word[::-1]:
        print(stripped_word)

wordlist.close()