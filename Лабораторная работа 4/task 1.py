from typing import Union


class Dog:
    """Базовый класс Собаки"""

    def __init__(self, name: str, sound: str, height: int, weight: int):
        """ Инициализация экземпляра класса. """
        self.name = name  # инициализируем атрибут
        self._sound = sound  # инициализируем защищенный атрибут, звук животного не изменяется
        self.height = height  # инициализируем атрибут
        self.weight = weight  # инициализируем атрибут

    def __str__(self) -> str:
        return f'Собака {self.name}, Звук {self._sound}, Рост {self.height}, Вес {self.weight}'

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, sound={self._sound!r}, height={self.height!r}," \
               f" weight={self.weight!r}) "

    def hair_cut(self):
        """Метод стрижка"""
        self.weight -= 1

    def give_rostishka(self):
        """Метод: выпить ростишку"""
        self.height += 5


class German_Shepherd(Dog):
    """Дочерний класс Немецкая Овчарка"""

    def __init__(self, name: str, sound: str, height: int, weight: int, age: Union[int, float], owner: str):
        super().__init__(name, sound, height, weight)
        self.age = age
        self.owner = owner

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, sound={self._sound!r}, height={self.height!r}," \
               f" weight={self.weight!r}, age={self.age!r}, owner={self.owner!r}) "

    def __str__(self) -> str:
        return f'Немецкая Овчарка {self.name}, Звук {self._sound}, Рост {self.height}, Вес {self.weight}, ' \
               f'Возраст {self.age}, Владелец {self.owner} '

    def give_rostishka(self):
        """Метод: выпить ростишку перезагружен,
        немецкие овчарки растут медленнее, чем другие породы собак"""
        self.height += 1


class Chihuahua(Dog):
    """Дочерний класс Чихуахуа"""

    def __init__(self, name: str, sound: str, height: int, weight: int, age: Union[int, float], brother_dog: str):
        super().__init__(name, sound, height, weight)
        self.age = age
        self._brother_dog = brother_dog  # инициализируем защищенный атрибут, брат собаки не изменяется при рождении

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, sound={self._sound!r}, height={self.height!r}," \
               f" weight={self.weight!r}, age={self.age!r}, brother_dog={self._brother_dog!r}) "

    def __str__(self) -> str:
        return f'Чихуахуа {self.name}, Звук {self._sound}, Рост {self.height}, Вес {self.weight}, ' \
               f'Возраст {self.age}, Брат собаки {self._brother_dog} '

    def hair_cut(self):
        """Метод стрижка перезагружен,
        у чихуахуа меньше шерсти, поэтому сбросит вес меньше, чем другие породы собак"""
        self.weight -= 0.5


if __name__ == "__main__":
    # Write your solution here
    Dog_1 = Chihuahua("Лютик", "Гав!", 18, 3, 4.5, "Ромашка")
    print(Dog_1)
    Dog_1.hair_cut()
    print(Dog_1)
    Dog_2 = German_Shepherd("Дженифер", "Гав!!!", 60, 25, 2.5, "Миша")
    print(Dog_2)
    Dog_2.give_rostishka()
    print(Dog_2)
