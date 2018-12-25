# Web上のhtmlを取得する・・みたいな。
# ステップ1: requestsモジュールをpip install requestsでインストール
# インストールされたのは・・
# certifi-2018.11.29, chardet-3.0.4, idna-2.8, requests-2.21.0, urllib3-1.24.1
# ですね～～～

import requests
# URLをgetするにはrequests.get関数を使う。
# Responseオブジェクトが返ってくる。これは？
# ・text属性：WebページのHTMLデータ
# ・status_code属性：レスポンスのステータスコード(？)
# HTMLが欲しいので.textで取り出す。

# sample: https://inaridarkfox4231.github.io/LT/ ビジュアライザー、自分の。

response = requests.get("https://twitter.com/Shizu_Cent_News/status/1077644147480190976")
# print(response.text)
print(response.encoding)
response.encoding = response.apparent_encoding
print(response.encoding)
with open("samplehtmls/sample_4.html", 'w') as file:
    file.write(response.text)

# 文字化けしてるんですけど・・
# response.encoding = response.apparent_encoding
# UTF-8がUTF-8になっただけ。はい、だめ。

# 調べた。どうやら、'\xe3'や'\xe0'を''でreplaceしてからエンコードすれば問題ないみたい。
