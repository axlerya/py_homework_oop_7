from Controller.Controller import Controller
from logger import *

a = complex(1,2)
b = complex(2,3)

controller = Controller()

def main():
    start_logger()
    controller.addition(a,b)
    print('=============================================')
    write_log(f'Сложение комплексных чисел {a} и {b}')
    controller.subtraction(a,b)
    print('=============================================')
    write_log(f'Вычитание комплексных чисел {a} и {b}')
    controller.multiplication(a,b)
    print('=============================================')
    write_log(f'Умножение комплексных чисел {a} и {b}')
    controller.division(a,b)
    print('=============================================')
    write_log(f'Деление комплексных чисел {a} и {b}')
    controller.sin(a)
    print('=============================================')
    write_log(f'Синус комплексного числа {a}')
    controller.cos(a)
    print('=============================================')
    write_log(f'Косинус комплексного числа {a}')
    
if __name__ == "__main__":
    main()