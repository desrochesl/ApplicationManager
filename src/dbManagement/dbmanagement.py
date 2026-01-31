import sqlite3 as sql
from sqlite3 import Connection, Cursor, Error



class DBManager:
    """
    Connection:
        creates a connection to a database using SQLite.
    Args:
      tableName (str): Name for a table.
    """

    def __init__(self, tableName: str):
        self.db_name: str = f'{tableName}.db'
        self.tableName: str = tableName
        self._conn: Connection = None
        self._c: Cursor = None

    def __enter__(self):
        # Automatically opens connection when using 'with'
        self._conn = sql.connect(self.db_name)
        self._c = self._conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Automatically commits and closes even if an error occurs
        if self._conn:
            if exc_type is None:
                self._conn.commit()
            self._conn.close()

    def create_table(self):
        query = f"""CREATE TABLE IF NOT EXISTS {self.tableName} (
                         companyID INTEGER PRIMARY KEY AUTOINCREMENT,
                         companyName text,
                         contact text,
                         position text)"""
        
        self._c.execute(query)

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

    def insert_into(self, company:str, contact: str, position:str):
        """Inserts a new row into the database
        Args:
            *inputs (Tuple): List of values to add to the database
        """

        query = f"INSERT INTO {self.tableName} (companyName, contact, position) VALUES (?, ?, ?)"
        try: 
            self._c.execute(query, (company, contact, position))
        except Error as e:
            print(f"Error inserting data: {e}")
            ...

    def delete_all(self):
        self._c.execute(f"""DELETE FROM {self.tableName}""")
        ...

    def fetch_all(self) -> str:
        self._c.execute(f"""SELECT * FROM {self.tableName}""")
        return self._c.fetchall()


if __name__ == "__main__":
    # Create a connection

    with DBManager("applications") as db:
        db.create_table()
        db.insert_into("Google", "Sundar", "CEO")
        print(db.fetch_all())

    ...
