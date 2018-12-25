# 陰関数のグラフを描く
import matplotlib.pyplot as plt
import numpy as np

# abs(abs(s) + abs(t) - 4) + 2 * abs(abs(s) - abs(t)) = 4 のグラフ。
# ただし、s = 1 - abs(x), t = 1 - abs(y).

# contourを使う。

fig = plt.figure()

xrange = np.linspace(-1, 5, 150)
yrange = np.linspace(-3, 3, 150)
x, y = np.meshgrid(xrange, yrange)
# ここのxとyは、描画に使う点のx座標のセットとy座標のセット
# からなるリストのリストになってるの。

plt.xticks([-1, 0, 1, 2, 3, 4, 5])
plt.yticks([-3, -2, -1, 0, 1, 2, 3])

plt.xlim(-1.2, 5.2)
plt.ylim(-3.2, 3.2)

plt.gca().set_aspect('equal') # x軸とy軸で幅を揃える感じ

z = abs((x - 1) ** 2 + y ** 2 - 4) - 2 * x

plt.title(r'$|{(x - 1)}^2 + y^2 - 4| - 2x = 0$')
# 三日月のような形になる。
plt.contour(x, y, z, [0])
plt.show()
