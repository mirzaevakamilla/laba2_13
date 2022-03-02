def add():
    """
    Запросить данные о товаре.
    """

    name = input("Имя: ")
    zodiac = input("Знак зодиака: ")
    dateString = input("Дата: ")

    # Создать словарь.
    return {
        'name': name,
        'zodiac': zodiac,
        'dateString': dateString,
    }
