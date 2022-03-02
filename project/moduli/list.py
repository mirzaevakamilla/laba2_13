def list(mans):
    if mans:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                "№",
                "Ф.И.О.",
                "Знак зодиака",
                "Дата"
            )
        )
        print(line)
        # Вывести данные о всех людях.
        for idx, man in enumerate(mans, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                    idx,
                    man.get('name', ''),
                    man.get('zodiac', ''),
                    man.get('dateString', '')
                )
            )
        print(line)
