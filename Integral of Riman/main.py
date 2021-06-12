import numpy
import matplotlib.pyplot as plt
import random


def f(x):
    return numpy.power(x, 3)


print("Enter the num:")
n = int(input())
step = 2 / n
fx = numpy.arange(0, 2, 0.00001)
fy = f(fx)
for mode in range(4):
    x = []
    y = []
    fig, ax = plt.subplots()
    title = ', число точек: ' + str(n) + "\nCумма: "
    if mode == 0:
        xi = float(0)
        title = 'Левое оснащение' + title
    if mode == 1:
        xi = float(step / 2)
        title = 'Среднее оснащение' + title
    if mode == 2:
        xi = float(step)
        title = 'Правое оснащение' + title
    if mode == 3:
        xi = float(random.randint(0, 2 * 10000) / (n * 10000))
        title = 'Рандомное оснащение' + title
    res = float(0)
    value = float(0)
    for i in range(n):
        value = numpy.power(xi, 3)
        res = float(res + step * value)
        x.append(i * step)
        y.append(value)
        if mode != 3:
            xi = xi + step
        else:
            xi = xi + (step - xi % step) + float(random.randint(0, 2 * 10000) / (n * 10000))
    title += str(res)
    print(title)
    plt.plot(fx, fy, color='green')
    plt.bar(x, y, align='edge', edgecolor='blue', color='yellow', width=step)
    ax.set(xlabel='x', ylabel='f(x)', title=title)
    plt.savefig(str(mode) + "_ step-" + str(n) + ".png", dpi=500)
