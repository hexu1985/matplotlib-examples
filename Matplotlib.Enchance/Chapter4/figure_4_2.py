import matplotlib.patches as patches
import matplotlib.pyplot as plt

fig = plt.figure(1, figsize=(8,9), dpi=72)
fontsize = 0.4*fig.dpi

# subplot(111)
ax = fig.add_subplot(1,1,1,frameon=False)

arrowStyles = patches.ArrowStyle.get_styles()
arrowStyleNames = list(arrowStyles.keys())
arrowStyleNames.sort()

ax.set_xlim(0,len(arrowStyleNames)+2.5)
ax.set_ylim(-2,len(arrowStyleNames))

for i,name in enumerate(arrowStyleNames):
    p = patches.Circle((float(len(arrowStyleNames))+1.2-i,float(len(arrowStyleNames))-2.8-i),
                       0.2,color="steelblue",alpha=1.0)
    ax.add_patch(p)
    ax.annotate(name,
                (float(len(arrowStyleNames))+1.2-i,float(len(arrowStyleNames))-2.8-i),
                (float(len(arrowStyleNames))-1-i,float(len(arrowStyleNames))-3-i),
                xycoords="data",
                ha="center",
                size=fontsize,
                arrowprops=dict(arrowstyle=name,
                                facecolor="k",
                                edgecolor="k",
                                patchB=p,
                                shrinkA=5,
                                shrinkB=5,
                                connectionstyle="arc3"),
                bbox=dict(boxstyle="round",fc="w",ec="k"))

ax.xaxis.set_visible(False)  # ax.set_xticks([])
ax.yaxis.set_visible(False)  # ax.set_yticks([])

plt.show()
