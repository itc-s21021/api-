import requests as req

url_1 = "https://zipcloud.ibsnet.co.jp/api/search"

code = str(input("7桁の数字を入力:  "))
i_code = f"{url_1}?zipcode={code}"

url = req.get(i_code).json()["results"]

p1 = url[0]["address1"]
p2 = url[0]["address2"]
p3 = url[0]["address3"]

print("検索結果を表示します")
final = f" ({p1}の{p2}{p3}でした) "

print(final)
