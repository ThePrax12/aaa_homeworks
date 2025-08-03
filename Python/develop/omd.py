def step2_no_umbrella():
    print('Правильно! Как утка возьмёт зонтик? У неё же крылышки!')


def step2_umbrella():
    print('Зачем утке в баре зонтик? Там же крыша!\n')
    print('Анекдот про рекурсию:')
    step1()


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
