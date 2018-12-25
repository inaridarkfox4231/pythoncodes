# 陰関数のグラフを描く
import matplotlib.pyplot as plt
import numpy as np

# abs(abs(s) + abs(t) - 4) + 2 * abs(abs(s) - abs(t)) = 4 のグラフ。
# ただし、s = 1 - abs(x), t = 1 - abs(y).

# contourを使う。

fig = plt.figure()

xrange = np.linspace(-6, 6, 150)
yrange = np.linspace(-6, 6, 150)
x, y = np.meshgrid(xrange, yrange)
# ここのxとyは、描画に使う点のx座標のセットとy座標のセット
# からなるリストのリストになってるの。

plt.xticks([-6, -4, -2, 0, 2, 4, 6])
plt.yticks([-6, -4, -2, 0, 2, 4, 6])

plt.xlim(-6.6, 6.6)
plt.ylim(-6.6, 6.6)

plt.gca().set_aspect('equal') # x軸とy軸で幅を揃える感じ

s = 1 - abs(x)
t = 1 - abs(y)
z = abs(abs(s) + abs(t) - 4) + 2 * abs(abs(s) - abs(t))

plt.title("||1-|x||+|1-|y||-4| + 2||1-|x||-|1-|y||| = 4")
# 万華鏡のような形になる
plt.contour(x, y, z, [4])
plt.show()
