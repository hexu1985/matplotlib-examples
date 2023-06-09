import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

fig,ax = plt.subplots(2,2)

x = np.linspace(0,2*np.pi,500)
y1= 2*np.cos(x)
y2 = 2*np.sin(x)

# subplot(221)
ax[0,0].plot(y1,y2,color="cornflowerblue",lw=2)

ax[0,0].set_xlim(-3,3)
ax[0,0].set_ylim(-3,3)

# subplot(222)
rectangle = ax[0,1].patch
rectangle.set_facecolor("gold")

ax[0,1].plot(y1,y2,color="cornflowerblue",lw=2)

ax[0,1].set_xlim(-3,3)
ax[0,1].set_ylim(-3,3)

ax[0,1].set_aspect("equal","box")

# subplot(223)
rectangle = ax[1,0].patch
rectangle.set_facecolor("palegreen")

ax[1,0].plot(y1,y2,color="cornflowerblue",lw=2)

ax[1,0].axis("equal")

# subplot(224)
rectangle = ax[1,1].patch
rectangle.set_facecolor("lightskyblue")

ax[1,1].plot(y1,y2,color="cornflowerblue",lw=2)

ax[1,1].axis([-3,3,-3,3])
ax[1,1].set_yticks(np.arange(-3,4,1))

ax[1,1].axis("equal")

plt.subplots_adjust(left=0.1)

plt.show()
