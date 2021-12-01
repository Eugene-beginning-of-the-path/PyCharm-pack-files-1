
class Purse:
    def __init__(self, name:str, valute:str):
        self.__money = 0
        self.owner = name
        self.valuta = valute

    def add(self, value:int):
        self.__money += value

    def get(self, value:int):
        if value > self.__money:
            raise ValueError("Purse has not " + value + self.valuta)

        self.__money -= value
        return value

    def getMoney(self):
        return self.__money

    def __del__(self):
        print("Purse " + self.owner + " deleted")

def test_Purse():
    "Функция для работы с классом Purse"
    x = Purse("Sergey", "$")
    x.add(100)

    y = Purse("Lida", "Руб")
    y.add(x.get(15) * 75)
    print("Lida has " + str(y.getMoney()) + y.valuta)
    print("Sergey has " + str(x.getMoney()) + x.valuta)


class A:
    def a(self):
        print('a')

class B(A):
    def a(self):
        print('b')

class C(B):
    def a(self):
        print('c')

class D(C, A):
    def a(self):
        super.a() #демонстрация линеализации, одно и то же если бы было написано A.a()
        print(super.__class__.__mro__) #вывод алгоритма, по которому работает super()
        super(C, self).a() #вызываем метод a() класса B

def test_ABCD():
    print(D.__mro__)
#D().b()
