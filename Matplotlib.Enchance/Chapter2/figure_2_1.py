import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

fig,ax = plt.subplots(2,2)

# subplot(221)
circle = Circle((2,2),radius=2,facecolor="white",edgecolor="cornflowerblue")
ax[0,0].add_patch(circle)

ax[0,0].set_xlim(-1,5)
ax[0,0].set_ylim(-1,5)

# subplot(222)
rectangle = ax[0,1].patch
rectangle.set_facecolor("gold")

circle = Circle((2,2),radius=2,facecolor="white",edgecolor="cornflowerblue")
ax[0,1].add_patch(circle)

ax[0,1].set_xlim(-1,5)
ax[0,1].set_ylim(-1,5)

ax[0,1].set_aspect("equal","box")

# subplot(223)
rectangle = ax[1,0].patch
rectangle.set_facecolor("palegreen")

circle = Circle((2,2),radius=2,facecolor="white",edgecolor="cornflowerblue")
ax[1,0].add_patch(circle)

ax[1,0].axis("equal")

# subplot(224)
rectangle = ax[1,1].patch
rectangle.set_facecolor("lightskyblue")

circle = Circle((2,2),radius=2,facecolor="white",edgecolor="cornflowerblue")
ax[1,1].add_patch(circle)

ax[1,1].axis([-1,5,-1,5])
ax[1,1].set_yticks(np.arange(-1,6,1))

ax[1,1].axis("equal")

plt.subplots_adjust(left=0.1)

plt.show()
