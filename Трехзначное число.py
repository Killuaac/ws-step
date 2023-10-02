a = int(input())
first = a // 100
second = a // 10
second = second % 10
third = a % 100
third = a % 10

su = first + second + third
pr = first * second * third

print("Сумма цифр =", su)
print("Произведение цифр =", pr)
