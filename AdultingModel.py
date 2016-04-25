import sqlite3 

conn = sqlite3.connect("adulting.db")


class Adulting_Model:

        def __init__(self):
                pass

        def check_player(self, username, password):
                conn = sqlite3.connect('adulting.db')
                c = conn.cursor()
                username = username
                password = password


                c = conn.execute(
                    """
                    SELECT * FROM player
                    WHERE username = ?
                    AND password = ?;
                """

                (username, password))

                player = c.fetchone()
                if player == True:
                            pass

                else:
                            reject 

                return c.fetchone()
 
# conn = sqlite3.connect('adulting.db')
# print "Database has been accessed";

# cursor = conn.execute("SELECT id, username, password, gender, marital_status, age, occupation")
# for row in cursor:
#    print "ID = ", row[0]
#    print "USERNAME = ", row[1]
#    print "PASSWORD = ", row[2]
#    print "GENDER = ", row[3]
#    print "MARITAL_STATUS", row[4]
#    print "AGE = ", row[5]
#    print "OCCUPATION = ", row[6], "\n"




# print "Operation complete";
# conn.close()





                    




# cursor.execute(
#     """
#     CREATE TABLE player (
#         id INTEGER PRIMARY KEY,
#         username TEXT,
#         password TEXT,
#         gender TEXT,
#         marital_status TEXT,
#         age INTEGER,
#         occupation TEXT);

#     """ 