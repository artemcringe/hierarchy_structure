from hierarchy.models import Worker
from random import choice

# Скрипт для создания иерархии в БД.

all_obj = Worker.objects.all()
employee_dict = {}
for emp in all_obj:
    employee_dict[emp.position] = employee_dict.get(emp.position, []) + [emp]

employee_dict = dict(sorted(employee_dict.items(),
                            key=lambda key: int(key[0][-1]),
                            reverse=True))  # Получаем отсортированный словарь по ключам в порядке убывания.


def switch_on_dict(key):
    """Функция возвращает экземпляр нашего работника более высокого по должности"""
    dict_key = f"level_{key}"
    random_boss = choice(employee_dict.get(dict_key))
    return random_boss


def set_bosses(employees: dict):
    """Функция для установки начальников"""
    for key, value in employees.items():
        key_digit = int(key[-1])
        if key == "level_2":
            for person in value:
                if person.boss is None:
                    person.boss = employee_dict["level_1"][0]
                    person.save()
            return

        for person in value:
            if person.boss is None:
                person.boss = switch_on_dict(key_digit - 1)
                person.save()


def run():
    set_bosses(employee_dict)
