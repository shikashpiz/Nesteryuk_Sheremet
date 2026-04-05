# Параметры помещения в метрах
space_length = 8.5
space_width = 6.0
space_height = 2.9

# Расценка за покраску квадратного метра
paint_tariff = 127

# Вычисляем площади и объём
floor_value = space_length * space_width
wall_value = 2 * (space_length + space_width) * space_height
room_capacity = space_length * space_width * space_height

# Определяем стоимость покраски стен
paint_total = wall_value * paint_tariff

print("=== ПАРАМЕТРЫ ПОМЕЩЕНИЯ ===")
print(f"Длина: {space_length} м")
print(f"Ширина: {space_width} м")
print(f"Высота: {space_height} м")
print()
print(f"Площадь пола: {floor_value:.2f} м²")
print(f"Площадь стен: {wall_value:.2f} м²")
print(f"Объём помещения: {room_capacity:.2f} м³")
print(f"Стоимость покраски стен: {paint_total:.2f} руб.")