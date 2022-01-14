from tkinter import *
import pyodbc
from SQLConnect import *
from passlib.context import CryptContext
from datetime import *
from tkcalendar import *
from tkinter import messagebox
from tkinter import ttk

class BOOKS:

    def __init__(self):
        self.__title = ""
        self.__author = ""
        self.__publisher = ""
        self.__number_pages = int()
        self.__genre = ""
        self.__publication_date = ""
        self.__quantity_book = int()
    

    def register(self, title, author, publisher, number_pages, genre, publication_date, quantity_book, window, connect):
        self.__title = title.get()
        self.__author = author.get()
        self.__publisher = publisher.get()
        self.__number_pages = number_pages.get()
        self.__genre = genre.get()
        self.__publication_date = publication_date.get_date()
        self.__quantity_book = quantity_book.get()
        confirmation = insertBooks(connect, self.__title, self.__author, self.__publisher, self.__number_pages, self.__genre, self.__publication_date, self.__quantity_book)
        if confirmation == True:
            ok_window = Tk()
            ok_window.geometry("300x200")
            messagebox.showinfo(title='Register', message='registration completed')
            window.destroy()
            ok_window.destroy()
            return True
        elif confirmation == False:
            error_window = Tk()
            error_window.geometry("300x200")
            messagebox.showinfo(title='Register Error', message='registration error')
            window.destroy()
            error_window.destroy()
            return False
        
    
    
    def update(self, field_id, field_title, field_author, field_publisher, field_pages, field_genre, cal, spin_quantity, connect, update_window):
        
        Id = field_id.get()
        title = field_title.get()
        author = field_author.get()
        publisher = field_publisher.get()
        number_pages = field_pages.get()
        genre = field_genre.get()
        publication_date = cal.get_date()
        quantity_book = spin_quantity.get()

        confirmation = updateBooks(Id, title, author, publisher, number_pages, genre, publication_date, quantity_book, connect)
        if confirmation == True:
            ok_window = Tk()
            ok_window.geometry("300x200")
            messagebox.showinfo(title='Update', message='update completed')
            update_window.destroy()
            ok_window.destroy()
            return True
        elif confirmation == False:
            error_window = Tk()
            error_window.geometry("300x200")
            messagebox.showinfo(title='Update Error', message='Update error')
            update_window.destroy()
            error_window.destroy()
            return False
            
    

    def delete(self, field_Id, connect, window):
        Id = field_Id.get()
        
        confirmation = deleteBooks(connect, Id)
        if confirmation == True:
            ok_window = Tk()
            ok_window.geometry("300x200")
            messagebox.showinfo(title='Delete', message='Book deleted')
            window.destroy()
            ok_window.destroy()
            return True
        elif confirmation == False:
            error_window = Tk()
            error_window.geometry("300x200")
            messagebox.showinfo(title='Delete', message='Delete error')
            window.destroy()
            error_window.destroy()
            return False


    def select(self, tv, connect):
        tv.delete(*tv.get_children())
        command = "SELECT * FROM BOOKS ORDER BY ID;"
        cursor = connect.cursor()
        cursor.execute(command)
        res = cursor.fetchall()
        
        for i in res:
            tv.insert('', 'end', values=list(i))


    def plus_Book(self, field_Id, field_quantity_book, connect, window):
        Id = field_Id.get()
        quantity_book = field_quantity_book.get()

        command = f"""UPDATE BOOKS SET Quantity_Book = Quantity_Book + {quantity_book}
                      WHERE ID = {Id};"""
        
        try:
            cursor = connect.cursor()
            cursor.execute(command)
            cursor.commit()
            ok_window = Tk()
            ok_window.geometry("300x200")
            messagebox.showinfo(title='Add Book', message='book added to collection')
            window.destroy()
            ok_window.destroy()
            return True
        except:
            error_window = Tk()
            error_window.geometry("300x200")
            messagebox.showinfo(title='Add Book', message='Add error')
            window.destroy()
            error_window.destroy()
            return False


class ADM:


    def __init__(self):
        pass


    def login(self, field1, field2, window, connect, mnu, pb):
        pwd_context = CryptContext(schemes="sha256_crypt")
        user = field1.get()
        password = field2.get()
        cursor = connect.cursor()
        command = f"""SELECT * FROM LOG_ADM;"""
        cursor.execute(command)
        rows = cursor.fetchall()
        for i in rows:
            if  pwd_context.verify(user, i.Adm_User) == True and pwd_context.verify(password, i.Password_Adm) == True:
                mnu.menu(window, connect)
                return True
        mnu.loginError(pb)
        return False


    def register_adm(self, field1, field2, window, connect, mnu):
        pwd_context = CryptContext(schemes="sha256_crypt")
        user_test = field1.get()
        cursor = connect.cursor()
        command = f"""SELECT * FROM LOG_ADM;"""
        cursor.execute(command)
        rows = cursor.fetchall()
        for i in rows:
            if pwd_context.verify(user_test, i.Adm_User) == True:
                mnu.windowRegisterError(window)
                return True
        user = pwd_context.hash(field1.get())
        password = pwd_context.hash(field2.get())
        try:
            command = f"""INSERT INTO LOG_ADM (Adm_User, Password_Adm) VALUES('{user}', '{password}');"""
            cursor.execute(command)
            cursor.commit()
            label_ok =Label(window, text="Ok", font="Stylus", background="#66B2FF", foreground="#56F037")
            label_ok.place(x=600, y=620, width=300, height=50)
        except:
            label_ok =Label(window, text="Register Adm Error", font="Stylus", background="#66B2FF", foreground="#FF0000")
            label_ok.place(x=600, y=620, width=300, height=50)
        window.destroy()
            

class CLIENT:


    def __init__(self):
        self.__cpf = ""
        self.__name_client = ""
        self.__phone_number = ""


    def registerClient(self, cpf, name, phone, connect, window):
        self.__cpf = cpf.get()
        self.__name_client = name.get()
        self.__phone_number = phone.get()

        confirmation = insertClient(connect, self.__cpf, self.__name_client, self.__phone_number)

        if confirmation == True:
            ok_window = Tk()
            ok_window.geometry("300x200")
            messagebox.showinfo(title='Register Client', message='registration completed')
            window.destroy()
            ok_window.destroy()
            self.__cpf = ""
            self.__name_client = ""
            self.__phone_number = ""
            return True
        elif confirmation == False:
            error_window = Tk()
            error_window.geometry("300x200")
            messagebox.showinfo(title='Register Client', message='registration error')
            window.destroy()
            error_window.destroy()
            self.__cpf = ""
            self.__name_client = ""
            self.__phone_number = ""
            return False


    def editClient(self, cpf, name, phone, connect, window):
        self.__cpf = cpf.get()
        self.__name_client = name.get()
        self.__phone_number = phone.get()

        confirmation = updateClient(connect, self.__cpf, self.__name_client, self.__phone_number)
        
        if confirmation == True:
            ok_window = Tk()
            ok_window.geometry("300x200")
            messagebox.showinfo(title='Edit Client', message='edition completed')
            window.destroy()
            ok_window.destroy()
            self.__cpf = ""
            self.__name_client = ""
            self.__phone_number = ""
            return True
        elif confirmation == False:
            error_window = Tk()
            error_window.geometry("300x200")
            messagebox.showinfo(title='Edit Client', message='edit error')
            window.destroy()
            error_window.destroy()
            self.__cpf = ""
            self.__name_client = ""
            self.__phone_number = ""
            return False

    
    def deleteClients(self, cpf, connect, window):
        self.__cpf = cpf.get()

        confirmation = deleteClient(connect, self.__cpf)

        if confirmation == True:
            ok_window = Tk()
            ok_window.geometry("300x200")
            messagebox.showinfo(title='Delete Client', message='Client deleted')
            window.destroy()
            ok_window.destroy()
            self.__cpf = ""
            self.__name_client = ""
            self.__phone_number = ""
            return True
        elif confirmation == False:
            error_window = Tk()
            error_window.geometry("300x200")
            messagebox.showinfo(title='Delete Client', message='delete error')
            window.destroy()
            error_window.destroy()
            self.__cpf = ""
            self.__name_client = ""
            self.__phone_number = ""
            return False
    
    
    def select2(self, tv, connect):
        tv.delete(*tv.get_children())
        command = "SELECT Name_Client, Phone_Number FROM CLIENT ORDER BY Name_Client;"
        cursor = connect.cursor()
        cursor.execute(command)
        res = cursor.fetchall()
        
        for i in res:
            tv.insert('', 'end', values=list(i))


class LOAN:

    def __init__(self):
        self.__cpf = ""
        self.__book1 = ""
        self.__book2 = ""
        self.__book3 = ""
        self.__loanDate = ""
        self.__devolutionDate = ""
        

    def registerLoan(self, connect, window, cpf, book1, book2, book3, date1, date2):
        pwd_context = CryptContext(schemes="sha256_crypt")
        
        cpf_test = cpf.get()
        cursor = connect.cursor()
        command = f"""SELECT * FROM CLIENT;"""
        cursor.execute(command)
        rows = cursor.fetchall()
        for i in rows:
            if pwd_context.verify(cpf_test, i.cpf) == True:
                self.__cpf = i.cpf
                self.__book1 = book1.get()
                self.__book2 = book2.get()
                self.__book3 = book3.get()
                self.__loanDate = date1.get_date()
                self.__devolutionDate = date2.get_date()
                commandx = f"""SELECT * FROM LOAN WHERE status_loan = 'PENDENCY';"""
                cursor.execute(commandx)
                aux = cursor.fetchall()
                for j in aux:
                    if self.__cpf == j.cpf:
                        error_window = Tk()
                        error_window.geometry("300x200")
                        messagebox.showinfo(title='Register Loan', message='register error')
                        self.__cpf = ""
                        self.__book1 = ""
                        self.__book2 = ""
                        self.__book3 = ""
                        self.__loanDate = ""
                        self.__devolutionDate = ""
                        window.destroy()
                        error_window.destroy()
                        return False    
                commandy = f"""SELECT * FROM LOAN;"""
                cursor.execute(commandy)
                aux = cursor.fetchall()
                for j in aux:
                    if self.__cpf == j.cpf:
                        error_window = Tk()
                        error_window.geometry("300x200")
                        messagebox.showinfo(title='Register Loan', message='register error')
                        self.__cpf = ""
                        self.__book1 = ""
                        self.__book2 = ""
                        self.__book3 = ""
                        self.__loanDate = ""
                        self.__devolutionDate = ""
                        window.destroy()
                        error_window.destroy()
                        return False 
                if self.__book1 == "" and self.__book2 == "" and self.__book3 == "":
                        error_window = Tk()
                        error_window.geometry("300x200")
                        messagebox.showinfo(title='Register Loan', message='register error')
                        self.__cpf = ""
                        self.__book1 = ""
                        self.__book2 = ""
                        self.__book3 = ""
                        self.__loanDate = ""
                        self.__devolutionDate = ""
                        window.destroy()
                        error_window.destroy()
                        return False
                if self.__book1 != "":
                    command = f"""SELECT * FROM BOOKS 
                              WHERE ID = {self.__book1};"""
                    cursor.execute(command)
                    row = cursor.fetchall()
                    for i in row:
                        if i.Quantity_Book == 0:
                            error_window = Tk()
                            error_window.geometry("300x200")
                            messagebox.showinfo(title='Register Loan', message='register error')
                            self.__cpf = ""
                            self.__book1 = ""
                            self.__book2 = ""
                            self.__book3 = ""
                            self.__loanDate = ""
                            self.__devolutionDate = ""
                            window.destroy()
                            error_window.destroy()
                            return False
                
                if self.__book2 != "":
                    command2 = f"""SELECT * FROM BOOKS 
                              WHERE ID = {self.__book2};"""
                    cursor.execute(command2)
                    row = cursor.fetchall()
                    for i in row:
                        if i.Quantity_Book == 0:
                            error_window = Tk()
                            error_window.geometry("300x200")
                            messagebox.showinfo(title='Register Loan', message='register error')
                            self.__cpf = ""
                            self.__book1 = ""
                            self.__book2 = ""
                            self.__book3 = ""
                            self.__loanDate = ""
                            self.__devolutionDate = ""
                            window.destroy()
                            error_window.destroy()
                            return False    
                
                if self.__book3 != "":
                    command3 = f"""SELECT * FROM BOOKS 
                              WHERE ID = {self.__book3};"""
                    cursor.execute(command3)
                    row = cursor.fetchall()
                    for i in row:
                        if i.Quantity_Book == 0:
                            error_window = Tk()
                            error_window.geometry("300x200")
                            messagebox.showinfo(title='Register Loan', message='register error')
                            self.__cpf = ""
                            self.__book1 = ""
                            self.__book2 = ""
                            self.__book3 = ""
                            self.__loanDate = ""
                            self.__devolutionDate = ""
                            window.destroy()
                            error_window.destroy()
                            return False
                
                if self.__book1 == self.__book2  or self.__book1 == self.__book3  or self.__book3 == self.__book2:
                    if self.__book1 != "" and self.__book2 != "" or self.__book2 != "" and self.__book3 != "" or self.__book1 != "" and self.__book3 != "":
                        error_window = Tk()
                        error_window.geometry("300x200")
                        messagebox.showinfo(title='Register Loan', message='register error')
                        self.__cpf = ""
                        self.__book1 = ""
                        self.__book2 = ""
                        self.__book3 = ""
                        self.__loanDate = ""
                        self.__devolutionDate = ""
                        window.destroy()
                        error_window.destroy()
                        return False
            

                command = f"""INSERT INTO LOAN (cpf, loan_date, devolution_date) VALUES('{self.__cpf}', CAST('{self.__loanDate}' AS DATE), CAST('{self.__devolutionDate}' AS DATE));
                              UPDATE LOAN SET status_loan = 'OPEN' WHERE cpf = '{self.__cpf}';"""
                cursor.execute(command)
                cursor.commit()
                
                command2 = f"""SELECT * FROM LOAN;"""
                cursor.execute(command2)
                rows = cursor.fetchall()
                for i in rows:
                    if self.__cpf == i.cpf:
                        Cod = i.Cod
                if self.__book1 != "" and self.__book2 != "" and self.__book3 != "":
                    command3 = f"""INSERT INTO ITEM (Cod, ID) VALUES({Cod}, {self.__book1});
                                   INSERT INTO ITEM (Cod, ID) VALUES({Cod}, {self.__book2});
                                   INSERT INTO ITEM (Cod, ID) VALUES({Cod}, {self.__book3});"""
                    cursor.execute(command3)
                    cursor.commit()

                    command = f"""UPDATE BOOKS SET Quantity_Book = Quantity_Book - 1 WHERE ID = {self.__book1} OR ID = {self.__book2} OR ID = {self.__book3};"""
                    cursor.execute(command)
                    cursor.commit()
                elif self.__book1 != "" and self.__book2 == "" and self.__book3 == "":
                    command3 = f"""INSERT INTO ITEM (Cod, ID) VALUES ({Cod}, {self.__book1});"""
                            
                    cursor.execute(command3)
                    cursor.commit()

                    command = f"""UPDATE BOOKS SET Quantity_Book = Quantity_Book - 1 WHERE ID = {self.__book1};"""
                    cursor.execute(command)
                    cursor.commit()
                elif self.__book1 != "" and self.__book2 != "" and self.__book3 == "":
                    command3 = f"""INSERT INTO ITEM (Cod, ID) VALUES ({Cod}, {self.__book1});
                            INSERT INTO ITEM (Cod, ID) VALUES ({Cod}, {self.__book2});
                            """
                    cursor.execute(command3)
                    cursor.commit()

                    command = f"""UPDATE BOOKS SET Quantity_Book = Quantity_Book - 1 WHERE ID = {self.__book1} OR ID = {self.__book2};"""
                    cursor.execute(command)
                    cursor.commit()
                elif self.__book1 == "" and self.__book2 != "" and self.__book3 != "":
                    command3 = f"""INSERT INTO ITEM (Cod, ID) VALUES ({Cod}, {self.__book2});
                            INSERT INTO ITEM (Cod, ID) VALUES ({Cod}, {self.__book3});
                            """
                    cursor.execute(command3)
                    cursor.commit()

                    command = f"""UPDATE BOOKS SET Quantity_Book = Quantity_Book - 1 WHERE ID = {self.__book2} OR ID = {self.__book3};"""
                    cursor.execute(command)
                    cursor.commit()
                elif self.__book1 != "" and self.__book2 == "" and self.__book3 != "":
                    command3 = f"""INSERT INTO ITEM (Cod, ID) VALUES ({Cod}, {self.__book1});
                            INSERT INTO ITEM (Cod, ID) VALUES ({Cod}, {self.__book3});
                            """
                    cursor.execute(command3)
                    cursor.commit()

                    command = f"""UPDATE BOOKS SET Quantity_Book = Quantity_Book - 1 WHERE ID = {self.__book1} OR ID = {self.__book3};"""
                    cursor.execute(command)
                    cursor.commit()
                elif self.__book1 == "" and self.__book2 != "" and self.__book3 == "":
                    command3 = f"""INSERT INTO ITEM (Cod, ID) VALUES ({Cod}, {self.__book2});
                            
                            """
                    cursor.execute(command3)
                    cursor.commit()

                    command = f"""UPDATE BOOKS SET Quantity_Book = Quantity_Book - 1 WHERE ID = {self.__book2};"""
                    cursor.execute(command)
                    cursor.commit()
                elif self.__book1 == "" and self.__book2 == "" and self.__book3 != "":
                    command3 = f"""INSERT INTO ITEM (Cod, ID) VALUES ({Cod}, {self.__book3});
                            
                            """
                    cursor.execute(command3)
                    cursor.commit()

                    command = f"""UPDATE BOOKS SET Quantity_Book = Quantity_Book - 1 WHERE ID = {self.__book3};"""
                    cursor.execute(command)
                    cursor.commit()
                
                
                ok_window = Tk()
                ok_window.geometry("300x200")
                messagebox.showinfo(title="Register Loan", message="Registration completed")
                self.__cpf = ""
                self.__book1 = ""
                self.__book2 = ""
                self.__book3 = ""
                self.__loanDate = ""
                self.__devolutionDate = ""
                window.destroy()
                ok_window.destroy()
                return True
                
                
        error_window = Tk()
        error_window.geometry("300x200")
        messagebox.showinfo(title='Register Loan', message='cpf error')
        self.__cpf = ""
        self.__book1 = ""
        self.__book2 = ""
        self.__book3 = ""
        self.__loanDate = ""
        self.__devolutionDate = ""
        window.destroy()
        error_window.destroy()
        return False 



    def edtLoan(self, Cod, status, connect, window):
        codeLoan = int(Cod.get())
        command = f"""SELECT * FROM LOAN;"""
        cursor = connect.cursor()
        cursor.execute(command)
        rows = cursor.fetchall()
        
        for i in rows:
            
            if int(Cod.get()) == i.Cod:
                command2 = f"""UPDATE LOAN SET status_loan = '{status}' WHERE Cod = {codeLoan};"""
                cursor.execute(command2)
                cursor.commit()
                   
                    
                if i.status_loan == 'PENDENCY' and status != 'CLOSE':
                    ok_window = Tk()
                    ok_window.geometry("300x200")
                    messagebox.showinfo(title="Edit Loan", message="Edit completed")
                    ok_window.destroy()
                    window.destroy()
                    return True
                
                if i.status_loan == 'CLOSE':
                    command3 = f"""UPDATE LOAN SET status_loan = '{status}' WHERE Cod = {codeLoan};"""
                    cursor.execute(command3)
                    cursor.commit()

                    command4 = f"""SELECT * FROM ITEM;"""
                    cursor.execute(command4)
                    rows = cursor.fetchall()
                    for i in rows:
                        if codeLoan == i.Cod:
                            command5 = f"""UPDATE BOOKS SET Quantity_Book = Quantity_Book + 1 WHERE ID = {i.Id};"""
                            cursor.execute(command5)
                            cursor.commit()
                    command6= f"""DELETE FROM ITEM WHERE Cod = {codeLoan};
                                  DELETE FROM LOAN WHERE Cod = {codeLoan};"""
                    cursor.execute(command6)
                    cursor.commit()
                    ok_window = Tk()
                    ok_window.geometry("300x200")
                    messagebox.showinfo(title="Edit Loan", message="Edit completed")
                    ok_window.destroy()
                    window.destroy()
                    return True
        
        error_window = Tk()
        error_window.geometry("300x200")
        messagebox.showinfo(title="Edit Loan", message="Edit error")
        error_window.destroy()
        return False
                    
    def select3(self, tv, connect):
        tv.delete(*tv.get_children())
        command = "SELECT Cod, loan_date, devolution_date, status_loan FROM LOAN ORDER BY Cod;"
        cursor = connect.cursor()
        cursor.execute(command)
        res = cursor.fetchall()
        
        for i in res:
            tv.insert('', 'end', values=list(i))    
     
    def select4(self, tv, connect):
        tv.delete(*tv.get_children())
        command = "SELECT Cod, loan_date, devolution_date, status_loan FROM LOAN WHERE status_loan = 'PENDENCY' ORDER BY Cod;"
        cursor = connect.cursor()
        cursor.execute(command)
        res = cursor.fetchall()
        
        for i in res:
            tv.insert('', 'end', values=list(i))







