inputWord = 'banana'
#input("Input a word: ")
# inputWord[2] = 'n'
letterDictionary = {}

for character in inputWord:
    letterDictionary[character] = inputWord.count(character)

print(letterDictionary)

inputPhrase = 'I wonder what is the best is'
WordDictionary = {}

PhraseList = inputPhrase.split()

for word in PhraseList:
    WordDictionary[word] = PhraseList.count(word)

print(WordDictionary)

