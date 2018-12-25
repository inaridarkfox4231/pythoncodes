# BytesIO使ってみる。
# とりあえず、Web上の画像を取得してみよう。

# インターネット上の画像を取得したのち、BytesIOを経由して、
# Pillowで保存するスクリプト。
# 参考→https://techacademy.jp/magazine/19185

import io
import urllib.request
from PIL import Image

# 画像のURL 今回はきつねさんのアイコンを使用
url = "https://pbs.twimg.com/profile_images/1059048162222960640/sgrzwSTQ_bigger.jpg"
# 画像データを取得する
img_in = urllib.request.urlopen(url).read()
print(type(img_in)) # <class 'bytes'>
img_bin = io.BytesIO(img_in)
print(type(img_bin)) # <class '_io.BytesIO'>
# Pillowで開き、画像を保存する
img = Image.open(img_bin)
print(type(img)) # <class 'PIL.JpegImagePlugin.JpegImageFile'>
img.save("foxlab_icon.png","PNG")
# 以下のコメントを外すとバイナリデータそのものを確認できる
# print(img_bin.getvalue())
