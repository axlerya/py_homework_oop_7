from abc import ABC, abstractmethod


class View(ABC):
    """
        Абстрактный класс для отображение в консоль
    """
    @abstractmethod
    def send_in_console(self):
        pass