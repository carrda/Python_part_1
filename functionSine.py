# Math Sine plot
# first need to type pipenv install matplotlib
# then type pipenv shellre
import matplotlib.pyplot as plot
import math



def f(x):
    return math.sin(x)

xs = list(range(-5,6))
ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs,ys)
plot.show()