# histogram dictionary exercise

# create a function that takes string as input & returns histogram

from collections import Counter

SENTENCE = """Only the fool would take trouble to verify that his sentence was composed of ten a's, three b's, four c's, 
four d's, forty-six e's, sixteen f's, four g's, thirteen h's, fifteen i's, two k's, nine l's, four m's, twenty-five n's, 
twenty-four o's, five p's, sixteen r's, forty-one s's, thirty-seven t's, ten u's, eight v's, eight w's, four x's, 
eleven y's, twenty-seven commas, twenty-three apostrophes, seven hyphens and, last but not least, a single !"""

# generate histogram
letters_hist = Counter(SENTENCE.lower().replace('\n', ''))
counts = letters_hist.values()
letters = letters_hist.keys()
print(counts)
print(letters)

"""
def f(x):
    from collections import Counter
    SENTENCE = x
    letters_hist = Counter(SENTENCE.lower().replace('\n', ''))
    counts = letters-hist.values()
    letters = letters_hist.keys()
    histogramSentence = 

"""