import psycopg2
import csv
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
        1. Upload data from csv file
        2. Insert new user from console
        3. Update user or phone
        4. Query data
        5. Delete user by name""")
    
    my_input = input()

    match my_input :
        case "1" :
            with open("lab10\sample.csv") as file :
                reader = csv.reader(file)

                for row in reader :
                    with conn.cursor() as cur :
                        cur.execute(f"""INSERT INTO phonebook (name, phone) VALUES ('{row[0]}', '{row[1]}')""")
                        
                print('[INFO] CSV file successfully inserted')
 
        case "2" :
            my_name = input("Enter users name : ")
            my_phone = input("Enter users phone : ")

            with conn.cursor() as cur :
                cur.execute(f"""INSERT INTO phonebook (name, phone) VALUES ('{my_name}', '{my_phone}')""")

                print('[INFO] New user successfully added')

        case "3" :
            print("""Type a number :
        1. Update users name
        2. Update users phone""")

            input3 = input()

            match input3 :
                case "1" :
                    old_name = input('Enter the name to change : ')
                    new_name = input('Enter new name : ')

                    with conn.cursor() as cur :
                        cur.execute(f"""UPDATE phonebook SET name = '{new_name}' WHERE name = '{old_name}'""")
                        print(f'[INFO] User "{old_name}" was successfully changed to "{new_name}"')

                case "2" :
                    old_phone = input('Enter the phone to change : ')
                    new_phone = input('Enter new phone : ')

                    with conn.cursor() as cur :
                        cur.execute(f"""UPDATE phonebook SET phone = '{new_phone}' WHERE phone = '{old_phone}'""")
                        print(f'[INFO] Phone number {old_phone} was successfully changed to {new_phone}')

        case "4" :
            print("""Type a number :
        1. Show users name by phone number
        2. Show phone number by users name
        3. Show phone number and user by id""")
            
            input4 = input()
            
            match input4 :
                case "1" :
                    my_phone = input("Enter the phone number : ")

                    with conn.cursor() as cur :
                        cur.execute(f"""SELECT name FROM phonebook WHERE phone = '{my_phone}'""")
                        print(cur.fetchone())

                case "2" :
                    my_name = input("Enter users name : ")

                    with conn.cursor() as cur :
                        cur.execute(f"""SELECT phone FROM phonebook WHERE name = '{my_name}'""")
                        print(cur.fetchone())

                case "3" :
                    my_id = int(input("Enter the id(integer) : "))

                    with conn.cursor() as cur :
                        cur.execute(f"""SELECT * FROM phonebook LIMIT 1 OFFSET {my_id - 1};""")
                        print(cur.fetchone())

        case "5" :
            my_name = input("Enter the name to delete : ")

            with conn.cursor() as cur :
                cur.execute(f"""DELETE FROM phonebook WHERE name = '{my_name}'""")
                print(f'[INFO] User {my_name} was successfully deleted')

except Exception as ex :
    print("[ERROR]", ex)

finally :
    if conn is not None:
        conn.close()
        print("[INFO] Connection was closed")

# with open("lab10\sample.csv") as file :
#     reader = csv.reader(file)

#     for row in reader :
#         print(row[0])