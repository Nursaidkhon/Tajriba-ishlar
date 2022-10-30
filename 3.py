import math
x = float(input())
y = float(input())
z = float(input())
gamma =5 * math.atan(x)-(1/4)*math.acos(x)*(x+3*math.fabs(x-y)+x**2)/(math.fabs(x-y)*z+x**2)
print(gamma)