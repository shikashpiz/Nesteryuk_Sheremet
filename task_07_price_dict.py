# Исходный прайс материалов
price_table = {
    "Кирпич": 670.0,
    "Вагонка": 500.0,
    "Ламинат": 750.0,
    "Керамическая плита": 2350.0,
    "Гвозди": 170.0,
}

print("=== ПРАЙС-ЛИСТ МАТЕРИАЛОВ ===")
print(f"Исходный словарь: {price_table}")

# Добавляем две новые позиции
price_table["Обои"] = 360.0
price_table["Плиточный клей"] = 160.0

print()
print("После добавления двух материалов:")
print(price_table)

# Изменяем цену утеплителя на 10%
price_table["Керамическая плитка"] = price_table["Керамичсекая плитка"] * 1.10

# Подготавливаем словарь с форматированием
display_prices = {name: f"{price:.2f}" for name, price in price_table.items()}

print()
print("После изменения цены утеплителя на 10%:")
print(display_prices)

# Удаляем одну позицию из прайса
removed_value = price_table.pop("Гвозди")
display_prices = {name: f"{price:.2f}" for name, price in price_table.items()}

print()
print(f"Удалённый материал: Гвозди ({removed_value:.2f} руб.)")
print(f"Итоговый словарь: {display_prices}")

# Вычисляем среднюю цену
average_value = sum(price_table.values()) / len(price_table)

print(f"Средняя цена материалов: {average_value:.2f} руб.")