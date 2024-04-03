'''
Dev: Álvaro Castro
Script description: Configure SQLite3 data
'''

#Import engine database pack
import sqlite3

#Create a database connection (Database name)
con = sqlite3.connect('school.db')

#Creating cursor objet by conection => let us execute sql comands operations (Query)
cur = con.cursor()

#create countries table
countries_table = '''
    CREATE TABLE IF NOT EXISTS countries (
        id_countries INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(10) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        deleted_at TIMESTAMP DEFAULT NULL
    ); 
'''

#create department table
department_table = '''
    CREATE TABLE IF NOT EXISTS department (
        id_department INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(10) NOT NULL,
        id_countries INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        deleted_at TIMESTAMP DEFAULT NULL,
        FOREIGN KEY (id_countries) REFERENCES countries(id_countries)
    ); 
'''

#create cities table
cities_table = '''
    CREATE TABLE IF NOT EXISTS cities (
        id_cities INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(10) NOT NULL,
        id_department INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        deleted_at TIMESTAMP DEFAULT NULL,
        FOREIGN KEY (id_department) REFERENCES department(id_department)
    ); 
'''

#create identification_types table
identification_types_table = '''
    CREATE TABLE IF NOT EXISTS identification_types (
        id_identification_types INTEGER PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(10) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        deleted_at TIMESTAMP DEFAULT NULL
    ); 
'''

#create users table
users_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id_users INTEGER PRIMARY KEY,
        email VARCHAR(100) NOT NULL,
        password TEXT(250) NOT NULL,
        status BOOLEAN NULL, 
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        deleted_at TIMESTAMP DEFAULT NULL
    ); 
'''

#create persons table
persons_table = '''
    CREATE TABLE IF NOT EXISTS persons (
        id_persons INTEGER PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        id_identification_types INTEGER,
        ident_number VARCHAR(10) NOT NULL, 
        id_cities INTEGER,
        address VARCHAR(150) NOT NULL,
        mobile VARCHAR(50) NOT NULL,
        id_users INTEGER,  
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        deleted_at TIMESTAMP DEFAULT NULL,
        FOREIGN KEY (id_cities) REFERENCES cities(id_cities),
        FOREIGN KEY (id_identification_types) REFERENCES identification_types(id_identification_types),
        FOREIGN KEY (id_users) REFERENCES users(id_users)
            
    ); 
'''

#create students table
students_table = '''
    CREATE TABLE IF NOT EXISTS students (
        id_students INTEGER PRIMARY KEY,
        code VARCHAR(50) NOT NULL,
        id_persons INTEGER,
        status boolean NULL, 
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        deleted_at TIMESTAMP DEFAULT NULL,
        FOREIGN KEY (id_persons) REFERENCES persons(id_persons)
    ); 
'''

#EXECUTE SQL (Query)
cur.execute(countries_table)
cur.execute(department_table)
cur.execute(cities_table)
cur.execute(identification_types_table)
cur.execute(users_table)
cur.execute(persons_table)
cur.execute(students_table)


#Save changes database
con.commit()

#print(":::Database market has been create:::")