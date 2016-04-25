import sqlite3 

conn = sqlite3.connect("adulting.db")


conn.execute(
    """
    CREATE TABLE player (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT,
        gender TEXT,
        marital_status TEXT,
        age INTEGER,
        occupation TEXT

    );

    """ 

)

conn.commit()
conn.close()

print ("New database has been created")
