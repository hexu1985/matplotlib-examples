import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(1,figsize=(8,8),dpi=80,facecolor="w")
fontsize = 1.5*0.1*fig.dpi
font_style = {"family":"sans-serif","fontsize":fontsize,"weight":"black"}

# xaxis separate tick and ticklabel
ax0_0 = fig.add_subplot(2,2,1,facecolor="yellowgreen",alpha=.1)
ax0_0.xaxis.set_ticks_position("top")
ax0_0.xaxis.set_label_position("top")
ax0_0.set_xlabel("separate tick and ticklabel",**font_style)

# xaxis universal tick and ticklabel
ax0_1 = fig.add_subplot(2,2,2,facecolor="yellowgreen",alpha=.1)
ax0_1.xaxis.tick_top()
ax0_1.xaxis.set_label_position("top")
ax0_1.xaxis.set_label_text("universal tick and ticklabel",**font_style)

# yaxis separate tick and ticklabel
ax1_0 = fig.add_subplot(2,2,3,facecolor="yellowgreen",alpha=.1)
ax1_0.yaxis.set_ticks_position("right")
ax1_0.yaxis.set_label_position("right")
ax1_0.set_ylabel("separate tick and ticklabel",**font_style)

# yaxis universal tick and ticklabel
ax1_1 = fig.add_subplot(2,2,4,facecolor="yellowgreen",alpha=.1)
ax1_1.yaxis.tick_right()
ax1_1.yaxis.set_label_position("right")
ax1_1.yaxis.set_label_text("universal tick and ticklabel",**font_style)

fig.subplots_adjust(wspace=0.3)

plt.show()
