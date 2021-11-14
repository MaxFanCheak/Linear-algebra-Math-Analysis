# This Python file uses the following encoding: utf-8
import math
import numpy as np
import matplotlib.pyplot as plt


def gradient(a, x, y):
    idgdx = 2 * (x ** 2) * y / ((x ** 2) + (y ** 2)) + y * math.log((x ** 2) + y ** 2)
    jdgdy = 2 * x * (y ** 2) / ((x ** 2) + (y ** 2)) + x * math.log((x ** 2) + y ** 2)
    mas = [-idgdx * a, -a * jdgdy]
    return mas

def myFunc(x,y):
    return x*y*math.log(x**2 + y**2)

def eLoc(e, x1, y1, x2, y2):
    return (x1 < x2 and x1 > (x2 - e) or x1 > x2 and x1 < (x2 + e)) and (y1 < y2 and y1 > (y2 - e) or y1 > y2 and y1 < y2 + e)

min1 = [- math.sqrt(1/(2*math.e)), - math.sqrt(1/(2*math.e))]
max2 = [- math.sqrt(1/(2*math.e)), math.sqrt(1/(2*math.e))]
max3 = [math.sqrt(1/(2*math.e)), - math.sqrt(1/(2*math.e))]
min4 = [math.sqrt(1/(2*math.e)), math.sqrt(1/(2*math.e))]
print(min4[0])
print(min4[1])
cur = [math.log(2.0), math.log(2.0)]
a = 0.9
ax = [cur[0]]
ay = [cur[1]]
eps = 1.0e-10
iter = -1
while(True):
    iter = iter + 1
    if(eLoc(eps, cur[0], cur[1], min4[0], min4[1])):
        break
    newVals = gradient(a, cur[0], cur[1])
    if (myFunc(cur[0] + newVals[0], cur[1] + newVals[1]) > myFunc(cur[0], cur[1])):
        a = a/2
        iter = iter - 1
    else:
        cur[0] = cur[0] + newVals[0]
        cur[1] = cur[1] + newVals[1]
        plt.scatter([cur[0]], [cur[1]])
        #ax.append(cur[0])
        #ay.append(cur[1])
print("Критерий останова:", eps)
print("Кол-во итераций:", iter)
print("Полученная точка:", cur[0], " ", cur[1])
print("Значение функции:", myFunc(cur[0], cur[1]))
print("Разница координат:")
print("По x: ", math.fabs(cur[0]-min4[0]))
print("По y: ", math.fabs(cur[1]-min4[1]))
print("Разница в значениях функции:", math.fabs(myFunc(cur[0], cur[1]) - myFunc(min4[0], min4[1])))
plt.plot(ax, ay, 'ro')
#plt.axis([0, 6, 0, 20])

#for i_x, i_y in zip(ax, ay):
#    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))

plt.show()

