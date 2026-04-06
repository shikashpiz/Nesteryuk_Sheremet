# Данные исполнителя
fio_student = "Нестерюк Илья Игоревич"
group_code = "52501"

# Описание объекта строительства
project_name = 'Газпром Арена"'
floors = 9
height = 75
is_residential = False
construction_year = 2017

# Переводим булево значение в текст
object_type = "Жилой" if is_residential else "Нежилой"

print("=== ПАСПОРТ СТРОИТЕЛЬНОГО ОБЪЕКТА ===")
print(f"Составитель: {fio_student}")
print(f"Группа: {group_code}")
print()
print(f"Объект: {project_name}")
print(f"Этажность: {floors} этажей")
print(f"Высота: {height} м")
print(f"Тип: {object_type}")
print(f"Год постройки: {construction_year}")

# Расположение объекта:
# г. Санкт-Петербург, Футбольная аллея, д. 1
#
# Причина выбора:
# крупный спортивный объект со сложной инженерной конструкцией
