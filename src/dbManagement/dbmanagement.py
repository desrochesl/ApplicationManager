import sqlite3 as sql
from sqlite3 import Connection
from sqlite3 import Cursor


class connection:
    """
    Connection:
        creates a connection to a database using SQLite.
    Args:
      tableName (str): Name for a table.
    """

    def __init__(self, tableName: str):
        self.conn: Connection = sql.connect(f"{tableName}.db")
        self.c: Cursor = self.conn.cursor()
        self.tableName: str = tableName

        self.createTable()

    def createTable(self):
        self.c.execute(f"""CREATE TABLE IF NOT EXISTS {self.tableName} (
                         companyID INTEGER PRIMARY KEY AUTOINCREMENT,
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

    def insertInto(self, *inputs):
        """Inserts a new row into the database
        Args:
            *inputs (Tuple): List of values to add to the database
        """
        placeholder = {
            "companyName": inputs[0],
            "contact": inputs[1],
            "position": inputs[2],
        }
        query = f"INSERT INTO {self.tableName} (companyName, contact, position) VALUES (:companyName, :contact, :position)"
        self.c.execute(query, placeholder)

    def deleteAll(self):
        self.c.execute(f"""DELETE FROM {self.tableName}""")
        ...

    def fetchAll(self) -> str:
        self.c.execute(f"""SELECT * FROM {self.tableName}""")
        return self.c.fetchall()

    def closeConn(self):
        self.conn.commit()
        self.conn.close()
        ...


if __name__ == "__main__":
    # Create a connection
    a: connection = connection("applications")

    # Fresh table
    # a.deleteAll()

    # Insert test values into table
    a.insertInto("a", "b", "c")

    a.insertInto("Apple", "My Mom", "Nerd")

    a.insertInto("Google", "My Mom", "Senior Engineer")

    # Selects rows to output
    a.selectAll()

    # Outputs selected rows
    print(a.fetchAll())

    # commit and close the connection
    a.closeConn()

    ...
