# Basic objects

class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1

    def print_contact_info(self):
        print("{0}'s email: {1}, {0}'s phone number: {2}".format(self.name, self.email, self.phone))

    def add_friend(self, other_person):
        self.friends.append(other_person.name)

    def num_friends(self):
        return len(self.friends)

    def __str__(self):
        return "Person: {}, {}, {}, greet count: {}, number of friends: {}".format(self.name, self.email, self.phone, self.greeting_count, self.num_friends())

# instantiate objects with names 'Sonny' and 'Jordan'

sonny = Person('Sonny', 'sonny@hotmail.com', '483-483-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
dee_ann = Person('Dee Ann', 'deeann@gmail.com', '486-333-0955')

# have sonny greet jordan & jordan greet sonny using greet method

sonny.greet(jordan)
jordan.greet(sonny)

# print out contact info for Sonny & Jordan

print("{}'s email is {} and phone is {}".format(sonny.name, sonny.email, sonny.phone))
print("{}'s email is {} and phone is {}".format(jordan.name, jordan.email, jordan.phone))

# create Vehicle class with 3 attributes

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# add a print_info method        

    def print_info(self):
        print("{} {} {}".format(self.year, self.make, self.model))

# instantiate a member of Vehicle class

car = Vehicle('Nissan', 'Leaf', 2015)

# print car info using print_info method

car.print_info()

# use added print_contact_info method

sonny.print_contact_info()

# add a friends attribute to Person class
# add a method add_friend to append a friend
# add a method num_friends to determine how many friends someone has
# add a greeting_count attribute
# add __str__ method to better "represent" the Person object

sonny.add_friend(jordan)
jordan.add_friend(sonny)

sonny.greet(jordan)
sonny.greet(jordan)
jordan.greet(sonny)

print("{} had {} friends".format(sonny.name, sonny.num_friends()))
print("{} has {} friends".format(jordan.name, jordan.num_friends()))
print("{} has greeted {} times".format(sonny.name, sonny.greeting_count))
print("{} has greeted {} times".format(jordan.name, jordan.greeting_count))
print("What does print self/Person look like? {}".format(sonny))
print("stringified jordan is {}".format(str(jordan)))
