'''
C => Create (INSERT INTO)
R => Read   (SELECT)
U => Update (UPDATE)
D => Delete (DELETE)

UPDATE AND DELETE NEED A WHERE CLAUSE.
'''

from database import con, cur
import os
import bcrypt

status_menu = True
global status_op

def hash_password(passwd):
    return bcrypt.hashpw(passwd.encode(), bcrypt.gensalt())

def create_user(op):
    #Create a new user
    os.system('clear')

    print("::: Signup form :::")
    fname = input("Your firstname: ")
    lname = input("Your lastname: ")
    ident = input("Your ident number: ")
    email = input("Your email: ")
    passwd = input("Your password: ")
    passwd_hashed = hash_password(passwd)

    new_user = f'''
        INSERT INTO 
            users (firstname, lastname, ident_number, email, password) 
            VALUES('{fname}', '{lname}', '{ident}', '{email}', "{passwd_hashed}")
    '''
    con.execute(new_user)
    con.commit()

    print("::: New user has been created sucessfully :::")
    os.system('pause')
    menu()

def list_active_users(op):
    #Read all the data from table users
    query_list_users = '''
        SELECT 
            u.id, 
            u.firstname,
            u.lastname,
            u.ident_number,
            u.email,
            u.password,
            CASE WHEN u.status = true THEN 'Active' ELSE 'Inactive' END as status,
            u.created_at,
            u.updated_at,
            u.deleted_at 
        FROM 
            users u
        WHERE 
            status = true
    ''' 
    os.system('clear')
    cur.execute(query_list_users)
    #print(cur.fetchall())
    data = cur.fetchall()

    print("-" * 95)
    print("{:<10} {:<20} {:<10} {:<20} {:<10} {:<20}".format("ID", "Firstname", "Lastname", "E-mail", "Status", "Created at"))
    print("-" * 95)
    for row in data:
        print("{:<10} {:<20} {:<10} {:<20} {:<10} {:<20}".format(row[0], row[1], row[2], row[4], row[6], row[7]))

    print("\n")
    os.system('pause')
    menu()

def list_inactive_users(op):
    #Read all the data from table users
    query_list_users = '''
        SELECT 
            u.id, 
            u.firstname,
            u.lastname,
            u.ident_number,
            u.email,
            u.password,
            CASE WHEN u.status = true THEN 'Active' ELSE 'Inactive' END as status,
            u.created_at,
            u.updated_at,
            u.deleted_at 
        FROM 
            users u
        WHERE 
            status = false
    ''' 
    os.system('clear')
    cur.execute(query_list_users)
    #print(cur.fetchall())
    data = cur.fetchall()

    print("-" * 95)
    print("{:<10} {:<20} {:<10} {:<20} {:<10} {:<20}".format("ID", "Firstname", "Lastname", "E-mail", "Status", "Created at"))
    print("-" * 95)
    for row in data:
        print("{:<10} {:<20} {:<10} {:<20} {:<10} {:<20}".format(row[0], row[1], row[2], row[4], row[6], row[7]))

    print("\n")
    os.system('pause')
    menu()

def list_all_users(op):
    #Read all the data from table users
    query_list_users = '''
        SELECT 
            u.id, 
            u.firstname,
            u.lastname,
            u.ident_number,
            u.email,
            u.password,
            CASE WHEN u.status = true THEN 'Active' ELSE 'Inactive' END as status,
            u.created_at,
            u.updated_at,
            u.deleted_at 
        FROM 
            users u
    ''' 
    os.system('clear')
    cur.execute(query_list_users)
    #print(cur.fetchall())
    data = cur.fetchall()

    print("-" * 95)
    print("{:<10} {:<20} {:<10} {:<20} {:<10} {:<20}".format("ID", "Firstname", "Lastname", "E-mail", "Status", "Created at"))
    print("-" * 95)
    for row in data:
        print("{:<10} {:<20} {:<10} {:<20} {:<10} {:<20}".format(row[0], row[1], row[2], row[4], row[6], row[7]))

    print("\n")
    os.system('pause')
    menu()

def search_user(op):
    os.system('clear')
    print("::: SEARCH USER BY IDENTIFICATION NUMBER :::")
    ident_num = input("Identification number: ")

    cur.execute(f"SELECT firstname, email FROM users WHERE ident_number = '{ident_num}' ")
    print(cur.fetchall())

    os.system('pause')
    menu()

def update_user(op):
    os.system('clear')
    print("::: UPDATE USER FORM :::")
    iden = input("User identification: ")

    cur.execute("SELECT firstname FROM users WHERE  ident_number=?", [iden])
    print(f"Current name: {cur.fetchall()}")

    user_name = input("New user name: ")

    conf = input("Do you want to update the user-name? (Y/n): ")
    if conf == 'Y' or conf == 'y':
        query_update_user = f'''
            UPDATE 
                users 
            SET 
                firstname = '{user_name}', 
                updated_at = datetime('now','localtime') 
            WHERE 
                ident_number = '{iden}'
        '''
        cur.execute(query_update_user)
        con.commit()
        print("::: User-name has been updated successfully :::")

    cur.execute("SELECT firstname FROM users WHERE  ident_number=?", [iden])
    print(f"Current name: {cur.fetchall()}")

    os.system('pause')
    menu()

def delete_user(op):
    os.system('clear')
    print("::: DELETE USER FORM :::")
    iden = input("Enter the user identification: ")

    cur.execute("SELECT firstname, lastname FROM users WHERE ident_number=?", [iden])
    print(f"User to delete is: {cur.fetchall()}")

    conf = input("Do you want to delete the user? (Y/n): ")
    if conf == 'Y' or conf == 'y':
        cur.execute(f"DELETE FROM users WHERE ident_number = '{iden}' ")
        con.commit()
        print("::: User has been deleted successfully :::")

    cur.execute("SELECT firstname, lastname FROM users WHERE  ident_number=?", [iden])
    print(f"Current name: {cur.fetchall()}")

    os.system('pause')
    menu()

def change_user_status(opt):
    os.system('clear')
    os.system('clear')
    print("::: UPDATE USER STATUS FORM :::")
    iden = input("User identification: ")

    cur.execute("SELECT CASE WHEN status = true THEN 'Active' ELSE 'Inactive' END as status FROM users WHERE ident_number=?", [iden])
    print(f"Current status: {cur.fetchall()}")

    new_status = input("New user status (0: Inactive, 1: Active): ")

    conf = input("Do you want to update the user-status? (Y/n): ")
    if conf == 'Y' or conf == 'y':
        query_update_user = f'''
            UPDATE 
                users 
            SET 
                status = '{new_status}', 
                deleted_at = datetime('now','localtime') 
            WHERE 
                ident_number = '{iden}'
        '''
        cur.execute(query_update_user)
        con.commit()
        print("::: User-status has been updated successfully :::")

    cur.execute("SELECT CASE WHEN status = true THEN 'Active' ELSE 'Inactive' END as status FROM users WHERE ident_number=?", [iden])
    print(f"Current name: {cur.fetchall()}")

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
        print("[1]. Create a new user")
        print("[2]. List active users")
        print("[3]. List inactive users")
        print("[4]. List all users")
        print("[5]. Search user")
        print("[6]. Update user")
        print("[7]. Delete user")
        print("[8]. Change user status")
        print("[9]. Exit")
        
        while status_opt:
            opt = input("Press an option: ")
            if opt < '1' or opt > '9':
                print(".:::::: Invalid option, try again.")
            else :
                status_opt = False

        if opt == '1':
            create_user(opt)
        elif opt == '2':
            list_active_users(opt)
        elif opt == '3':
            list_inactive_users(opt)
        elif opt == '4':
            list_all_users(opt)
        elif opt == '5':
            search_user(opt)
        elif opt == '6':
            update_user(opt)
        elif opt == '7':
            delete_user(opt)
        elif opt == '8':
            change_user_status(opt)       
        else: 
            print("::: See 'u soon :::")
            exit()
    
#Call main menu
menu()

#Close connection
con.close()