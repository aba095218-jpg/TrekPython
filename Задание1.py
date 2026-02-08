import doctest


class Plant:
    def __init__(self, species: str, hydration_level: float):
        """
        Создание и подготовка к работе объекта "Растение".

        :param species: Вид растения.
        :param hydration_level: Уровень влажности почвы в процентах (0.0 - 100.0).

        Примеры:
        >>> cactus = Plant("Кактус", 20.5)  # инициализация экземпляра класса
        """
        if not isinstance(species, str):
            raise TypeError("Название вида должно быть строкой")
        if not species.strip():
            raise ValueError("Название вида не может быть пустым")
        self.species = species

        if not isinstance(hydration_level, (int, float)):
            raise TypeError("Уровень влажности должен быть типа int или float")
        if not (0 <= hydration_level <= 100):
            raise ValueError("Влажность должна быть в диапазоне от 0 до 100")
        self.hydration_level = float(hydration_level)

    def water(self, amount: float) -> None:
        """
        Полив растения для увеличения уровня влажности.

        :param amount: Процент добавляемой влаги.
        :raise ValueError: Если сумма текущей влажности и полива превышает 100%.

        Примеры:
        >>> flower = Plant("Роза", 40.0)
        >>> flower.water(30.0)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Количество воды должно быть типа int или float")
        if amount < 0:
            raise ValueError("Количество воды не может быть отрицательным")
        ...

    def check_health(self) -> bool:
        """
        Проверка состояния здоровья растения на основе влажности.

        :return: True если растение здорово, иначе False.

        Примеры:
        >>> aloe = Plant("Алоэ", 50.0)
        >>> aloe.check_health()
        """
        ...


class Elevator:
    def __init__(self, current_floor: int, max_floor: int):
        """
        Создание и подготовка к работе объекта "Лифт".

        :param current_floor: Текущий этаж.
        :param max_floor: Максимальный этаж в здании.

        Примеры:
        >>> elevator = Elevator(1, 10)
        """
        if not isinstance(max_floor, int):
            raise TypeError("Максимальный этаж должен быть целым числом")
        if max_floor <= 1:
            raise ValueError("Максимальный этаж должен быть больше 1")
        self.max_floor = max_floor

        if not isinstance(current_floor, int):
            raise TypeError("Номер этажа должен быть целым числом")
        if not (1 <= current_floor <= max_floor):
            raise ValueError(f"Этаж должен быть в диапазоне от 1 до {max_floor}")
        self.current_floor = current_floor

    def move_to_floor(self, target_floor: int) -> int:
        """
        Перемещение лифта на указанный этаж.

        :param target_floor: Целевой этаж.
        :return: Этаж, на который прибыл лифт.
        :raise ValueError: Если выбранный этаж вне допустимого диапазона.

        Примеры:
        >>> elevator = Elevator(1, 15)
        >>> elevator.move_to_floor(5)
        """
        if not isinstance(target_floor, int):
            raise TypeError("Целевой этаж должен быть целым числом")
        ...

    def open_doors(self) -> None:
        """
        Открытие дверей лифта.

        Примеры:
        >>> elevator = Elevator(2, 5)
        >>> elevator.open_doors()
        """
        ...


class Playlist:
    def __init__(self, name: str, tracks_count: int):
        """
        Создание и подготовка к работе объекта "Плейлист".

        :param name: Название плейлиста.
        :param tracks_count: Текущее количество треков в плейлисте.

        Примеры:
        >>> my_playlist = Playlist("Daily Mix", 15)
        """
        if not isinstance(name, str):
            raise TypeError("Название плейлиста должно быть строкой")
        self.name = name

        if not isinstance(tracks_count, int):
            raise TypeError("Количество треков должно быть целым числом")
        if tracks_count < 0:
            raise ValueError("Количество треков не может быть отрицательным")
        self.tracks_count = tracks_count

    def add_track(self, count: int = 1) -> int:
        """
        Добавление треков в плейлист.

        :param count: Количество добавляемых треков.
        :return: Общее количество треков после добавления.

        Примеры:
        >>> rock = Playlist("Rock", 10)
        >>> rock.add_track(2)
        """
        if not isinstance(count, int):
            raise TypeError("Количество добавляемых треков должно быть целым числом")
        if count <= 0:
            raise ValueError("Нужно добавить хотя бы один трек")
        ...

    def clear_playlist(self) -> None:
        """
        Удаление всех треков из плейлиста.

        Примеры:
        >>> hits = Playlist("Top Hits", 100)
        >>> hits.clear_playlist()
        """
        ...


if __name__ == "__main__":
    # Запуск тестов, встроенных в документацию (doctest)
    doctest.testmod()