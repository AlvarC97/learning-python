'''
C => Create (INSERT INTO)
R => Read   (SELECT)
U => Update (UPDATE)
D => Delete (DELETE)

UPDATE AND DELETE NEED A WHERE CLAUSE.
'''

from school_db import con, cur
import os
import bcrypt

status_menu = True
global status_op

def hash_password(passwd):
    return bcrypt.hashpw(passwd.encode(), bcrypt.gensalt())

def create_user(op):
    # Crear users
    os.system('clear')

    print("::: Create user :::")
    usemail = input("Enter email of your user: ")
    passwd = input("Enter password of your user: ")
    passwd_hashed = hash_password(passwd)
    users = f'''
        INSERT INTO 
            users (email, password) 
            VALUES('{usemail}', '{passwd_hashed}')
    '''
    cur.execute(users)
    con.commit()

    print("::: New user has been created successfully :::")
    os.system('pause')
    menu()

def create_identification_type(op):
    # Crear un tipo de identificación
    os.system('clear')

    print("::: Create identification type :::")
    name = input("Enter name of your identification type: ")
    abrev = input("Enter abbreviation of your identification type: ")
    descrip = input("Enter description of your identification type: ")

    identification_types = f'''
        INSERT INTO 
            identification_types (name, abrev, descrip) 
            VALUES('{name}', '{abrev}', '{descrip}')
    '''
    cur.execute(identification_types)
    con.commit()

    print("::: New identification type has been created successfully :::")
    os.system('pause')
    menu()

def create_person(op):
    # Crear una persona
    os.system('clear')

    print("::: Create Person :::")
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    idNumber = input("Enter your ident number: ")
    address = input("Enter your address: ")
    mobile = input("Enter your mobile: ")

    persons = f'''
        INSERT INTO 
            persons (firstname, lastname, ident_number, address, mobile) 
            VALUES('{fname}', '{lname}', '{idNumber}', '{address}', '{mobile}')
    '''
    cur.execute(persons)
    con.commit()

    print("::: New person has been created successfully :::")
    os.system('pause')
    menu()

def create_city(op):
    # Crear ciudad
    os.system('clear')

    print("::: Create city :::")
    cname = input("Enter name of your city: ")
    cabrev = input("Enter abreviation of your city: ")
    cdescrip= input("Enter description of your city: ")

    cities = f'''
        INSERT INTO 
            cities (name, abrev, descrip) 
            VALUES('{cname}', '{cabrev}', '{cdescrip}')
    '''
    cur.execute(cities)
    con.commit()

    print("::: New city has been created successfully :::")
    os.system('pause')
    menu()

def create_deparment(op):
    # Crear departamento
    os.system('clear')

    print("::: Create department :::")
    dname = input("Enter name of your department: ")
    dabrev = input("Enter abreviation of your department: ")
    ddescrip= input("Enter description of your department: ")

    departments = f'''
        INSERT INTO 
            departments (name, abrev, descrip) 
            VALUES('{dname}', '{dabrev}', '{ddescrip}')
    '''
    cur.execute(departments)
    con.commit()

    print("::: New department has been created successfully :::")
    os.system('pause')
    menu()

def create_country(op):
    # Crear pais
    os.system('clear')

    print("::: Create country :::")
    coname = input("Enter name of your country: ")
    coabrev = input("Enter abreviation of your country: ")
    codescrip= input("Enter description of your country: ")

    countries = f'''
        INSERT INTO 
            countries (name, abrev, descrip) 
            VALUES('{coname}', '{coabrev}', '{codescrip}')
    '''
    cur.execute(countries)
    con.commit()

    print("::: New country has been created successfully :::")
    os.system('pause')
    menu()

def create_student(op):
    # Crear estudiante
    os.system('clear')

    print("::: Create student :::")
    ecode = input("Enter your code of student: ")
    cur.execute("SELECT * from persons")
    print( )
    students = f'''
        INSERT INTO 
            students (code) 
            VALUES('{ecode}')
    '''
    cur.execute(students)
    con.commit()

    print("::: New user has been created successfully :::")
    os.system('pause')
    menu()


def menu():
    global opt
    status_opt = True
    while status_menu: 
        os.system('clear')
        print(":::::::::::::::::::::::")
        print(":::::: MAIN MENU ::::::")
        print(":::::::::::::::::::::::")
        print("[1]. Create identification type")
        print("[2]. Create person")
        print("[3]. Create city")
        print("[4]. Create department")
        print("[5]. Create country ")
        print("[6]. Create user")
        print("[7]. Create student")
        print("[8]. Exit")
        
        while status_opt:
            opt = input("Press an option: ")
            if opt < '1' or opt > '8':
                print(".:::::: Invalid option, try again.")
            else :
                status_opt = False

        if opt == '1':
            create_identification_type(opt)
        elif opt == '2':
            create_person(opt)
        elif opt == '3':
            create_city(opt)
        elif opt == '4':
            create_deparment(opt)
        elif opt == '5':
            create_country(opt)
        elif opt == '6':
            create_user(opt)
        elif opt == '7':
            create_student(opt)      
        else: 
            print("::: See 'u soon :::")
            exit()
    
#Call main menu
menu()

#Close connection
con.close()

