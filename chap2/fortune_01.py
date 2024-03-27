import random

fortune_number =  random.randint(1,7)

fortune_text = ''
print(fortune_number)

if fortune_number == 1:
    fortune_text = "大吉 おめでとう"
elif fortune_number == 2:
    fortune_text = "吉 おめでとう"
elif fortune_number == 3:
    fortune_text = "中吉 おめでとう"
elif fortune_number == 4:
    fortune_text = "小吉 わるくないですよ"
elif fortune_number == 5:
    fortune_text = "末吉 大丈夫"
elif fortune_number == 6:
    fortune_text = "凶 残念"
else:
    fortune_text = "大凶 気をつけてね"

print(fortune_text)