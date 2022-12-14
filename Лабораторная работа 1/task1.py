from typing import Union


class Phone:
    def __init__(self, num_model: int, zoom_camera: Union[(int, float)], color: str):
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


class Sofa:
    def __init__(self, length: Union[int, float], width: Union[int, float], color: str, shape: str):
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


class Telegram:
    def __init__(self, id_account: str, count_contacts: int, subscriptions: str):
        if not isinstance(id_account, str):
            raise TypeError("ID аккаунта должен содержать буквы и цифры!")
        self.id_account = id_account
        if not isinstance(count_contacts, int):
            raise TypeError("Количество контактов должно содержать число типа int")
        if count_contacts < 0:
            raise ValueError("Количество контактов не может быть меньше 0!")
        self.count_contacts = count_contacts
        if not isinstance(subscriptions, str):
            raise TypeError("Наличие или отсутствие подписок прописывается словами")
        self.subscriptions = subscriptions


if __name__ == "__main__":
    iphone = Phone(13, 10.5, 'white')
    samsung = Phone(10, 7.0, 'grey')
    sofa_1 = Sofa(200, 150, 'red', 'angular')
    sofa_2 = Sofa(180, 100, 'green', 'sofa-book')
    telegram_mother = Telegram('july_1912', 70, 'нет подписок')
    telegram_friend = Telegram('kate_11', 40, 'есть подписки')
    import doctest
    doctest.testmod()
    pass
