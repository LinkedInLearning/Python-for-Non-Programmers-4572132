lst_name = ["akira","tadao","jiro","akane","siro"]

print(len(lst_name))

sorted_name = sorted(lst_name)
print(sorted_name)

search_name = "jiro"

if search_name in lst_name:
    print(f"{search_name}は入ってます")