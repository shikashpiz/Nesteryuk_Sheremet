# Цена товара и количество единиц
product_price = 870
product_quantity = 9

# Находим сумму заказа
base_amount = product_price * product_quantity

# Определяем процент скидки по правилам
if base_amount < 1000:
    discount_rate = 0
elif base_amount <= 5000:
    discount_rate = 5
else:
    discount_rate = 10

# Считаем скидку и сумму после неё
discount_value = base_amount * discount_rate / 100
payable_amount = base_amount - discount_value

print("=== КАЛЬКУЛЯТОР СКИДКИ ===")
print(f"Цена за единицу: {product_price:.2f} руб.")
print(f"Количество товара: {product_quantity}")
print(f"Стоимость без скидки: {base_amount:.2f} руб.")
print(f"Размер скидки: {discount_rate}%")
print(f"Сумма скидки: {discount_value:.2f} руб.")
print(f"Итоговая стоимость: {payable_amount:.2f} руб.")

# Пример покупки:
# взято 9 единиц товара по 870 рублей.
#
# Почему выбраны такие числа:
# они переводят заказ в диапазон максимальной скидки 10%.
