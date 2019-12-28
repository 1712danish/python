import sqlite3

def conection():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (ID NUMBER PRIMARY KEY,title text,author text,year integer,isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?) ",(title,author,year,isbn))   
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books")   
    rows=cur.fetchall()
    conn.close()  
    return rows

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books WHERE TITLE=? OR AUTHOR=? OR YEAR=? OR ISBN=?",(title,author,year,isbn))   
    rows=cur.fetchall()
    conn.close()  
    return rows        

def delete(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("Delete FROM books WHERE TITLE=? OR AUTHOR=? OR YEAR=? OR ISBN=?",(title,author,year,isbn))   
    conn.commit()
    conn.close()  
             

conection()    
insert("lord of the rings","J.K. Rowling",1981,4218537610)
print(view())
print(search(title="Harry Potter"))
