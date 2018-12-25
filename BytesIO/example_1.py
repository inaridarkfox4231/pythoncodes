# BytesIO使ってみる。
# とりあえず、Web上の画像を取得してみよう。

# インターネット上の画像を取得したのち、BytesIOを経由して、
# Pillowで保存するスクリプト。
# 参考→https://techacademy.jp/magazine/19185

import io
import urllib.request
from PIL import Image

# url = "https://pbs.twimg.com/card_img/1075279465473748992/osfB4tKP?format=jpg&name=600x314"
# url = "https://pbs.twimg.com/media/DvQ6bNSWkAAJ_q5.jpg"
# url = "https://pbs.twimg.com/media/DgsPvSsVAAAirTh.jpg"
url = "https://pbs.twimg.com/media/DvMVkEZV4AEzSkM.jpg"
# 画像データを取得する
img_in = urllib.request.urlopen(url).read()
img_bin = io.BytesIO(img_in)
# Pillowで開き、画像を保存する
img = Image.open(img_bin)
img.save("sampleimages/sample_4.png","png")
