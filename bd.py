from tkinter import ttk,messagebox
import sqlite3
def registrarse3(self):
    conn = sqlite3.connect('usuariosBD.sqlite')
    cur= conn.cursor()
    #cur.execute('DROP TABLE IF EXISTS usuarios')
    #cur.execute('CREATE TABLE usuarios (name VARCHAR(128), password VARCHAR(128), email VARCHAR(128))') 
    nombre=str(self.keyword.get())
    contr=str(self.keyword1.get())
    try:
        correo=str(self.keyword3.get())
        print(correo)
        c= cur.execute('INSERT INTO usuarios (name,password,email) VALUES (?, ?,?)', (nombre,contr,correo))
        conn.commit()
    except:
        a=cur.execute('SELECT * FROM usuarios WHERE name = ? AND password = ?',(nombre,contr))
        if a.fetchall():
            messagebox.showinfo(title = "Login correcto", message = "Usuario y contraseña correctos")
        else:
            messagebox.showerror(title = "Login incorrecto", message = "Usuario o contraseña incorrecta")

    cur.close()