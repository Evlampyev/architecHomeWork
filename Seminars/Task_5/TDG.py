import sqlite3


class StudentTableGateway:
    # Соединение с базой данных
    def __init__(self, conn):
        self.conn = conn

    def findAll(self):
        # Здесь мы формируем SQL запрос на получение всех записей из таблицы студентов.
        sql = "SELECT * FROM students"
        cur = self.conn.cursor()
        cur.execute(sql)
        return cur.fetchall()

    def insert(self, id, name, course):
        # Здесь мы формируем SQL запрос на вставку новой записи в таблицу студентов.
        sql = "INSERT INTO students (id, name, course) VALUES (?, ?, ?)"
        cur = self.conn.cursor()
        cur.execute(sql, (id, name, course))
        self.conn.commit()

    def update(self, id, name, course):
        # Здесь мы формируем SQL запрос на обновление записи в таблице студентов.
        sql = "UPDATE students SET name = ?, course = ? WHERE id = ?"
        cur = self.conn.cursor()
        cur.execute(sql, (name, course, id))
        self.conn.commit()

    def delete(self, id):
        # Здесь мы формируем SQL запрос на удаление записи из таблицы студентов.
        sql = "DELETE FROM students WHERE id = ?"
        cur = self.conn.cursor()
        cur.execute(sql, (id,))
        self.conn.commit()
