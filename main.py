import sqlite3 as sq


def create_database(db: str):
    """Функция для создания базы данных отдела кадров"""
    with sq.connect(db) as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS position (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            position_name TEXT
            );
        """)
        cur.execute("""CREATE TABLE IF NOT EXISTS employees (
            id INTEGER NOT NULL,
            full_name TEXT,
            sex TEXT,
            birth_year INTEGER,
            address TEXT,
            job_start_year INTEGER,
            experience AS (2017 - job_start_year),
            promotion TEXT,
            position_id INTEGER,
            FOREIGN KEY (position_id) REFERENCES position (id),
            CONSTRAINT personnel_number PRIMARY KEY(id)
            );
        """)


def populate_database(db: str):
    """Функция заполнения базы данных отдела кадров"""
    with sq.connect(db) as con:
        cur = con.cursor()
        # запрос на внесение данных в таблицу position
        sql = 'INSERT INTO position (position_name) values(?)'
        # указываем данные для запроса
        data = [
            ('Аналитик',),
            ('Программист',),
            ('Менеджер проектов',),
            ('Секретарь',),
        ]
        # добавляем записи в таблицу position
        cur.executemany(sql, data)
        # запрос на внесение данных в таблицу employees
        sql = 'INSERT INTO employees (id, full_name, sex, birth_year, address, ' \
              'job_start_year, promotion, position_id) values(?, ?, ?, ?, ?, ?, ?, ?)'
        # указываем данные для запроса
        data = [
            (1000, 'Карпов В.И.', 'муж.', 1978, 'Капроновская наб. 1', 2004, 'есть', 3),
            (1001, 'Варламов П.И.', 'муж.', 1988, ' Варгуновский бульвар, 2', 2007, 'нет', 2),
            (1002, 'Карасева А.Г.', 'жен.', 1992, 'Батайская улица, 1', 2008, 'нет', 1),
            (1003, 'Потапов И.Е.', 'муж.', 1970, 'Северный 2-й проезд, 3', 1999, 'есть', 2),
            (1004, 'Вешнякова В.М.', 'жен.', 1990, 'Ореховый бульвар, 2', 2012, 'нет', 4),
        ]
        # добавляем записи в таблицу employees
        cur.executemany(sql, data)


def get_query_result(db: str, q: int):
    """Функция получения результата требуемого запроса к базе данных
    Функция запроса на получение данных из БД"""
    with sq.connect(db) as con:
        cur = con.cursor()
        if q == 1:
            s = input('Введите первую букву фамилии сотрудника:\n')
            pass
        elif q == 2:
            pass
        elif q == 3:
            # выбор диапазона табельных номеров из базы данных
            while True:
                try:
                    min_number = int(input())
                    max_number = int(input())
                    break
                except ValueError:
                    print('Ошибка ввода. Должно быть целое число!')

            pass
        elif q == 4:
            pass
        else:
            sex = input('Введите пол сотрудника:\n')
            while True:
                try:
                    birth_year = int('Введите год рождения сотрудника:\n')
                    break
                except ValueError:
                    print('Ошибка ввода. Должно быть целое число!')

            pass
        return 'результат'


def choose_command() -> int:
    """Функция выбора команды для вывода в консоль"""
    task = """
    Программа по требованию выдает списки:
    1. По заданной первой букве фамилии сотрудника
    2. По стажу
    3. По заданному пользователем диапазону табельных номеров,
    отсортированный по году рождения
    4. По поощрениям,отсортированный по стажу
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
