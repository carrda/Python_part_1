# Math functions
# first need to type pipenv install matplotlib
# then type pipenv shellre
import matplotlib.pyplot as plot

f_output = []

def f(x):
    if (x % 2) == 1:
        return 1
    else:
        return -1

xs = list(range(-5,6))
ys = []

for x in xs:
    ys.append(f(x))

plot.bar(xs,ys)
plot.show()