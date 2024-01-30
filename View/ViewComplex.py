from View.View import View


class ViewComplex(View):
    """
        Класс для отображения комплексных чисел в консоли
    """
    
    def send_in_console(self, complex_number: complex):
        """Метод вывода в консоль комплексного числа

        Args:
            complex_number (complex): комплексное число
        """
        return print(f"комплексное число: {complex_number}\nдействительная часть: {complex_number.imag}\nмнимая часть: {complex_number.real}")