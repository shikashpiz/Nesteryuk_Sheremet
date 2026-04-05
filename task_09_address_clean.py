dirty_addresses = [
    " г. Шахты,ул. Куйбышева,д. 28 ",
    "г.Новосибирск; ул.Ильича, д.11",
    "  г. Казань ;ул.Правды;д. 24  ",
]

# Здесь будем хранить уже очищенные адреса
ready_addresses = []

for dirty_address in dirty_addresses:
    # Убираем лишние пробелы по краям
    clear_address = dirty_address.strip()
    # Приводим разделители к одному виду
    clear_address = clear_address.replace(";", ",")
    clear_address = clear_address.replace(", ", ",")
    clear_address = clear_address.replace(" ,", ",")
    # Добавляем пробелы после сокращений
    clear_address = clear_address.replace("г.", "г. ")
    clear_address = clear_address.replace("ул.", "ул. ")
    clear_address = clear_address.replace("д.", "д. ")

    # Удаляем двойные пробелы
    while "  " in clear_address:
        clear_address = clear_address.replace("  ", " ")

    # Делаем единый формат после запятых
    clear_address = clear_address.replace(",", ", ")

    while "  " in clear_address:
        clear_address = clear_address.replace("  ", " ")

    ready_addresses.append(clear_address.strip())

print("=== СРАВНЕНИЕ ===")

for idx, dirty_address in enumerate(dirty_addresses, start=1):
    # Выводим адрес до и после очистки
    print(f"#{idx}")
    print(f"ДО: '{dirty_address}'")
    print(f"ПОСЛЕ: '{ready_addresses[idx - 1]}'")
    print()
