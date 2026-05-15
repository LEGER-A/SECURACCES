import sqlite3
from flask_bcrypt import Bcrypt

## Connection a la base sqlite3
conn = sqlite3.connect('id_utilisateurs.db')

## Creation d'un curseur
cursor = conn.cursor()

## Suppression des tables   
cursor.execute("DROP TABLE cartes_rfid")
cursor.execute("DROP TABLE journaux_acces")
cursor.execute("DROP TABLE admins")

## Creation des tables "carte_rfid" et "admins" "journaux_acces"
cursor.execute("""CREATE TABLE cartes_rfid (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    uid TEXTE UNIQUE NOT NULL
                )""")

cursor.execute("""CREATE TABLE admins (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )""")

cursor.execute("""CREATE TABLE journaux_acces (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    uid TEXT,
                    resultat TEXT,
                    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )""")

## Creation des donnees RFID    
cartes = [
    ('uid1',),
    ('uid2',),
    ('uid3',),
    ('uid4',)
]
cursor.executemany('INSERT INTO cartes_rfid (uid) VALUES (?)', cartes)

## Creation des donnees admins   
bcrypt = Bcrypt()
admins = [
    ('antoine', bcrypt.generate_password_hash('1234')),
    ('toto', bcrypt.generate_password_hash('4567'))
]
cursor.executemany('INSERT INTO admins (username, password) VALUES (?, ?)', admins)

## Commit the changes to the database
conn.commit()

## Close the cursor and the database connection
cursor.close()
conn.close()