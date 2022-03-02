#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from moduli import add, list, help


if __name__ == '__main__':
    mans = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            mans.append(add.add())

        elif command == 'list':
            list.list(mans)

        elif command == 'help':
            mans.append(help.help())

        else:
            print(f"Неизвестная команда {command}")
