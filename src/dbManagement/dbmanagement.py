import sqlite3 as sql
from sqlite3 import Connection
from sqlite3 import Cursor


class connection:
    def __init__(self, tableName: str):
        self.conn: Connection = sql.connect(f"{tableName}.db")
        self.c: Cursor = self.conn.cursor()
        self.tableName: str = tableName

        self.createTable()

    def createTable(self):
        self.c.execute(f"""CREATE TABLE IF NOT EXISTS {self.tableName} (
                         companyName text,
                         contact text,
                         position text)""")

        # self.c.execute(f"""CREATE TABLE IF NOT EXISTS {self.tableName} (
        #                 companyName text,
        #                 contact text,
        #                 position text,
        #                 deadline DATE,
        #                 sentResume DATE,
        #                 recieved DATE,
        #                 interview DATE,
        #                 followUp text,
        #                 description text
        #                )""")

    def selectAll(self):
        self.c.execute(f"""SELECT * FROM {self.tableName}""")

    def insertInto(self, *inputs):
        placeholders = ", ".join(["?"] * len(inputs))

        query = f"INSERT INTO {self.tableName} VALUES ({placeholders})"

        self.c.execute(query, inputs)

    def deleteAll(self):
        self.c.execute(f"""DELETE FROM {self.tableName}""")
        ...

    def fetchAll(self):
        return self.c.fetchall()

    def closeConn(self):
        self.conn.commit()
        self.conn.close()
        ...


if __name__ == "__main__":
    a: connection = connection("applications")

    a.createTable()

    a.deleteAll()

    a.insertInto("a", "b", "c")

    a.insertInto("Apple", "My Mom", "Nerd")

    a.insertInto("Google", "My Mom", "Senior Engineer")

    a.selectAll()

    print(a.fetchAll())

    a.closeConn()

    ...
