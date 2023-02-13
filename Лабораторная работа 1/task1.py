from typing import Union
import doctest


class Phone:
    """Класс Телефон"""

    def __init__(self, num_model: int, zoom_camera: Union[(int, float)], color: str):
        """ Инициализация экземпляра класса. """
        if not isinstance(num_model, int):
            raise TypeError("Номер модели должен содержать цифры типа int")
        if num_model <= 0:
            raise ValueError("Номер модели не может быть меньше или равен 0!")
        self.num_model = num_model
        if not isinstance(zoom_camera, (int, float)):
            raise TypeError("Зум камеры должен содержать цифры типа int, float")
        if zoom_camera <= 0:
            raise ValueError("Зум камеры не может быть меньше или равен 0!")
        self.zoom_camera = zoom_camera
        if not isinstance(color, str):
            raise TypeError("Цвет телефона должен быть записан типа str")
        self.color = color

    def change_color(self, color_ch: str):

        """Метод изменения цвета телефона

        :param color_ch: Цвет, на который нужно поменять

        >>> Samsung = Phone(28928, 2.928, "red")
        >>> Samsung.change_color("white")

        """

        self.color = color_ch

    def improve_zoom(self, zoom_plus: (int, float)):

        """Метод улучшения качества зума камеры телефона

        :param zoom_plus: Значение зума

        >>> Samsung = Phone(28928, 2.928, "red")
        >>> Samsung.improve_zoom(3.0)

        """

        self.zoom_camera = zoom_plus


class Sofa:
    """Класс Диван"""

    def __init__(self, length: Union[int, float], width: Union[int, float], color: str, shape: str):
        """ Инициализация экземпляра класса. """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина дивана должна содержать цифры типа int, float")
        if length <= 0:
            raise ValueError("Диван не может быть длиной меньше 0!")
        self.length = length
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина дивана должна содержать цифры типа int, float")
        if width <= 0:
            raise ValueError("Ширина дивана не может быть меньше 0!")
        self.width = width
        if not isinstance(color, str):
            raise TypeError("Цвет дивана должен быть записан типа str")
        self.color = color
        if not isinstance(shape, str):
            raise TypeError("Форма дивана должна быть записана типа str")
        self.shape = shape

    def change_shape(self, shape_ch: str):
        """  Метод изменения формы дивана

            :param shape_ch: Форма дивана

            >>> my_sofa = Sofa( 50 , 60 , "red", "triangle")
            >>> my_sofa.change_shape("square") """

        self.shape = shape_ch

    def colors_sofa(self, sofa_colors: str):
        """  Метод изменения цвета дивана

                   :param sofa_colors: Цвет дивана

                   >>>my_sofa = Sofa( 50 , 60 , "red", "triangle")
                   >>>my_sofa.colors_sofa("white") """

        self.color = sofa_colors


class Telegram:
    """Класс Телеграм"""

    def __init__(self, id_account: str, count_contacts: int, amount_subscriptions: int):
        """ Инициализация экземпляра класса. """
        if not isinstance(id_account, str):
            raise TypeError("ID аккаунта должен содержать буквы и цифры!")
        self.id_account = id_account
        if not isinstance(count_contacts, int):
            raise TypeError("Количество контактов должно содержать число типа int")
        if count_contacts < 0:
            raise ValueError("Количество контактов не может быть меньше 0!")
        self.count_contacts = count_contacts
        if not isinstance(amount_subscriptions, int):
            raise TypeError("Количество подписок на каналы")
        self.amount_subscriptions = amount_subscriptions

    def chanel_sub(self):
        """Метод подписки на канал

        >>> Katya_Tel= Telegram('1212121' , 12 ,21)
        >>> Katya_Tel.chanel_sub()

        """
        self.amount_subscriptions += 1

    def chanel_unsub(self):
        """Метод отписки от канала

                >>> Katya_Tel= Telegram('1212121' , 12 ,21)
                >>> Katya_Tel.chanel_unsub()

                """
        self.amount_subscriptions -= 1


if __name__ == "__main__":
    doctest.testmod()
