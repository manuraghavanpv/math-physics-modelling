import matplotlib.pyplot as plt
import numpy as np
#Sun's Orbit
th = np.linspace(0,2*(np.pi),360)
a = 0.00464
b = 0.00464
x = (a*np.sin(th))
y = (b*np.cos(th))
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Solar System(Roll. No. : 241)')
plt.plot(x,y)

#Mercury
a1=0.387
b1=0.037873
c1=0.079567
x1=(a1*np.sin(th))+c1
y1=(b1*np.cos(th))
plt.plot(x1,y1)

#Venus
a2=0.723
b2=0.722980
c2=0.00498
x2=(a2*np.sin(th))+c2
y2=(b2*np.cos(th))
plt.plot(x2,y2)

#Earth
a3=1
b3=0.99985
c3=0.0167
x3=(a3*np.sin(th))+c3
y3=(b3*np.cos(th))
plt.plot(x3,y3)

#Mars
a4=1.524
b4=1.51756
c4=0.4234
x4=(a4*np.sin(th))+c4
y4=(b4*np.cos(th))
plt.plot(x4,y4)

#Jupiter
a5=5.203
b5=5.1417
c5=0.25182
x5=(a5*np.sin(th))+c5
y5=(b5*np.cos(th))
plt.plot(x5,y5)

#Saturn
a6=9.537
b6=9.5230
c6=0.51690
x6=(a6*np.sin(th))+c6
y6=(b6*np.cos(th))
plt.plot(x6,y6)

#Uranus
a7=19.191
b7=19.16961
c7=0.90581
x7=(a7*np.sin(th))+c7
y7=(b7*np.cos(th))
plt.plot(x7,y7)

#Neptune
a8=30.069
b8=30.06899
c8=0.25860
x8=(a8*np.sin(th))+c8
y8=(b8*np.cos(th))
plt.plot(x8,y8)

#Pluto
a9=39.482
b9=38.24035
c9=9.82312
x9=(a9*np.sin(th))+c9
y9=(b9*np.cos(th))
plt.plot(x9,y9)

#Halley's Comet
a10=17.834
b10=4.5241
c10=17.2480
x10=(a10*np.sin(th))+c10
y10=(b10*np.cos(th))
plt.plot(x10,y10)

plt.show()