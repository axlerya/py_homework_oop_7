from Model.ComplexOperation import *
from View.ViewComplex import ViewComplex


class Controller:
    """
        Класс контроллер 
    """
    _view = ViewComplex()
    _addition = Addition()
    _subtraction = Subtraction()
    _multiplication = Multiplication()
    _division = Division()
    _sin = Sine()
    _cos = Cosine()

    def addition(self, a: complex, b: complex):
        """ Метод сложения комплексных чисел

        Args:
            a (complex): первое комплексное число
            b (complex): второе комплексное число
        """
        return self._view.send_in_console(self._addition.operation(a, b))

    def subtraction(self, a: complex, b: complex):
        """ Метод вычитания комплексных чисел

        Args:
            a (complex): первое комплексное число
            b (complex): второе комплексное число
        """
        return self._view.send_in_console(self._subtraction.operation(a, b))

    def multiplication(self, a: complex, b: complex):
        """ Метод умножения комплексных чисел

        Args:
            a (complex): первое комплексное число
            b (complex): второе комплексное число
        """
        return self._view.send_in_console(self._multiplication.operation(a, b))

    def division(self, a: complex, b: complex):
        """ Метод деления комплексных чисел

        Args:
            a (complex): первое комплексное число
            b (complex): второе комплексное число
        """
        return self._view.send_in_console(self._division.operation(a, b))

    def sin(self, a: complex):
        """ Метод вычисления синуса числа

        Args:
            a (complex): комплексное число
        """
        return self._view.send_in_console(self._sin.operation(a))

    def cos(self, a: complex):
        """ Метод вычисления косинуса числа

        Args:
            a (complex): комплексное число
        """
        return self._view.send_in_console(self._cos.operation(a))
