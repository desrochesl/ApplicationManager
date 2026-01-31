import sqlite3 as sql

conn = sql.connect("applications.db")

c = conn.cursor()

# c.execute("""CREATE TABLE applications (
#           companyName text,
#           contact text,
#           position text)""")
        #   ,deadline DATE,
        #   sentResume DATE,
        #   recieved DATE,
        #   interview DATE,
        #   followUp text,
        #   description text
        #   )""")

c.execute("DELETE FROM applications")


c.execute("INSERT INTO applications VALUES ('Apple', 'My Mom', 'Nerd')")
c.execute("INSERT INTO applications VALUES ('Google', 'My Mom', 'Senior Engineer')")

c.execute("SELECT * FROM applications")

print(c.fetchall())

conn.commit()

conn.close()

