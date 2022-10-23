from pylab import * 
print('Template Fungsi: a x^3 + b x^2 + c x + d')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d = int(input('d: '))
def f(x, a, b, c, d):
    return a*x**3 + b*x**2 + c * x + d
x = linspace(-1000,1000,10)
xa = float(input("X1: "))
xb = float(input("X2: "))
xc = (xa+xb)/2
i = 1
while abs(f(xc, a, b, c, d))>0.001:
    print("Iterasi Ke -",i)
    print("X1 =",xa)
    print("X2 =",xb)
    print("X3 =",xc)
    print(" ")
    if f(xa, a, b, c, d)*f(xc, a, b, c, d)>0:
        xa = xc
    else:
        xb = xc
    xc = (xa + xb)/2
    i+=1
print("Jadi X = ",xc)
plot(x,f(x, a, b, c, d))
xlabel('x values')
ylabel('y values')
title('Graph')
grid(True)
show()