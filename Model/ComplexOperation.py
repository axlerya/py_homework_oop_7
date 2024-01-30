import cmath
from Model.ComlexOperationAbstract import ComplexOperation


class Addition(ComplexOperation):
    """
        Класс для работы со сложением  комплекстных чисел
    """

    def operation(self, a: complex, b: complex) -> complex:
        """ Метод сложения комплексных чисел

        Args:
            a (complex): первое комплексное число
            b (complex): второе комплексное число

        Returns:
            complex: сумма комплексных чисел (a + b)
        """
        return a + b


class Subtraction(ComplexOperation):
    """
        Класс для работы с вычитанием комплекстных чисел
    """

    def operation(self, a: complex, b: complex) -> complex:
        """ Метод вычитания комплексных чисел

        Args:
            a (complex): первое комплексное число
            b (complex): второе комплексное число

        Returns:
            complex: результат вычитания комплексных чисел (a - b)
        """
        return a - b


class Multiplication(ComplexOperation):
    """
        Класс для работы с умножением комплекстных чисел
    """

    def operation(self, a: complex, b: complex) -> complex:
        """ Метод умножения комплексных чисел

        Args:
            a (complex): первое комплексное число
            b (complex): второе комплексное число

        Returns:
            complex: результат умножения комплексных чисел (a * b)
        """
        return a * b


class Division(ComplexOperation):
    """
        Класс для работы с делением комплекстных чисел
    """

    def operation(self, a: complex, b: complex) -> complex:
        """ Метод деления комплексных чисел

        Args:
            a (complex): первое комплексное число
            b (complex): второе комплексное число

        Returns:
            complex: результат деления комплексных чисел (a / b)
        """
        return a / b


class Sine(ComplexOperation):
    """
        Класс для работы с синусом комплекстных чисел
    """

    def operation(self, a: complex) -> complex:
        """ Метод вычисления синуса числа

        Args:
            a (complex): комплексное число

        Returns:
            complex: синус а
        """
        return cmath.sin(a)


class Cosine(ComplexOperation):
    """
        Класс для работы с косинусом комплекстных чисел
    """

    def operation(self, a: complex) -> complex:
        """ Метод вычисления косинусa числа

        Args:
            a (complex): комплексное число

        Returns:
            complex: косинус а
        """
        return cmath.cos(a)