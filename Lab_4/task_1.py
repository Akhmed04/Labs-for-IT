""""родительский класс социальные сети"""
class SocialNetwork:
    def __init__(self, name: str, users: int):
        """
        Инициализация объекта социальная сеть
        :param name: Название социальной сети
        :param users: Количество пользователей в социальной сети
        """
        self._name = name
        self._users = users

    @property
    def name(self) -> str:
        """Возвращает название"""
        return self._name

    @property
    def users(self) -> int:
        """Возврашает количество пользователей"""
        return self._users

    def __str__(self) -> str:
        return f"Социальная сеть: {self.name}, Кол-во пользователей: {self.users}"

    def __repr__(self) -> str:
        return f"Социальная сеть({self.name}, Кол-во пользователей: {self.users})"

    """""Добавление пользователей"""
    def add_users(self, count: int):
        """
        Добавляет пользователей в социальную сеть
        :param count: Количество новых пользователей
        """
        self._users +=count

""""дочерний класс телеграм"""
class Telegram(SocialNetwork):
    def __init__(self, users: int, groups: int):
        """
        Инициализация обьекта Телеграм
        :param users: Количество пользователей в телеграме
        :param groups: Количество групп
        """
        super().__init__(name='Telegram', users=users)
        self._groups = groups

    @property
    def groups(self) -> int:
        """Возвращает количество групп"""
        return self._groups

    def __str__(self) ->str:
        return f"Телеграм: Кол-во пользователей: {self.users}, Групп: {self.groups}"

    def __repr__(self) ->str:
        return f"{self.__class__.__name__} (Кол-во пользователей: {self.users}, Групп: {self.groups})"

    def add_users(self, count: int):
        """
        Добавляет пользователей и группы (на 100 человек 1 группа)
        :param count: Количество новых пользователей
        """
        super().add_users(count)
        self._groups += count // 100



if __name__ == "__main__":

    instagram = SocialNetwork("Instagram", 100000000)
    print(instagram)
    print(repr(instagram))

    instagram.add_users(2000000)
    print(instagram)


    telegram = Telegram(10000,50)
    print(telegram)
    print(repr(telegram))
    telegram.add_users(5000)
    print(telegram)
