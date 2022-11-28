"""Скрипт с SQL запросами и данными. База данных отдела кадров"""
"""
========================
Создание базы данных
========================
"""
position_table = """CREATE TABLE IF NOT EXISTS position (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        position_name TEXT
                        );"""

employees_table = """CREATE TABLE IF NOT EXISTS employees (
                        id INTEGER PRIMARY KEY,
                        full_name TEXT,
                        sex TEXT,
                        birth_year INTEGER,
                        address TEXT,
                        job_start_year INTEGER,
                        experience AS (2017 - job_start_year),
                        promotion TEXT,
                        position_id INTEGER,
                        FOREIGN KEY (position_id) REFERENCES position (id)
                        );"""
"""
===============================
Внесение данных в базу данных
===============================
"""
insert_into_position = 'INSERT INTO position (position_name) values(?)'
position_name_data = [('Аналитик',),
                      ('Программист',),
                      ('Менеджер проектов',),
                      ('Секретарь',),
                      ]

insert_into_employees = 'INSERT INTO employees (id, full_name, sex, birth_year, address, ' \
                        'job_start_year, promotion, position_id) values(?, ?, ?, ?, ?, ?, ?, ?)'

employees_data = [
    (1000, 'Карпов В.И.', 'муж.', 1978, 'Капроновская наб. 1', 2004, 'есть', 3),
    (1001, 'Варламов П.И.', 'муж.', 1988, ' Варгуновский бульвар, 2', 2007, 'нет', 2),
    (1002, 'Карасева А.Г.', 'жен.', 1992, 'Батайская улица, 1', 2008, 'нет', 1),
    (1003, 'Потапов И.Е.', 'муж.', 1970, 'Северный 2-й проезд, 3', 1999, 'есть', 2),
    (1004, 'Иванов Г.О.', 'муж.', 1981, 'Назаровский бульвар, 6', 2003, 'есть', 2),
    (1005, 'Вешнякова В.М.', 'жен.', 1990, 'Ореховый бульвар, 2', 2012, 'нет', 4),

]

"""
===============================
Запросы к базе данных
===============================
"""
# выборка по заданной первой букве фамилии сотрудника
select_1 = """SELECT employees.id, full_name, sex, birth_year, address, 
                                    job_start_year, experience, promotion, position_name 
                             FROM employees INNER JOIN position
	                           ON employees.position_id = position.id
                            WHERE full_name LIKE '{}%'; """

# выборка по убыванию стажа работы сотрудников
select_2 = """SELECT employees.id, full_name, sex, birth_year, address, 
                                    job_start_year, experience, promotion, position_name 
                             FROM employees INNER JOIN position
	                           ON employees.position_id = position.id
                         ORDER BY experience DESC; """

# выборка по заданному диапазону табельных номеров, сотрудники отсортированы по убыванию года рождения
select_3 = """SELECT employees.id, full_name, sex, birth_year, address, 
                                    job_start_year, experience, promotion, position_name 
                                      FROM employees INNER JOIN position
	                                    ON employees.position_id = position.id
                                     WHERE employees.id BETWEEN {} AND {}
                                            ORDER BY birth_year DESC; """
# выборка по поощрениям,сотрудники отсортированы по убыванию стажа работы
select_4 = """SELECT employees.id, full_name, sex, birth_year, address, 
                                    job_start_year, experience, promotion, position_name 
                             FROM employees INNER JOIN position
	                           ON employees.position_id = position.id
                            WHERE promotion LIKE '%сть'
                         ORDER BY experience DESC; """
# выборка по заданному пользователем году рождения и полу
select_5 = """SELECT employees.id, full_name, sex, birth_year, address, 
                                    job_start_year, experience, promotion, position_name 
                                       FROM employees INNER JOIN position
	                                     ON employees.position_id = position.id
                                        WHERE birth_year = {} AND sex LIKE '{}%'; """
