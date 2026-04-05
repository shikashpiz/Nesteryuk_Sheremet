# Списки материалов от трёх исполнителей
executor_1 = ["Кирпчич", "Вагонка", "Ламинат", "Керамический клей"]
executor_2 = ["Вагонка", "Обои", "Гвозди", "Керамичсекая плитка"]
executor_3 = ["Вагонка", "Керамический клей", "Ламитнат ", "Кирпич"]

# Приводим списки к множествам
set_a = set(executor_1)
set_b = set(executor_2)
set_c = set(executor_3)

# Выполняем операции над множествами
union_all = set_a | set_b | set_c
intersection_all = set_a & set_b & set_c
unique_first = set_a - set_b - set_c
intersection_two = (set_a & set_b) | (set_a & set_c) | (set_b & set_c)
intersection_two = intersection_two - intersection_all

print("=== АНАЛИЗ ЗАКАЗОВ ===")
print(f"Материалы первого подрядчика: {executor_1}")
print(f"Материалы второго подрядчика: {executor_2}")
print(f"Материалы третьего подрядчика: {executor_3}")
print()
print(f"Все уникальные материалы: {sorted(union_all)}")
print(f"Общие для всех: {sorted(intersection_all)}")
print(f"Только у первого подрядчика: {sorted(unique_first)}")
print(f"Ровно у двух подрядчиков: {sorted(intersection_two)}")