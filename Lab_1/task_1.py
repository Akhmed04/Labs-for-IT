# TODO Написать 3 класса с документацией и аннотацией типов
from random import random
from tokenize import String


class Table:
    """"
    Класс, представляющий стол.
    """
    def __init__(self, square, height):
        """
        Инициализация обьекта стола.
        :param square:
        :param height:
        """
        if not isinstance(square, (int, float)):
            raise TypeError
        if not square > 0:
            raise ValueError
        """
        Проверка атрибута square на тип и 
        коректное числовое значение.
        """
        self.square = square  # площадь поверхности стола

        if not isinstance(height, (int, float)):
            raise TypeError
        if height < 0:
            raise ValueError
        self.height = height # высота стола
        """   
        Проверка атрибута height на тип и 
        коректное числовое значение.
        """
    def sit_down_at_the_table (self):
        print("You sat down at the table")
        """"Метод сесть за стол"""

    def get_up_from_the_table (self):
        print("You got up from the table")
        """Метод встать из-за стола"""

class Tree:
    """
    Класс, Дерево
    """
    def __init__(self, diameter, height):
        """
        Инициализация обьекта дерево
        :param diameter:
        :param height:
        """
        if not isinstance(diameter, (int, float)):
            raise TypeError
        if not diameter > 0:
            raise ValueError
        """
        Проверка атрибута diameter на тип 
        и коректность числового значения
        """
        self.diameter = diameter  # диаметер ствола дерева

        if not isinstance(height, (int, float)):
            raise TypeError
        if height < 0:
            raise ValueError
        """
        Проверка атрибута height на тип 
        и коректность числового значения
        """
        self.height = height # высота дерева

    def water_the_tree(self):
        print("You watered the tree")
        """Метод полив дерева"""

    def look_for_an_apple(self):
        probability = random()
        if(probability < 0.5):
            print("You didn't find the apple")
        else:
            print("You found the apple")
        """
        Метод поиска яблока на дереве 
        Реализован с помощью функции random()
        
        """


class Car:
    """
    Класс, машина
    """
    def __init__(self, make, max_speed):
        """
        Инициализация обьекта машина
        :param make:
        :param max_speed:
        """
        if not isinstance(make, str):
            raise TypeError
        if not make == "":
            raise ValueError
        """
        Проверка атрибута make на тип
        и заполнености строки
        """
        self.make = make  # площадь поверхности стола

        if not isinstance(max_speed, (int, float)):
            raise TypeError
        if max_speed < 0:
            raise ValueError
        """
        Проверка атрибута  max_speed на тип 
        и коректность числового значения. 
        """
        self.max_speed = max_speed # высота стола

    def start(self):
        print("The car started moving")
        """Метод начала движения"""

    def stop(self):
        print("The car stopped")
        """Метод остановки"""

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
    pass
