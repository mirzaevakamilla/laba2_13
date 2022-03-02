# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import hi


if __name__ == "__main__":
    sample_string = (
         "Уважаемый(-ая) %F% %N%! Вы делаете работу по замыканиям функций."
    )
    name, surname = input("Введите имя и фамилию: ").split()
    print(hi.sample(sample_string)(name, surname))
