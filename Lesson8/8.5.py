"""7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата."""


class Complex:

    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a

    def __mul__(self, other):
        return self.a * other.a



c_1 = Complex(1 + 1j)
c_2 = Complex(1 + 4j)
print(type(c_1))
print(c_1 * c_2)
print(c_1 + c_2)