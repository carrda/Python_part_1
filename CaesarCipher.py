# Caesar Cipher with 13 offset

cipherText = 'lbh zhfg hayrnea jung lbh unir yrnearq'
convertedText = ''
for index in range(0, len(cipherText)):
    if ord(cipherText[index]) == 32: #check if space character
        convertedText += cipherText[index]
    else:
        #convert ord values of lower case letters to 1 - 26
        loweredOrd = ord(cipherText[index]) - 96
        convertedOrd = (loweredOrd + 13) % 26
        convertedText += chr(convertedOrd + 96)

print("Ciphertext is :" + cipherText)
print("Plaintext is :" + convertedText)

        
