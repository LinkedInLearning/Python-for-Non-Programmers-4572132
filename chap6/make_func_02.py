def say_hello():
    print("こんにちは、太郎さん")

say_hello()

def say_hello(name):
    print(f"こんにちは、{name}さん")

say_hello("次郎")
say_hello("三郎")
say_hello("四郎")

def mul_nums():
    print(1 * 2)

mul_nums()

def mul_nums(x, y):
    print(x * y)

mul_nums(3, 5)
mul_nums(10, -5)
