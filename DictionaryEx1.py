#Phonebook dictionaryt exercises

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

#print Elizabeth's phone #

print(phonebook_dict['Alice'])

# add entry for Kareem

phonebook_dict['Kareem'] = '938-489-1234'
print(phonebook_dict)

# delete Alice's phone entry

del phonebook_dict['Alice']
print(phonebook_dict)

# change Bob's phone # to '968-345-2345'

phonebook_dict['Bob'] = '968-345-2345'
print(phonebook_dict)

# print all the phone #'s

for value in phonebook_dict.values():
    print(value)

# print all the keys

for key in phonebook_dict.keys():
    print(key)

# print key:value pairs formatted

for key, value in phonebook_dict.items():
    print(key, ':', value)