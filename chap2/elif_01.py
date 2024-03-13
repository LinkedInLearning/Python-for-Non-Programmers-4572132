score = 55

#パターン1
if score >= 80:
    print("とても良い")

#パターン2
if score >= 60:
    print("合格")
else:
    print("不合格")

#パターン3
if score >= 90:
    print("すばらしい")
elif score >= 80:
    print("とても良い")
elif score >= 60:
    print("まあ良い")
else:
    print("今回は残念")

#三項演算子を使うとパターン2が1行で書ける
print("合格") if score >= 60 else print("不合格")