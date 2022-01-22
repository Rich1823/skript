# создается два класса Родитель и потомок .в Итоге :Создал два класса и сделал скрипт калькулятора
# Буду пробовать с числами создам несколько методов для вычесления.
# В первом классе сложение и вычитание во втором умножение и деление
# z-это знак который должен указать пользователь
# Пример использования функции super()
class One():  # Создание первого класса
    def __init__(self, numb1, numb2):
        self.numb1 = numb1
        self.numb2 = numb2

    def plus(self):
        out_plus = self.numb1+self.numb2
        return out_plus

    def minus(self):
        out_minus = self.numb1-self.numb2
        return out_minus


class Two(One):
    def __init__(self, numb1, numb2):
        super().__init__(numb1, numb2)

    def umno(self):
        out_umno = self.numb1*self.numb2
        return out_umno

    def delit(self):
        out_delit = self.numb1 / self.numb2
        return out_delit


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
