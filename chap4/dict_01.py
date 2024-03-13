fruits  = { "apple":"りんご", "grape":"ぶどう", "pear":"なし"}

print(fruits["apple"])

key = "grape"
print(f"{key}は日本語で{fruits[key]}です")

fruits["pear"] = "洋なし"

fruits["apple"] = 150

print(fruits)