# Math functions X squared
# first need to type pipenv install matplotlib
# then type pipenv shellre
import matplotlib.pyplot as plot

f_output = []

def f(x):
    return x**2

xs = list(range(-100,101))
ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs,ys)
plot.show()