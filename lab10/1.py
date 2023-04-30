import psycopg2
from config import host, user, db_name, password

conn = None

try :
    
    conn = psycopg2.connect(
        host = host,
        database = db_name,
        user = user,
        password = password,
    )

    conn.autocommit = True

    with conn.cursor() as cursor :
        cursor.execute(
            "SELECT version()"
        )
        print(F"Server version : {cursor.fetchone()}")

    # with conn.cursor() as cursor :
    #     cursor.execute(
    #         """CREATE TABLE phonebook(
    #             id SERIAL PRIMARY KEY,
    #             name VARCHAR(255) NOT NULL,
    #             phone INT NOT NULL) """
    #     )
    #     print("Table successfully created!")

    # with conn.cursor() as cursor :
    #     cursor.execute(
    #         """INSERT INTO phonebook (name, phone) VALUES ('Eren', 451969)"""
    #     )
    #     print("New user successfully inserted!")

    with conn.cursor() as cursor :
        cursor.execute(
            """SELECT * FROM phonebook"""
        )
        print(f"{cursor.fetchall()}")

    with conn.cursor() as cursor :
        cursor.execute(
            """DROP TABLE phonebook"""
        )
        print(f"Table 'phonebook' was successfully deleted!")

except Exception as ex :
    print("error", ex)

finally :
    if conn is not None:
        conn.close()
        print("Connection was closed")