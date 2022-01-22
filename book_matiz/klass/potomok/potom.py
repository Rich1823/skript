# Классы находятся в файле potomok.
import potomok
num1 = int(input("Ведите первое число :"))
num2 = int(input("Ведите второе число :"))
znak = input("Введите знак :")
out = One(num1, num2)
out_two = (Two(num1, num2))
if znak == "-":
    print(out.minus())
if znak == "+":
    print(out.plus)
if znak == "*":
    print(out_two.umno())
if znak == "/":
    print(out_two.delit())
