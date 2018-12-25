# reduce, map, filter等の使い方
# まず、reduceを使うにはimportする

from functools import reduce
# reduceは[[2, 3], [4, 5], [5, 6]]のようなのを[2, 3, 4, 5, 5, 6]にする
# または、[1, 3, 5]→[4, 5]→9みたいなこと。
a = [[1, 2], [3, 4], [5, 6]]
b = reduce(lambda x, y: x + y, a)
print(b) # [1, 2, 3, 4, 5, 6]
c = reduce(lambda x, y: x + y, b)
print(c) # 21
greet = ["How", " ", "are", " ", "you", "?"]
print(reduce(lambda x, y: x + y, greet)) # How are you?

d = reduce(lambda x, y: x * y, b)
print(d) # 720
e = reduce(lambda x, y: 2 * x + 3 * y, b)
print(e) # 296

# mapは配列の各要素に対して処理を行う
a = [i * i for i in range(5)]
print(a) # [0, 1, 4, 9, 16]
b = list(map(lambda i : i * 2, a))
print(b) # [0, 2, 8, 18, 32]

# filterは配列から特定の要素を抽出するときに使う
x = [1, -2, 3, -4, 5]
y = list(filter(lambda x: x > 0, x))
print(y) # [1, 3, 5]

# reduuce, map, filterは自作関数も使える。
def func(n):
    if n % 3 == 0 or n % 10 == 3: return True
    if n // 10 == 3: return True
    return False

x = range(100)
y = list(filter(func, x))
print(y) # 0から100までのうち3の倍数と3が含まれる数だけが抽出される
