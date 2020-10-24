# используется для сортировки
from operator import itemgetter


class Lib:
    """Библиотека"""

    def __init__(self, id, name, functionality, amount_of_funcs, lang_id):
        self.id = id
        self.name = name
        self.functionality = functionality
        self.amount_of_funcs = amount_of_funcs
        self.lang_id = lang_id


class Lang:
    """Язык программирования"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class LibLang:
    """
    Библиотека написана на языке:(связь мн:мн)
    """

    def __init__(self, lib_id, lang_id):
        self.lib_id = lib_id
        self.lang_id = lang_id


# Библиотеки
libs = [
    Lib(1, 'Requests', 'Web', 87, 1),
    Lib(2, 'TensorFlow', 'Machine Learning', 172, 1),
    Lib(3, 'Matplotlib', 'MathCalculations', 35, 1),
    Lib(4, 'SQL Alchemy', 'SQL proccessing', 60, 3),
    Lib(11, 'LinqToSql', 'SQL proccessing', 51, 2),
    Lib(22, 'CacheManager', 'Web', 84, 4)
]

# Сотрудники
langs = [
    Lang(1, 'Python'),
    Lang(2, 'C#'),
    Lang(3, 'PHP'),
    Lang(4, 'GO')
]

libs_langs = [
    LibLang(1, 1),
    LibLang(2, 1),
    LibLang(3, 1),
    LibLang(4, 1),
    LibLang(11, 2),
    LibLang(3, 2),
    LibLang(22, 3),
    LibLang(22, 1),
    LibLang(22, 4),
    LibLang(4, 4),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(lib.name, lib.amount_of_funcs, lang.name)
                   for lang in langs
                   for lib in libs
                   if lib.lang_id == lang.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(lang.name, lib_lang.lib_id, lib_lang.lang_id)
                         for lang in langs
                         for lib_lang in libs_langs
                         if lang.id == lib_lang.lang_id]

    many_to_many = [(lib.name, lib.amount_of_funcs, lang_name)
                    for lang_name, lib_id, lang_id in many_to_many_temp
                    for lib in libs if lib.id == lib_id]
    print('Задание Г1')
    print(
        [
            (lang.name, [lib.name
                         for lib in libs
                         if lib.lang_id == lang.id],)
            for lang in langs
            if str.startswith(lang.name.lower(), 'p')
        ]
    )

    print('Задание Г2')
    print(sorted(
        [
            (lang.name, max([lib.amount_of_funcs
                             for lib in libs
                             if lib.lang_id == lang.id]),)
            for lang in langs
        ]
        , key=lambda x: x[1], reverse=True))

    print('Задание Г3')
    print(
        {
            x[2]: [y[0] for y in many_to_many if x[2]==y[2] ]
            for x in sorted(
            many_to_many,
            key=lambda x: x[2]
        )
        },)


if __name__ == '__main__':
    main()
