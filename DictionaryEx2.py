# Dictionary exercise2

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# print Ramit's e-mail address

print("Ramit's email address: " + ramit['email'])

# write a python expression that gets the first of Ramit's interests.

print("Ramit's first interest is: " + ramit['interests'] [0])

# print Jasmine's email address -- 2 ways, 1st direct, 2nd by checking for 'Jasmine'

print("Jasmine's email address is: " + ramit['friends'][0]['email'])
ramitsFriends = ramit['friends']
print(ramitsFriends)

for index in range(0, len(ramitsFriends)):
    if ramitsFriends[index]['name'] == 'Jasmine':
        print("Jasmine's email is: " + ramitsFriends[index]['email'])




# print 2nd of Jan's of Jan's two interestes

print("Jan's 2nd interest is: " + ramit['friends'][1]['interests'][1])

# histogram function




