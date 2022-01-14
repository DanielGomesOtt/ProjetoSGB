import pyodbc
from passlib.context import CryptContext

#connection and disconnection
def sgbConnect():
    dataConnection = (
        "Driver={SQL Server};"
        "Server=DanOtt;"
        "Database=SGB;"
    )

    connection = pyodbc.connect(dataConnection)
    return connection

def sgbDisconnection(connection, window, mnu):
    window.destroy()
    return True

def sgbDisconnection1(connection, window, mnu):
    cursor = connection.cursor()
    cursor.close()
    connection.close()
    window.destroy()
    mnu.menuLogin()
    return True

#SQL books
def insertBooks(connect, title, author, publisher, number_pages, genre, publication_date, quantity_book):
    command = f"INSERT INTO BOOKS (Title, Author, Publisher, Number_Pages, Genre, Publication_Date, Quantity_Book) VALUES('{title}', '{author}', '{publisher}', '{number_pages}', '{genre}', CAST('{publication_date}' AS DATE), '{quantity_book}');"
    try:
        cursor = connect.cursor()
        cursor.execute(command)
        cursor.commit()
        return True
    except:
        return False


def updateBooks(Id, title, author, publisher, number_pages, genre, publication_date, quantity_book, connect):
    command = f"""UPDATE BOOKS 
                  SET
                  Title = '{title}', 
                  Author = '{author}',
                  Publisher = '{publisher}',
                  Number_Pages = {number_pages},
                  Genre = '{genre}',
                  Publication_Date = CAST('{publication_date}' AS DATE),
                  Quantity_Book = {quantity_book}
                  WHERE ID = {Id};
            """
    try:
        cursor = connect.cursor()
        cursor.execute(command)
        cursor.commit()
        return True
    except:
        return False
    


def deleteBooks(connect, Id):
    command = f"""DELETE FROM BOOKS WHERE ID = {Id};"""
    try:
        cursor = connect.cursor()
        cursor.execute(command)
        cursor.commit()
        return True
    except:
        return False

#SQL clients
def insertClient(connect, cpf, name, phone):
    pwd_context = CryptContext(schemes="sha256_crypt")
    cpf_test = cpf
    cursor = connect.cursor()
    command = f"""SELECT * FROM CLIENT;"""
    cursor.execute(command)
    rows = cursor.fetchall()
    for i in rows:
        if pwd_context.verify(cpf_test, i.cpf) == True:
            return False
    cpf = pwd_context.hash(cpf) 
    command = f"INSERT INTO CLIENT (cpf, Name_Client, Phone_Number) VALUES('{cpf}', '{name}', '{phone}');"
    try:
        cursor = connect.cursor()
        cursor.execute(command)
        cursor.commit()
        return True
    except:
        return False
    


def updateClient(connect, cpf, name, phone):
    pwd_context = CryptContext(schemes="sha256_crypt")
    cursor = connect.cursor()
    command = f"""SELECT * FROM CLIENT;"""
    cursor.execute(command)
    rows = cursor.fetchall()
    for i in rows:
        if pwd_context.verify(cpf, i.cpf) == True:
            cpf = i.cpf
            command = f"""UPDATE CLIENT 
                  SET
                  Name_Client = '{name}', 
                  Phone_Number = '{phone}'
                  WHERE cpf = '{cpf}';
            """
            try:
                cursor = connect.cursor()
                cursor.execute(command)
                cursor.commit()
                return True
            except:
                return False
    return False
    
        


def deleteClient(connect, cpf):
    pwd_context = CryptContext(schemes="sha256_crypt")
    cursor = connect.cursor()
    command = f"""SELECT * FROM CLIENT;"""
    cursor.execute(command)
    rows = cursor.fetchall()
    for i in rows:
        if pwd_context.verify(cpf, i.cpf) == True:
            cpf = i.cpf
            command = f"""DELETE FROM CLIENT WHERE cpf = '{cpf}';"""
            try:
                cursor = connect.cursor()
                cursor.execute(command)
                cursor.commit()
                return True
            except:
                return False
    return False


