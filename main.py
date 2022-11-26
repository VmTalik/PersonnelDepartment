import sqlite3 as sq


def creating_database():
    """Функция для создания базы данных отдела кадров"""
    with sq.connect('pers_department.db') as con:
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


def populate_database():
    """Функция заполнения базы данных отдела кадров"""
    with sq.connect('pers_department.db') as con:
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
            (1000, 'Алексей', 'мужчина', '01.11.1978', 'Капроновская наб. 1', 2004, 'есть', 3),
            (1001, 'Петр', 'мужчина', '07.10.1988', ' Варгуновский бульвар, 2', 2007, 'нет', 2),
            (1002, 'Марина', 'женщина', '03.08.1992', 'Батайская улица, 1', 2008, 'нет', 1),
            (1003, 'Илья', 'мужчина', '01.05.1970', 'Северный 2-й проезд, 3', 1999, 'есть', 2),
            (1004, 'Виктория', 'женщина', '05.12.1990', 'Ореховый бульвар, 2', 2012, 'нет', 4),
        ]
        # добавляем записи в таблицу employees
        cur.executemany(sql, data)


creating_database()
populate_database()
