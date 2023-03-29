# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

x = np.random.randn(1000)

plt.boxplot(x,vert=False,showfliers=False)

plt.xlabel("随机数值")
plt.yticks([1],["随机数生成器AlphaRM"],rotation=90)
plt.title("随机数生成器抗干扰能力的稳定性")

plt.grid(axis="x",ls=":",lw=1,color="gray",alpha=0.4)

plt.show()

