# String Exercises
myString = 'Howdy Doody'
lowerString = myString.lower
upperString = myString.upper

print("Original string is " + myString)
print("Uppercase string is " + myString.upper())
print("Lowercase string is " + myString.lower())
print("Capitalized string is " + myString.capitalize())

# print reverse string
reverseString = ''

for index in range(len(myString) - 1, -1, -1):
    reverseString += myString[index]

print("The reverse string is: " + reverseString)


# Leetspeak conversion/translation problem
LeetString = 'AAEEETSOIG'

LeetConverted = ''

for index in range(0, len(LeetString)):
    if LeetString[index] == 'A':
        LeetConverted += '4'
    elif LeetString[index] == 'E':
        LeetConverted += '3'
    elif LeetString[index] == 'G':
        LeetConverted += '6'
    elif LeetString[index] == 'I':
        LeetConverted += '1'
    elif LeetString[index] == 'O':
        LeetConverted += '0'
    elif LeetString[index] == 'S':
        LeetConverted += '5'
    elif LeetString[index] == 'T':
        LeetConverted += '7'
    else:
        Print("I don't understand this LEET input!")

print("Original LEET string is :" + LeetString)
print("Converted LEET is: " + LeetConverted)  

# Long-long Vowels exercise 
# e.g., in any string, 'ii' => 'iiiii'   'oo' => 'ooooo'  

inputString = 'goofiijkiuux'
longLongString = ''
for index in range(0, len(inputString)):
    if index == len(inputString) - 1:
        longLongString += inputString[index]
    elif inputString[index] == 'a' and inputString[index + 1] == 'a':
        longLongString += 4 * inputString[index] 
    elif inputString[index] == 'e' and inputString[index + 1] == 'e':
        longLongString += 4 * inputString[index] 
    elif inputString[index] == 'i' and inputString[index + 1] == 'i':
        longLongString += 4 * inputString[index] 
    elif inputString[index] == 'o' and inputString[index + 1] == 'o':
        longLongString += 4 * inputString[index]         
    elif inputString[index] == 'u' and inputString[index + 1] == 'u':
        longLongString += 4 * inputString[index]         
    else:
        longLongString += inputString[index]

print("Original string is: " + inputString)
print("Converted long-long vowel string is: " + longLongString)