# Math functions
# first need to type pipenv install matplotlib
# then type pipenv shellre
import matplotlib.pyplot as plot

f_output = []

def f(x):
    return x + 1

xs = list(range(-3,4))
ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs,ys)
plot.show()

