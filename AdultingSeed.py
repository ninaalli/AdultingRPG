"""
Seed the database with admins
"""


import sqlite3


db = 'adulting.db'


PLAYERS = [
    ["hrgunn", "FourHead", "male", "single", "28", "Athlete"],
    ["ninaalli", "EleGiggle", "female", "significantother", "33", "Hacker"]

]

conn = sqlite3.connect(db)
c = conn.cursor()

print("Destroying old data")
c.execute("DELETE FROM player")


for player in PLAYERS:
    c.execute("""
        INSERT INTO player
        ("username", "password", "gender", "marital_status", "age", "occupation" )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (player[0], player[1], player[2], player[3], player[4], player[5])

        )

conn.commit()

c.close()

print ("Seems Good! We're done here!")