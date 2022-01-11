import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from math import log

c=1
w=0.1
R=1
T=2*np.pi/w
t=np.linspace(0,2*np.pi/w,50)
s=c*(c*R*w*np.cos(t*w)- np.sin(t*w))/(1+(c ** 2)*(R ** 2)*(w ** 2))
sd = c*(-w*np.cos(t*w)-c*R*(w ** 2)*np.sin(t*w))/(1+(c ** 2)*(R ** 2)*(w ** 2))
plt.plot(t,s,'bo')
plt.plot(t,sd,'ro')
plt.show()

amps = []
amps1 = []
ampsd = []
ampsd1 = []
w = 0.1
v = 0
c = 0.7147
R = 1
n = 100
while w < 10.1:
    st = []
    sdt = []
    v = 0
    while v < 101:
        t = (2 * np.pi) / w / n * v
        s = c * (c * R * w * np.cos(t * w) - np.sin(t * w)) / (1 + (c ** 2) * (R ** 2) * (w ** 2))
        st.append(s)
        sd = c * (-w * np.cos(t * w) - c * R * (w ** 2) * np.sin(t * w)) / (1 + (c ** 2) * (R ** 2) * (w ** 2))
        sdt.append(sd)
        v = v + 1

    logarytm = math.log10(w)

    amps.append(logarytm)
    amps1.append(max(st))
    ampsd.append(logarytm)
    ampsd1.append(max(sdt))
    w = w + 0.1
print(max(amps1))
print(min(amps))
print(max(ampsd))
print(max(ampsd1))
plt.plot(amps, amps1, 'bo', ampsd, ampsd1, 'ro')

plt.show()
