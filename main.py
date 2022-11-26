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


creating_database()
