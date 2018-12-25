import requests
# ・text属性：WebページのHTMLデータ
# ・status_code属性：レスポンスのステータスコード(？)
# HTMLが欲しいので.textで取り出す。
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

response = requests.get("https://twitter.com/foxydrove/status/1077649841495265280")

print(response.encoding)
#response.encoding = response.apparent_encoding
print(response.encoding)

text = response.text

with open("samplehtmls/sample_7.html", 'w', encoding = 'utf-8') as file: # encoding='utf-8'を追加
    file.write(text)

# 調べた。どうやら、'\xe3'や'\xe0'を''でreplaceしてからエンコードすれば問題ないみたい。
# 違う。cp932の色々を無視するんだって。
# 表示出来たけど'cp932'を無視した分だけスカスカ・・・・

# なんかできたような、できてないような？
# あ、sample_4の方は化けてるけど、sample_5の方は化けてない！
# sample_6はutf-8でビジュアライザーIをやり直したやつ。うん、化けてない、化けてない。なるほど・・
# 開くときにencoding = 'utf-8' ってやる必要があったのかー。
# 今日はここまで
