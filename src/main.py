from dbManagement.dbmanagement import DBManager

if __name__ == "__main__":
    print("Hello, World!")


def createDB():
    DB = DBManager("applications")
    DB.create_table()
    return DB