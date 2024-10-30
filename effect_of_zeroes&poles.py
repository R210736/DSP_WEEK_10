import numpy as np
from matplotlib import pyplot as plt
z=input("Zero location in z plane")
zero=complex(z)
r=input("zero location from origin")
w0=input("frequency of zero")
z1=r* np.exp((np.j)*w0)
h=1/(1-z1*np.exp(np.j*w0))
plt.plot(h)
plt.plot(np.angle(h))