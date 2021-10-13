def CountWordsFromFile():
    file = input("Enter the File Name: ")
    fileName = open(file,"r")
    wordCount = 0
    for i in fileName:
        word = i.split()
        wordCount = wordCount + len(word)
    print(wordCount)
CountWordsFromFile()    