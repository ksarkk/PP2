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

    #[INFO] Creating a table :

    # with conn.cursor() as cursor :
    #     cursor.execute(
    #         """CREATE TABLE phonebook(
    #             name VARCHAR(255) NOT NULL,
    #             phone VARCHAR(11) NOT NULL) """
    #     )
    #     print("[INFO] Table successfully created!")

    print("""Type a number :
        1. Get an user by pattern
        2. Insert new user and phone (Update phone if user already exist)
        3. Insert list of users
        4. Query data by pagination
        5. Delete data by name or by phone""")
    
    my_input = input()

    sample_list = [['Alibek', '87476547889'], ['Alibi', '87475457845'], ['ErrorPhone', '874747445455']]

    match my_input :
        case "1" :
            print("""Type a number : 
        1. Part of phone number
        2. Part of name""")

            input1 = input()

            match input1 :
                case "1" :
                    pattern = input("Enter your pattern : ")

                    with conn.cursor() as cur :
                        cur.execute(f"""SELECT * FROM phonebook WHERE phone ~ '.*{pattern}.*'""")
                        print(cur.fetchall())
                case "2" :
                    pattern = input("Enter part of name : ")
                    with conn.cursor() as cur :
                        cur.execute(f"""SELECT * FROM phonebook WHERE name ~ '.*{pattern}.*'""")
                        print(cur.fetchall())

        case "2" :
            my_name = input("Enter users name : ")
            my_phone = input("Enter users phone : ")

            with conn.cursor() as cur :
                cur.execute(f"""SELECT * FROM phonebook WHERE name = '{my_name}'""")
                if cur.fetchall() :
                    cur.execute(f"""UPDATE phonebook SET phone = '{my_phone}' WHERE name = '{my_name}'""")
                    print(f"[INFO] {my_name}s phone number was successfully changed")
                else :
                    cur.execute(f"""INSERT INTO phonebook (name, phone) VALUES ('{my_name}', '{my_phone}')""")
                    print(f"[INFO] New user was successfully added")

        case "3" :
            for lis in sample_list :
                if len(lis[1]) != 11 :
                    print(f"[ERROR] Phone number was typed incorrectly! --- {lis[0]} ---> {lis[1]}")
                else :
                    with conn.cursor() as cur :
                        cur.execute(f"""INSERT INTO phonebook (name, phone) VALUES ('{lis[0]}', '{lis[1]}')""")

        case "4" :
            input4 = int(input("Enter the id : "))
            
            with conn.cursor() as cur :
                cur.execute(f"""SELECT * FROM phonebook LIMIT 1 OFFSET {input4 - 1};""")
                print(cur.fetchone())
        
        case "5" :
            print("""Type a number : 
        1.Delete data by username
        2.Delete data by phone number""")

            input5 = input()

            match input5 :
                case "1" :
                    my_name = input("Enter the name : ")

                    with conn.cursor() as cur :
                        cur.execute(f"""DELETE FROM phonebook WHERE name = '{my_name}'""")
                        print(f'[INFO] User {my_name} was successfully deleted')
                case "2" :
                    my_phone = input("Enter the phone number : ")

                    with conn.cursor() as cur :
                        cur.execute(f"""DELETE FROM phonebook WHERE phone = '{my_phone}'""")
                        print(f'[INFO] User with {my_phone} phone number was successfully deleted')
            
except Exception as ex :
    print("[ERROR]", ex)

finally :
    if conn is not None:
        conn.close()
        print("[INFO] Connection was closed")