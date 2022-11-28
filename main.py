import sqlite3 as sq
from SQL_queries_data import position_table, employees_table, position_name_data, \
    insert_into_position, employees_data, insert_into_employees, \
    select_1, select_2, select_3, select_4, select_5


def create_database(db: str):
    """Функция для создания базы данных отдела кадров"""
    with sq.connect(db) as con:
        cur = con.cursor()
        cur.execute(position_table)
        cur.execute(employees_table)


def populate_database(db: str):
    """Функция заполнения базы данных отдела кадров"""
    with sq.connect(db) as con:
        cur = con.cursor()
        cur.executemany(insert_into_position, position_name_data)
        cur.executemany(insert_into_employees, employees_data)


def get_query_result(db: str, q: int) -> any:
    """Функция получения результата требуемого запроса к базе данных"""
    with sq.connect(db) as con:
        cur = con.cursor()
        if q == 1:
            s = input('Введите первую букву фамилии сотрудника:\n').capitalize()
            cur.execute(select_1.format(s))
            rows = cur.fetchall()
            if len(rows) != 0:
                return rows
            else:
                return 'Фамилий сотрудников, начинающихся на введенную букву, нет в БД'

        elif q == 2:
            cur.execute(select_2)
            rows = cur.fetchall()
            return rows
        elif q == 3:
            while True:
                try:
                    min_n, max_n = map(int, input('Введите диапазон табельных номеров через пробел:').split())
                    cur.execute(select_3.format(min_n, max_n))
                    rows = cur.fetchall()
                    if len(rows) != 0:
                        return rows
                    else:
                        return 'Сотрудников из данного диапазона табельных номеров в БД нет'
                except ValueError:
                    return 'Ошибка ввода. Должен быть диапазон целых чисел, введеннй через пробел'
        elif q == 4:
            cur.execute(select_4)
            rows = cur.fetchall()
            if len(rows) != 0:
                return rows
            else:
                return 'У сотрудников нет поощрений'

        elif q == 5:
            sex = input('Введите пол сотрудника (м/ж):\n').lower()
            while True:
                try:
                    birth_year = int(input('Введите год рождения сотрудника:\n'))
                    cur.execute(select_5.format(birth_year, sex))
                    rows = cur.fetchall()
                    if len(rows) != 0:
                        return rows
                    else:
                        return 'Таких сотрудников нет в БД'
                except ValueError:
                    return 'Ошибка ввода. Должно быть целое число!'


def choose_command() -> int:
    """Функция выбора команды для вывода в консоль"""
    task = """
    Программа по требованию выдает списки:
    1. По заданной первой букве фамилии сотрудника
    2. По убыванию стажа работы сотрудников
    3. По заданному пользователем диапазону табельных номеров,
    сотрудники должны быть отсортированы по убыванию года рождения
    4. По поощрениям, сотрудники должы быть отсортированы по
     убыванию стажа работы
    5. По заданному пользователем году рождения и полу\n
    Выберете, какой список Вы хотите получить, введите число от 1 до 5:
    """
    while True:
        try:
            user_query = int(input(task))
            break
        except ValueError:
            print('Ошибка ввода. Должно быть целое число!')

    return user_query


def check_database(db: str) -> int:
    """Функция проверки базы данных на заполненность данными"""
    with sq.connect(db) as con:
        cur = con.cursor()
        sql = "SELECT * FROM employees;"
        # число строк данных в таблице employees
        num = len(cur.execute(sql).fetchall())
        return num


if __name__ == "__main__":
    name_db = "pers_department.db"
    create_database(name_db)
    if not check_database(name_db):
        populate_database(name_db)
    while True:
        output = get_query_result(name_db, choose_command())
        print('Полученный результат:\n', output)
        s = input('Вы желаете еще что-то получить из базы данных, введите "да" или "нет"\n')
        if s in ('Да,да'):
            pass
        else:
            break
