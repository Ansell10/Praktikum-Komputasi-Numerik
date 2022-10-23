from pylab import * 
def f(x):
    y = x**3 + x**2 - 3*x + 1
    return y
x = linspace(-1000,1000,10)
xa = float(input("X1: "))
xb = float(input("X2: "))
xc = (xa+xb)/2
i = 1
while abs(f(xc))>0.001:
    print("Iterasi Ke -",i)
    print("X1 =",xa)
    print("X2 =",xb)
    print("X3 =",xc)
    print(" ")
    if f(xa)*f(xc)>0:
        xa = xc
    else:
        xb = xc
    xc = (xa + xb)/2
    i+=1
print("Jadi X = ",xc)
plot(x,f(x))
xlabel('x values')
ylabel('y values')
title('Graph')
grid(True)
show()