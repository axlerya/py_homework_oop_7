from abc import ABC, abstractmethod


class ComplexOperation(ABC):
    """
        Абстрактный класс для операций с комплекстными числами
    """
    
    @abstractmethod
    def operation(self):
        """
        абстрактный метод операции с комплекстным числом
        """
        pass