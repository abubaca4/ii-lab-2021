import inspect
from abc import ABC


def dbool(bool_str: str):
    return bool_str == 'True'


class Sport(ABC):
    def __init__(self, name: str, season: str, age: int):
        self.__name = name
        self.season = season
        self.age = int(age)

    def get_type(self):
        raise NotImplementedError(
            "Пожалуйста не используйте экземпляры базового класса")

    def __str__(self):
        return ','.join([self.get_type(), *map(str, self.__dict__.values())])

    def deserialize(device_str: str):
        str_parts = device_str.split(',')
        if str_parts[0] == 'Healfull':
            return Healfull(str_parts[1], str_parts[2], int(str_parts[3]), dbool(str_parts[4]), str_parts[5])
        else:
            return Competitive(str_parts[1], str_parts[2], int(str_parts[3]), int(str_parts[4]), dbool(str_parts[5]), str_parts[6])

    @property
    def name(self):
        return self.__name

    @property
    def season(self):
        return self.__season

    @season.setter
    def season(self, season: str):
        season_LIST = ['Лето', 'Зима', 'Круглогодичные']
        if season in season_LIST:
            self.__season = season
        else:
            raise ValueError('Допустимы сезоны '+' '.join(season_LIST))

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        if age <= 2:
            raise ValueError("Возраст не может быть <= 2")
        if age > 90:
            raise ValueError(
                "Возраст спротсмена не может быть > 90")
        self.__age = age


class Healfull(Sport):
    def __init__(self, name: str, season: str, age: int, trainer_required: bool, Purpose: str):
        super().__init__(name, season, age)
        self.__trainer_required = trainer_required
        self.__Purpose = Purpose

    def get_type(self):
        return "Healfull"

    @ property
    def trainer_required(self):
        return self.__trainer_required

    @ property
    def Purpose(self):
        return self.__Purpose


class Competitive(Sport):
    def __init__(self, name: str, season: str, age: int, participants: int, conflict: bool, taget: str):
        super().__init__(name, season, age)
        self.participants = int(participants)
        self.__conflict = conflict
        self.__taget = taget

    def get_type(self):
        return "Competitive"

    @ property
    def participants(self):
        return self.__participants

    @participants.setter
    def participants(self, participants: int):
        if participants < 2:
            raise ValueError("Число участников не может быть меньше 2")
        if participants > 30:
            raise ValueError(
                "Число участников не может быть больше 30")
        self.__participants = participants

    @ property
    def conflict(self):
        return self.__conflict

    @ property
    def taget(self):
        return self.__taget


def parse_db():
    db = []
    with open('db.txt', 'r', encoding="utf-8") as db_file:
        for line in db_file.readlines():
            if len(line) > 0:
                db.append(Sport.deserialize(line.strip("\r\n ")))
    return db


def save_db():
    with open('db.txt', 'w', encoding="utf-8") as db_file:
        db_file.write('\n'.join(map(str, db)))


def add_entry(e: Sport):
    if find_entry(e.name) is None:
        db.append(e)
        save_db()
    else:
        raise ValueError(f"Запись с таким именем уже есть в базе данных")


def find_entry(name: str):
    for e in db:
        if e.name == name:
            return e
    return None


def remove_entry(name: str):
    e = find_entry(name)
    if e is not None:
        db.remove(e)
        save_db()
    else:
        raise ValueError(f"Запись с таким именем не найдена в базе данных")


db = parse_db()


def bool_to_ru(e):
    if type(e) == bool:
        return 'да' if e else 'нет'
    return e


while True:
    command = None
    en_to_ru = {
        "name": "название",
        "season": "Сезон",
        "age": "Необходимый возраст",
        "trainer_required": "Необходимо присутствие тренера",
        "Purpose": "Назначение",
        "participants": "Количество участников",
        "conflict": "Наличие непосредственной борьбой и соприкосновением с противником",
        "taget": "Цель спорта"
    }
    while command not in ['найти', 'добавить', 'удалить']:
        command = input("Выберите действие(найти, добавить, удалить): ")
    if command == 'найти':
        e = find_entry(input('название: '))
        if e is not None:
            for key in e.__dict__:
                print(
                    f"{en_to_ru[key.split('__')[1]]}: {bool_to_ru(e.__dict__[key])}")
        else:
            print(f"База знаний не содержит сведений о данном виде спорта")
    elif command == 'добавить':
        try:
            dclass = None
            while dclass not in ['оздоровительный', 'соревновательный']:
                dclass = input(
                    "Вид спорта(оздоровительный, соревновательный): ").lower()
            if dclass == "оздоровительный":
                values = []
                for key in list(inspect.signature(Healfull.__init__).parameters)[1:]:
                    values.append(input(f"{en_to_ru[key]}: "))
                for i in range(len(values)):
                    if values[i].lower() == 'да':
                        values[i] = True
                    elif values[i].lower() == 'нет':
                        values[i] = False
                add_entry(Healfull(*values))
            else:
                values = []
                for key in list(inspect.signature(Competitive.__init__).parameters)[1:]:
                    values.append(input(f"{en_to_ru[key]}: "))
                for i in range(len(values)):
                    if values[i].lower() == 'да':
                        values[i] = True
                    elif values[i].lower() == 'нет':
                        values[i] = False
                add_entry(Competitive(*values))
        except ValueError as e:
            print(e)
    else:
        try:
            remove_entry(input('название: '))
        except ValueError as e:
            print(e)
