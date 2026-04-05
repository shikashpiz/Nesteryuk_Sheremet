# Входной номер дня недели
day_index = int(input("Введите номер дня недели: "))

# Подбираем название дня
if day == 1:
    day_name = "Понедельник"
elif day == 2:
    day_name = "Вторник"
elif day == 3:
    day_name = "Среда"
elif day == 4:
    day_name = "Четверг"
elif day == 5:
    day_name = "Пятница"
elif day == 6:
    day_name = "Суббота"
elif day == 7:
    day_name = "Воскресенье"
else:
    day_name = "Некорректный номер дня"

# Проверяем, рабочий это день или выходной
if 1 <= day <= 5:
    status_text = "Рабочий день"
    mode_value = "8:00 - начало смены"
elif day == 6 or day == 7:
    status_text = "Выходной"
    mode_value = "Отдых"
else:
    status_text = "Не определён"
    mode_value = "Проверьте номер дня"

print("=== РАБОЧИЙ ГРАФИК ===")
print(f"Номер дня: {day}")
print(f"День недели: {day_name}")
print(f"Статус: {status_text}")
print(f"Режим: {mode_value}")
