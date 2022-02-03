import sqlite3


import sqlite3
conn = sqlite3.connect('usuariosBD.sqlite') #crea la base de datos
cur= conn.cursor()
cur.execute('DROP TABLE IF EXISTS usuarios')
cur.execute('CREATE TABLE usuarios (name VARCHAR(128), password VARCHAR(128), email VARCHAR(128))') ##crea la tabla Usuarios
cur.close()