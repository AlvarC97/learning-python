'''
Dev: Álvaro Castro
Script description: Configure SQLite3 data
'''

#Import engine database package
import sqlite3

#Create a database connnection (Database name)
con = sqlite3.connect('school.db')

#Creating cursor object by conection => Let us execute sql commands or operations (Query)
cur = con.cursor()

#Create students table
students = '''
    CREATE TABLE IF NOT EXISTS students (
        id_student INTEGER PRIMARY KEY,
        code VARCHAR(50) NOT NULL, 
        id_person INTEGER,
        status BOOLEAN NULL,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        updated_at TIMESTAMP NULL,
        deleted_at TIMESTAMP NULL,
        FOREIGN KEY (id_person) REFERENCES persons(id_person)
    );
'''
#Execute SQL (Query)
cur.execute(students)

#Create identification_types table
identification_types = '''
    CREATE TABLE IF NOT EXISTS identification_types (
        id_ident_type INTEGER PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(100) NOT NULL,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        updated_at TIMESTAMP NULL,
        deleted_at TIMESTAMP NULL 
    );
'''
#Execute SQL (Query)
cur.execute(identification_types)

#Create persons table
persons = '''
    CREATE TABLE IF NOT EXISTS persons (
        id_person INTEGER PRIMARY KEY,
        firstname VARCHAR(50) NOT NULL,
        lastname VARCHAR(50) NOT NULL,
        id_ident_type INTEGER,
        ident_number VARCHAR(15) NOT NULL,
        id_exp_city INTEGER,
        address VARCHAR(150) NOT NULL,
        mobile VARCHAR(50) NOT NULL, 
        id_user INTEGER,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        updated_at TIMESTAMP NULL,
        deleted_at TIMESTAMP NULL,
        FOREIGN KEY (id_ident_type) REFERENCES identification_types(id_ident_type) 
    );
'''
#Execute SQL (Query)
cur.execute(persons)

#Create users table
users = '''
    CREATE TABLE IF NOT EXISTS users (
        id_user INTEGER PRIMARY KEY,
        email VARCHAR(100) NOT NULL,
        password VARCHAR(255) NOT NULL,
        status BOOLEAN NULL,
        id_ident_type INTEGER,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        updated_at TIMESTAMP NULL,
        deleted_at TIMESTAMP NULL,
        FOREIGN KEY (id_user) REFERENCES persons(id_user)
    );
'''
#Execute SQL (Query)
cur.execute(users)

#Create cities table
cities = '''
    CREATE TABLE IF NOT EXISTS cities (
        id_exp_city INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(10) NOT NULL,
        id_dept INTEGER,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        updated_at TIMESTAMP NULL,
        deleted_at TIMESTAMP NULL,
        FOREIGN KEY (id_exp_city) REFERENCES persons(id_exp_city)
    );
'''
#Execute SQL (Query)
cur.execute(cities)

#Create deparmets table
deparments = '''
    CREATE TABLE IF NOT EXISTS departments (
        id_dept INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(10) NOT NULL,
        id_country INTEGER,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        updated_at TIMESTAMP NULL,
        deleted_at TIMESTAMP NULL,
        FOREIGN KEY (id_dept) REFERENCES cities(id_dept)
    );
'''
#Execute SQL (Query)
cur.execute(deparments)
#Create persons table
countries = '''
    CREATE TABLE IF NOT EXISTS countries (
        id_country INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(10) NOT NULL,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        updated_at TIMESTAMP NULL,
        deleted_at TIMESTAMP NULL,
        FOREIGN KEY (id_country) REFERENCES departments(id_country)
    );
'''
#Execute SQL (Query)
cur.execute(countries)
#Save changes in database => Push to database
con.commit()

#print("::: Database market has been created :::")

#Close connection
#con.close()