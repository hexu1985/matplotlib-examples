import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import RadioButtons

x = np.linspace(0.0,2.0,1000)
y1 = 1.5*np.cos(2*np.pi*x)
y2 = 1.0*np.cos(2*np.pi*x)
y3 = 0.8*np.cos(2*np.pi*x)

fig,ax = plt.subplots(1,1)
line, = ax.plot(x,y1,color="red",lw=2)
plt.subplots_adjust(left=0.35)

axesbgcolor = "cornflowerblue"

# a set of radionbuttons about amplitude
ax1 = plt.axes([0.1,0.7,0.15,0.15],axisbg=axesbgcolor)
radio1 = RadioButtons(ax1,("1.5 A","1.0 A","0.8 A"))

def amplitudefunc(label):
    hzdict = {"1.5 A":y1,"1.0 A":y2,"0.8 A":y3}
    ydata = hzdict[label]
    line.set_ydata(ydata)
    plt.draw()

radio1.on_clicked(amplitudefunc)

# a set of radiobuttons about color
ax2 = plt.axes([0.1,0.4,0.15,0.15],axisbg=axesbgcolor)
radio2 = RadioButtons(ax2,("red","green","orange"))

def colorfunc(label):
    line.set_color(label)
    plt.draw()

radio2.on_clicked(colorfunc)

# a set of radionbuttons about linestyle
ax3 = plt.axes([0.1,0.1,0.15,0.15],axisbg=axesbgcolor)
radio3 = RadioButtons(ax3,("-","--","-.",":"))

def linestylefunc(label):
    line.set_linestyle(label)
    plt.draw()

radio3.on_clicked(linestylefunc)

plt.show()
