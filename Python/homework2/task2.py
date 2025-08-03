import csv


def welcome() -> None:
    """Приветственная функция программы(меню).

        Эта функция - реализация меню для программы. Сначала считывается файл,
        затем программа переходит в другие функции в зависимости от выбранного пункта

        Args:
            None

        Returns:
           None
        """
    to_open = input('Привет, введи название файла, который нужно открыть:')
    data = read_file(to_open)

    while 1:
        print('\nВведи: \n1 - чтобы получить иерархию команд \n2 - чтобы получить сводный отчёт по департаментам\n3 - чтобы сохранить отчёт в csv\n0 - чтобы выйти\n')
        n = int(input())
        if n == 1:
            step_1(data)
        elif n == 2:
            step_2(data, work_mode='for_step_2')
        elif n == 3:
            step_3(data)
            pass
        elif n == 0:
            print('Программа завершается!')
            break
        else:
            print('Нет такого пункта!')


def read_file(name: str) -> list:
    """Функция считывания файла.

           Данная функция считывает csv файл и переводит его в список списков.
           (Если в название файла - '', то по дефолту оно ставиться как 'Corp_Summary.csv' для удобства запуска)

            Args:
                name (str): Название файла

            Returns:
               list : список списков (двумерный массив с данными из csv файла)
            """
    if name == '':
        name = 'Corp_Summary.csv'
    with open(name, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        data = []
        for row in reader:
            data.append(row[0].split(';'))
        return data


def step_1(data: list) -> None:
    """Функция выводит иерархию команд.

              Данная функция обрабатывает двумерный массив, группируя команды по департаментам.
              Далее функция печатает результат.

               Args:
                   data (list): Двумерный массив с даннми из csv

               Returns:
                  None
               """
    dep_dict = {}
    for pers_info in data:
        to_add = dep_dict.get(pers_info[1], set())
        to_add.add(pers_info[2])
        dep_dict[pers_info[1]] = to_add

    for department, teams in dep_dict.items():
        teams_sorted = list(sorted(teams))
        print('Департамент:', department, '\nКоманды:', end=' ')
        print(*teams_sorted, sep=', ', end='\n\n')


def step_2(data: list, work_mode: str = 'for_step_2') -> list:
    """Функция выводит сводный отчёт по департаментам.

                  Данная функция обрабатывает двумерный массив, агрегируя данные по департаментам.
                  Далее есть два вида выполнения: напечатать данные (для пункта 2) или вывести данные в виде списка словарей (для пункта 3)

                   Args:
                       data (list): Двумерный массив с даннми из csv
                       work_mode(str): Режим работы for_step_2/for_step_3

                   Returns:
                      list : Массив словарей с агрегированными данными по департаментам
                   """
    dep_dict = {}
    for pers_info in data:
        to_add = dep_dict.get(pers_info[1], [])
        to_add.append(int(pers_info[5]))
        dep_dict[pers_info[1]] = to_add

    final_data = []
    for department, salaries in dep_dict.items():
        dep_dict_agg = {}
        dep_dict_agg['Департамент'] = department
        dep_dict_agg['Численность'] = len(salaries)
        dep_dict_agg['Минимальная ЗП'] = min(salaries)
        dep_dict_agg['Максимальная ЗП'] = max(salaries)
        dep_dict_agg['Средняя ЗП'] = round(sum(salaries) / len(salaries))
        final_data.append(dep_dict_agg)

    if work_mode == 'for_step_2':
        for dep in final_data:
            print('Департамент: {Департамент}, Численность: {Численность}, Минимальная ЗП: {Минимальная ЗП}, Максимальная ЗП: {Максимальная ЗП}, Средняя ЗП: {Средняя ЗП}'.format(**dep))

    if work_mode == 'for_step_3':
        return final_data


def step_3(data: list) -> None:
    """Функция сохраняет агрегированные данные по департаментам.

                      Данная функция сохраняет данные из пункта 2 в csv файл, перед этим она запрашивает название файла для сохранения

                       Args:
                           data (list): Двумерный массив с даннми из csv

                       Returns:
                          None
                       """
    name_of_new_file = input(
        'Введите название файла,куда нужно записать: ') + '.csv'
    final_data = step_2(data, work_mode='for_step_3')

    with open(name_of_new_file, mode='w', encoding='utf-8', newline='') as file:
        fieldnames = ['Департамент', 'Численность',
                      'Минимальная ЗП', 'Максимальная ЗП', 'Средняя ЗП']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')

        writer.writeheader()

        writer.writerows(final_data)

        print('Успешно!')


if __name__ == '__main__':
    welcome()
