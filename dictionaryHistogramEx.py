# histogram dictionary exercise

# create a function that takes string as input & returns histogram of letters

from collections import Counter

SENTENCE = """Only the fool would take trouble to verify that his sentence was composed of ten a's, three b's, four c's, 
four d's, forty-six e's, sixteen f's, four g's, thirteen h's, fifteen i's, two k's, nine l's, four m's, twenty-five n's, 
twenty-four o's, five p's, sixteen r's, forty-one s's, thirty-seven t's, ten u's, eight v's, eight w's, four x's, 
eleven y's, twenty-seven commas, twenty-three apostrophes, seven hyphens and, last but not least, a single !"""

# for char in SENTENCE.lower().replace('\n', ''):
#    print(char)

# generate histogram
letters_hist = Counter(SENTENCE.lower().replace('\n', ''))
# print(letters_hist)

counts = letters_hist.values()

# letters = letters_hist.keys()
# print(counts)
# print(letters)

Histogram_dictionary = {}
# Histogram_dictionary['a'] = '3'
print(Histogram_dictionary)
print()

letters = list(letters_hist.keys())
letters.sort()
for letter in letters:
    print("{}: {}".format(letter, letters_hist[letter]))
    Histogram_dictionary[str(letter)] = letters_hist[str(letter)]

print(Histogram_dictionary)   

#for key in letters_hist
#    print(key, letters_hist[key])


# histogram_dictionary = {}


#>>> d = {'key':'value'}
#>>> print(d)
#{'key': 'value'}
#>>> d['mynewkey'] = 'mynewvalue'
#>>> print(d)

"""
for i in range(0, len(counts)):
    histogram_dictionary[letters(i)] = counts(i)
    print("{}:{}".format(letters(i), counts(i)))

print(histogram_dictionary)
"""

#def f(x):
#    from collections import Counter
#    SENTENCE = x
#    letters_hist = Counter(SENTENCE.lower().replace('\n', ''))
#    counts = letters-hist.values()
#    letters = letters_hist.keys()
#    histogramSentence = 