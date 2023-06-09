import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2*np.pi,500)
y = 1.85*np.sin(x)

fig,ax = plt.subplots(3,1)

# subplot(3,1,1)
ax[0].plot(x,y,lw=3,color="dodgerblue")

ax[0].set_ylim(-2,2)

ax[0].set_axis_bgcolor("lemonchiffon")

# subplot(3,1,2)
ax[1].plot(x,y,lw=3,color="dodgerblue")

ax[1].spines["right"].set_visible(False)
ax[1].spines["top"].set_visible(False)

ax[1].xaxis.set_ticks_position("bottom")
ax[1].yaxis.set_ticks_position("left")

ax[1].set_ylim(-3,3)

ax[1].set_axis_bgcolor("lemonchiffon")

# subplot(3,1,3)
ax[2].plot(x,y,lw=3,color="dodgerblue")

ax[2].spines["right"].set_color("none")
ax[2].spines["top"].set_color("none")

ax[2].yaxis.tick_left()
ax[2].xaxis.tick_bottom()

ax[2].spines["left"].set_bounds(-1,1)
ax[2].spines["bottom"].set_bounds(0,2*np.pi)

ax[2].set_ylim(-2,2)

ax[2].set_axis_bgcolor("lemonchiffon")

fig.subplots_adjust(hspace=0.3)

plt.show()
