import random

print(random.randint(1,10))

print(random.random())

answer = random.randint(1,3)

if answer == 1:
    print(f"はい={answer}")
elif answer == 2:
    print(f"いいえ={answer}")
else:
    print(f"たぶん={answer}")
