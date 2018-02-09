# Plot Degrees F vs. Degrees C
# first need to type pipenv install matplotlib
# then type pipenv shell
import matplotlib.pyplot as plot

# x Degrees Celcius, f(x) is Degrees Fahrenheirt

def f(x):
    return (x * 1.8) + 32

xs = list(range(-100,101))
ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs,ys)
plot.show()
