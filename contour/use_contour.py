# 等高線の使い方、まとめ（陰関数のグラフ）
import matplotlib.pyplot as plt
import numpy as np

# x^2 + y^2 = 2のグラフを描こう。

# contourを使う。

fig = plt.figure()

xrange = np.linspace(-3, 3, 100)
yrange = np.linspace(-3, 3, 100)
x, y = np.meshgrid(xrange, yrange)
# ここのxとyは、描画に使う点のx座標のセットとy座標のセット
# からなるリストのリストになってるの。

plt.xticks([-3, -2, -1, 0, 1, 2, 3])
plt.yticks([-3, -2, -1, 0, 1, 2, 3])

plt.xlim(-3.3, 3.3)
plt.ylim(-3.3, 3.3)

plt.gca().set_aspect('equal') # x軸とy軸で幅を揃える感じ

z = x ** 2 + y ** 2 - 2
# それを元に、例えばこの場合[0]なのでz=0の等高線が描かれる。
# [-1, 0, 1]とすればzが-1, 0, 1の線がすべて描かれる感じですかね。
plt.contour(x, y, z, [0])
plt.show()
