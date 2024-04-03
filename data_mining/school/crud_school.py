'''
C => Create (INSERT INTO)
R => Read   (SELECT)
U => Update (UPDATE)
D => Delete (DELETE)

UPDATE AND DELETE NEED A WHERE CLAUSE.
'''

from school_db import con, cur
import os
import sqlite3

# Crear un nuevo país
def create_country(op):
    os.system('clear')
    print("::: Create Country :::")
    name_country = input("Enter country name: ")
    abrev_country = input("Enter country abbreviation: ")
    descrip_country = input("Enter country description: ")

    new_country_query = f'''
        INSERT INTO countries (name, abrev, descrip, created_at, updated_at, deleted_at)
        VALUES ('{name_country}', '{abrev_country}', '{descrip_country}', datetime('now', 'localtime'), datetime('now', 'localtime'), null)
    '''
    cur.execute(new_country_query)
    con.commit()

    print("::: New country has been created successfully :::")
    os.system('pause')
    menu()

# Crear un nuevo departamento
def create_department(op):
    os.system('clear')
    print("::: Create Department :::")
    name_department = input("Enter department name: ")
    abrev_department = input("Enter department abbreviation: ")
    descrip_department = input("Enter department description: ")
    country_id = int(input("Enter ID of associated country: "))

    try:
        # Verificar si el ID del país existe
        cur.execute(f"SELECT 1 FROM countries WHERE id_countries = {country_id}")
        country_exists = cur.fetchone()
        if country_exists:
            new_department_query = f'''
                INSERT INTO department (name, abrev, descrip, id_countries, created_at, updated_at, deleted_at)
                VALUES ('{name_department}', '{abrev_department}', '{descrip_department}', {country_id}, datetime('now', 'localtime'), datetime('now', 'localtime'), null)
            '''
            cur.execute(new_department_query)
            con.commit()

            print("::: New department has been created successfully :::")
        else:
            print("Error: This country ID does not exist.")
            os.system('pause')
            create_department(op)
    except sqlite3.IntegrityError:
        print("Error: Failed to create department.")
        os.system('pause')
        create_department(op)
    finally:
        os.system('pause')
        menu()

# Crear una nueva ciudad
def create_city(op):
    os.system('clear')
    print("::: Create Cities :::")
    name_city = input("Enter city name: ")
    abrev_city = input("Enter city abbreviation: ")
    descrip_city = input("Enter city description: ")
    department_id = int(input("Enter ID of associated department: "))

    try:
        # Verificar si el ID del departamento existe
        cur.execute(f"SELECT 1 FROM department WHERE id_department = {department_id}")
        department_exists = cur.fetchone()
        if department_exists:
            new_city_query = f'''
                INSERT INTO cities (name, abrev, descrip, id_department, created_at, updated_at, deleted_at)
                VALUES ('{name_city}', '{abrev_city}', '{descrip_city}', {department_id}, datetime('now', 'localtime'), datetime('now', 'localtime'), null)
            '''
            cur.execute(new_city_query)
            con.commit()

            print("::: New city has been created successfully :::")
        else:
            print("Error: This department ID does not exist.")
            os.system('pause')
            create_city(op)
    except sqlite3.IntegrityError:
        print("Error: Failed to create city.")
        os.system('pause')
        create_city(op)
    finally:
        os.system('pause')
        menu()

# Crear un nuevo tipo de identificaciòn
def create_identification_types(op):
    os.system('clear')
    print("::: Create identification_types :::")
    name_identification_types = input("Enter identification_types name: ")
    abrev_identification_types = input("Enter identification_types abbreviation: ")
    descrip_identification_types = input("Enter identification_types description: ")

    new_identification_types_query = f'''
        INSERT INTO identification_types (name, abrev, descrip, created_at, updated_at, deleted_at)
        VALUES ('{name_identification_types}', '{abrev_identification_types}', '{descrip_identification_types}', datetime('now', 'localtime'), datetime('now', 'localtime'), null)
    '''
    cur.execute(new_identification_types_query)
    con.commit()

    print("::: New identification_types has been created successfully :::")
    os.system('pause')
    menu()

# Crear un nuevo usuario
def create_users(op):
    os.system('clear')
    print("::: Create users :::")
    email_users = input("Enter users email: ")
    password_users = input("Enter users password: ")
    status_users = input("Enter user's status (True/False): ").lower()
    

    # Asegurarse de que el status introducido sea True, False o NULL
    if status_users in ['true', 'false']:
        new_users_query = f'''
            INSERT INTO users (email, password, status, created_at, updated_at, deleted_at)
            VALUES ('{email_users}', '{password_users}', {status_users}, datetime('now', 'localtime'), datetime('now', 'localtime'), null)
        '''
    else:
        new_users_query = f'''
            INSERT INTO users (email, password, created_at, updated_at, deleted_at)
            VALUES ('{email_users}', '{password_users}', datetime('now', 'localtime'), datetime('now', 'localtime'), null)
        '''
    cur.execute(new_users_query)
    con.commit()

    print("::: New user has been created successfully :::")
    os.system('pause')
    menu()

# Crear una nueva persona
def create_person(op):
    os.system('clear')
    print("::: Create person :::")
    fname_person = input("Enter first name: ")
    lname_person = input("Enter last name: ")
    id_identification = int(input("Enter ID of associated identification_types: "))
    ident_number = input("Enter identification number: ")
    id_cities = int(input("Enter ID of associated cities: "))
    address = input("Enter address: ")
    mobile = input("Enter mobile number: ")
    id_users = int(input("Enter ID of associated users: "))

    try:
        # Verificar si el ID del identification_types existe
        cur.execute(f"SELECT 1 FROM identification_types WHERE id_identification_types = {id_identification}")
        identification_exists = cur.fetchone()
        if identification_exists:
            # Verificar si el ID del cities existe
            cur.execute(f"SELECT 1 FROM cities WHERE id_cities = {id_cities}")
            city_exists = cur.fetchone()
            if city_exists:
                # Verificar si el ID del users existe
                cur.execute(f"SELECT 1 FROM users WHERE id_users = {id_users}")
                user_exists = cur.fetchone()
                if user_exists:
                    new_person_query = f'''
                        INSERT INTO persons (first_name, last_name, id_identification_types, ident_number, id_cities, address, mobile, id_users, created_at, updated_at, deleted_at)
                        VALUES ('{fname_person}', '{lname_person}', {id_identification}, '{ident_number}', {id_cities}, '{address}', '{mobile}', {id_users}, datetime('now', 'localtime'), datetime('now', 'localtime'), null)
                    '''
                    cur.execute(new_person_query)
                    con.commit()

                    print("::: New person has been created successfully :::")
                else:
                    print("Error: This user ID does not exist.")
                    os.system('pause')
                    create_person(op)
            else:
                print("Error: This city ID does not exist.")
                os.system('pause')
                create_person(op)
        else:
            print("Error: This identification_types ID does not exist.")
            os.system('pause')
            create_person(op)
    except sqlite3.IntegrityError:
        print("Error: Failed to create person.")
        os.system('pause')
        create_person(op)
    finally:
        os.system('pause')
        menu()

# Crear un nuevo estudiante
def create_students(op):
    os.system('clear')
    print("::: Create Students :::")
    code = input("Enter student code: ")
    id_persons = int(input("Enter ID of associated person: "))
    status_students = input("Enter student's status (True/False): ").lower()

    try:
        # Verificar si el ID de persons existe
        cur.execute(f"SELECT 1 FROM persons WHERE id_persons = {id_persons}")
        persons_exists = cur.fetchone()
        if persons_exists:
            # Asegurarse de que el status introducido sea True, False o NULL
            if status_students in ['true', 'false', 'null']:
                new_students_query = f'''
                    INSERT INTO students (code, id_persons, status, created_at, updated_at, deleted_at)
                    VALUES ('{code}', {id_persons}, {status_students}, datetime('now', 'localtime'), datetime('now', 'localtime'), null)
                '''
                cur.execute(new_students_query)
                con.commit()
                print("::: New student has been created successfully :::")
            else:
                print("Error: Invalid student status.")
                os.system('pause')
                create_students(op)
        else:
            print("Error: This person ID does not exist.")
            os.system('pause')
            create_students(op)
    except sqlite3.IntegrityError:
        print("Error: Failed to create student.")
        os.system('pause')
        create_students(op)
    finally:
        os.system('pause')
        menu()


# Mostrar menú
def menu():
    while True:
        os.system('clear')
        print(":::::::::::::::::::::::")
        print(":::::: MAIN MENU ::::::")
        print(":::::::::::::::::::::::")
        print("[1]. Create country")
        print("[2]. Create department")
        print("[3]. Create city")
        print("[4]. Create identification type")
        print("[5]. Create users")
        print("[6]. Create person")
        print("[7]. Create Student") 
        print("[8]. Exit")

        opt = input("Press an option: ")
        if opt < '1' or opt > '8':
            print(".:::::: Invalid option, try again.")
            continue

        if opt == '1':
            create_country(opt)
        elif opt == '2':
            create_department(opt)
        elif opt == '3':
            create_city(opt)
        elif opt == '4':
            create_identification_types(opt)
        elif opt == '5':
            create_users(opt)
        elif opt == '6':
            create_person(opt)
        elif opt == '7':
            create_students(opt)
        elif opt == '8':
            print("::: See 'u soon :::")
            exit()

# Llamar al menú principal
menu()

# Cerrar conexión
con.close()