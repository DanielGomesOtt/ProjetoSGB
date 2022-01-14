from calendar import month
from distutils import command
from Library import *
from SQLConnect import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
from maskedentry import MaskedWidget


class Menu:


    def __init__(self):
        pass

        
    def menuLogin(self):
        login_window = Tk()
        varBar = DoubleVar()
        varBar.set(0)

        login_window.title("Login")
        login_window.geometry("1900x1080")
        login_window.configure(background="#606060")
        label_login = Label(login_window, text="Login", font="Arial 40", background="#606060", foreground="#FFFFFF")
        label_login.place(x=750, y=200, width=500, height=100)

        label_user = Label(login_window, text="User: ", font="Arial", background="#606060", foreground="#FFFFFF")
        label_user.place(x=678, y=340, width=100, height=25)
        user_field = Entry(font="Stylus 20")
        user_field.place(x=700, y=370, width=600, height= 50)

        hide_password = StringVar()
        label_password = Label(login_window, text="Password: ", font="Arial", background="#606060", foreground="#FFFFFF")
        label_password.place(x=702, y=450, width=100, height=25)
        password_field = Entry(font="Stylus 20", textvariable=hide_password, show="*")
        password_field.place(x=700, y=480, width=600, height=50)
        
        admin = ADM()
        connect = sgbConnect()
        mnu = Menu()
        login_btn = Button(login_window, text="Enter", font="Stylus", background="#404040", foreground="#FFFFFF", relief="sunken", command=lambda:self.progressBar(varBar, login_window, admin, user_field, password_field, connect, mnu))
        login_btn.place(x=1075, y=560, width=200, height=50)

        register_btn = Button(login_window, text="New Admin", font="Stylus", background="#404040", foreground="#FFFFFF", relief="sunken", command=lambda:Menu.addAdmin(connect))
        register_btn.place(x=725, y=560, width=200, height=50)
        
        pb = ttk.Progressbar(login_window, variable=varBar, maximum=100)
        pb.place(x=700, y=700, width=600, height=50)
        login_window.mainloop()
    
    
    def progressBar(self, pb, window, admin, user_field, password_field, connect, mnu):
        cont = 0
        parts = 10000/100
        while cont < parts:
            cont = cont + 1
            i = 0
            while i < 1000000:
                i = i + 1
            pb.set(cont)
            window.update()
        admin.login(user_field, password_field, window, connect, mnu, pb)

    
    def loginError(self, pb):
        pb.set(0)
        error_window = Tk()
        error_window.geometry("300x200")
        messagebox.showinfo(title='Login Error', message='invalid username or password')
        error_window.destroy()
        error_window.mainloop()

    
    def menu(self, window, connect):
        mnu = Menu()
        window.destroy()
        menu_window = Tk()
        menu_window.title("Library Management System")
        menu_window.geometry("1900x1080")
        menu_window.configure(background="#606060")

        first_label = Label(menu_window, text= "Menu", font="Stylus 25", background="#404040", foreground="#FFFFFF")
        first_label.place(x=0, y=0, width=1920, height=50)
        
        categories_label1 = Label(menu_window, text="Books", font="Stylus 22", background="#606060", foreground="#FFFFFF")
        categories_label1.place(x=150, y=300, width=300, height=50)

        btn_register = Button(menu_window, text="Register Book", font="Stylus", background="#404040", foreground="#FFFFFF", command=lambda:self.registerBook(connect))
        btn_register.place(x=175, y=375, width=250, height=50)
        
        btn_view = Button(menu_window, text="Book Viewing", font="Stylus", background="#404040", foreground="#FFFFFF", command=lambda:self.bookView(connect))
        btn_view.place(x=175, y=450, width=250, height=50)

        btn_update = Button(menu_window, text="Update Book", font="Stylus", background="#404040", foreground="#FFFFFF", command=lambda:self.updateBook(connect))
        btn_update.place(x=175, y=525, width=250, height=50)

        btn_delete = Button(menu_window, text="Delete Book", font="Stylus", background="#404040", foreground="#FFFFFF", command=lambda:self.deleteBook(connect))
        btn_delete.place(x=175, y=600, width=250, height=50)

        btn_addexist = Button(menu_window, text="Add to Stock", font="Stylus", background="#404040", foreground="#FFFFFF", command=lambda:self.addBook(connect))
        btn_addexist.place(x=175, y=675, width=250, height=50)
        

        categories_label2 = Label(menu_window, text="Clients", font="Stylus 22", background="#606060", foreground="#FFFFFF")
        categories_label2.place(x=800, y=300, width=300, height=50)

        btn_regClient = Button(menu_window, text="Register Client", font="Stylus", background="#404040", foreground="#FFFFFF", command=lambda:self.regClient(connect))
        btn_regClient.place(x=825, y=375, width=250, height=50)

        btn_editClient = Button(menu_window, text="Edit Client", font="Sytlus", background="#404040", foreground="#FFFFFF", command=lambda:self.uptClient(connect))
        btn_editClient.place(x=825, y=450, width=250, height=50)

        btn_delClient = Button(menu_window, text="Delete Client", font="Stylus", background="#404040", foreground="#FFFFFF", command=lambda:self.dltClient(connect))
        btn_delClient.place(x=825, y=525, width=250, height=50)
        
        btn_viewClient = Button(menu_window, text="Client Viewing", font="Stylus", background="#404040", foreground="#FFFFFF", command=lambda:self.vwClient(connect))
        btn_viewClient.place(x=825, y=600, width=250, height=50)

        categories_label3 = Label(menu_window, text="Loans", font="Stylus 22", background="#606060", foreground="#FFFFFF")
        categories_label3.place(x=1450, y=300, width=300, height = 50)

        btn_regloan = Button(menu_window, text="Register Loan", font="Stylus", background="#404040", foreground="#FFFFFF", command=lambda:self.regLoan(connect))
        btn_regloan.place(x=1475, y=375, width=250, height=50)

        btn_editloan = Button(menu_window, text="Edit Loan", font="Sytlus", background="#404040", foreground="#FFFFFF", command=lambda:self.editLoan(connect))
        btn_editloan.place(x=1475, y=450, width=250, height=50)

        btn_vwloan = Button(menu_window, text="Loan Viewing", font="Stylus", background="#404040", foreground="#FFFFFF", command= lambda:self.vwLoan(connect))
        btn_vwloan.place(x=1475, y=525, width=250, height=50)

        btn_exit = Button(menu_window, text="Disconnect", font="Stylus", background="#CD1010", foreground="#FFFFFF", command=lambda:sgbDisconnection1(connect, menu_window, mnu))
        btn_exit.place(x=1725, y=0, width=200, height=50)


        btn_vwPendency = Button(menu_window, text="Pendency viewing", font="Stylus", background="#404040", foreground="#FFFFFF", command=lambda:self.vwPendency(connect))
        btn_vwPendency.place(x=1475, y=600, width=250, height=50)
        menu_window.mainloop()


    def addAdmin(connect, *args):
        add_window = Tk()
        add_window.title("Register Admin")
        add_window.geometry("1900x1080")
        add_window.configure(background="#606060")

        label_register = Label(add_window, text="Register Admin", font="Arial 40", background="#606060", foreground="#FFFFFF")
        label_register.place(x=750, y=200, width=500, height=100)

        label_user = Label(add_window, text="User: ", font="Arial", background="#606060", foreground="#FFFFFF")
        label_user.place(x=678, y=340, width=100, height=25)
        
        user = Entry(add_window, font="Stylus 20")
        user.place(x=700, y=370, width=600, height= 50)

        hide_password = StringVar()
        label_password = Label(add_window, text="Password: ", font="Arial", background="#606060", foreground="#FFFFFF")
        label_password.place(x=702, y=450, width=100, height=25)
        
        password = Entry(add_window, font="Stylus 20", textvariable=hide_password, show="*")
        password.place(x=700, y=480, width=600, height=50)

        admin = ADM()
        mnu = Menu()
        register_btn = Button(add_window, text="Enter", font="Stylus", background="#404040", foreground="#FFFFFF", relief="sunken", command=lambda:admin.register_adm(user, password, add_window, connect, mnu))
        register_btn.place(x=1075, y=560, width=200, height=50)

        btn_exit = Button(add_window, text="Exit", font="Stylus", background="#CD1010", foreground="#FFFFFF", command=lambda:sgbDisconnection(connect, add_window, mnu))
        btn_exit.place(x=1725, y=0, width=200, height=50)
        add_window.mainloop()




    def windowRegisterError(self, window):
        error_window = Tk()
        error_window.geometry("300x200")
        messagebox.showinfo(title='Register Error', message='admin already registered')
        window.destroy()
        error_window.destroy()
        

    def registerBook(self, connect):
        mnu = Menu()
        reg = BOOKS()
        register_window = Tk()
        register_window.geometry("1900x1080")
        register_window.title("Library Management System")
        register_window.configure(background="#606060")

        label_window = Label(register_window, text="Register Book", font="Stylus 25", background="#404040", foreground="#FFFFFF")
        label_window.place(x=0, y=0, width=1920, height=50)

        field_title = Entry(register_window, font="Stylus 16")
        field_title.place(x = 100, y = 150, width=500, height=50)

        label_title = Label(register_window, text="Title:", font="Stylus", background="#606060", foreground="#FFFFFF")
        label_title.place(x = 70, y=115, width=100, height=20)

        field_author = Entry(register_window, font="Stylus 16")
        field_author.place(x = 100, y = 255, width=500, height=50)

        label_author = Label(register_window, text="Author:", font="Stylus", background="#606060", foreground="#FFFFFF")
        label_author.place(x = 80, y=220, width=100, height=20)

        field_publisher = Entry(register_window, font="Stylus 16")
        field_publisher.place(x = 100, y = 360, width=500, height=50)

        label_publisher = Label(register_window, text="Publisher:", font="Stylus", background="#606060", foreground="#FFFFFF")
        label_publisher.place(x = 95, y=325, width=100, height=20)

        field_pages = Entry(register_window, font="Stylus 16")
        field_pages.place(x = 100, y = 465, width=500, height=50)

        label_pages = Label(register_window, text="Number of Pages:", font="Stylus", background="#606060", foreground="#FFFFFF")
        label_pages.place(x = 85, y=430, width=200, height=20)

        field_genre = Entry(register_window, font="Stylus 16")
        field_genre.place(x = 100, y = 570, width=500, height=50)

        label_genre = Label(register_window, text="Genre:", font="Stylus", background="#606060", foreground="#FFFFFF")
        label_genre.place(x = 80, y=535, width=100, height=20)

        label_date = Label(register_window, text = "Publication date:",font="Stylus",  background="#606060", foreground="#FFFFFF")
        label_date.place(x = 927, y = 110, width = 500, height= 50)

        cal = Calendar(register_window, selectmode = "day")
        cal.place(x= 1100, y = 155, width=500)

        label_quantity = Label(register_window, text="Quantity of Books:", font="Stylus", background="#606060", foreground="#FFFFFF")
        label_quantity.place(x = 938, y = 465, width = 500, height = 50)

        spin_quantity = Spinbox(register_window, from_= 1, to = 10000, font="Stylus 20")
        spin_quantity.place(x = 1100, y = 510, width = 500, height = 50)

        btn_register = Button(register_window, text="OK", font="Stylus", background="#404040", foreground="#FFFFFF", command=lambda:reg.register(field_title, field_author, field_publisher, field_pages, field_genre, cal, spin_quantity, register_window, connect))
        btn_register.place(x = 775, y = 800, width= 200, height = 50)

        btn_exit = Button(register_window, text="Exit", font="Stylus", background="#CD1010", foreground="#FFFFFF", command=lambda:sgbDisconnection(connect, register_window, mnu))
        btn_exit.place(x=1725, y=0, width=200, height=50)

        register_window.mainloop()


    def bookView(self, connect):
        mnu = Menu()
        view = BOOKS()
        view_window = Tk()
        view_window.geometry("1900x1080")
        view_window.configure(background="#606060")
        view_window.title("Library Management System")

        label_window = Label(view_window, text="List of Books", font="Stylus 25", background="#404040", foreground="#FFFFFF")
        label_window.place(x=0, y=0, width=1920, height=50)
        
        columns = ("ID", "Title", "Author", "Publisher", "Number of Pages", "Genre", "Publication Date", "Quantity of Books")
        tree = ttk.Treeview(view_window, columns=columns, show="headings")
        tree.place(x=100, y=150, width=1700, height=800)

        tree.heading("ID", text="ID")
        tree.heading("Title", text="Title")
        tree.heading("Author", text="Authour")
        tree.heading("Publisher", text="Publisher")
        tree.heading("Number of Pages", text="Number of Pages")
        tree.heading("Genre", text="Genre")
        tree.heading("Publication Date", text="Publication Date")
        tree.heading("Quantity of Books", text="Quantity of Books")

        scrollbar = ttk.Scrollbar(
        view_window,
        orient='vertical',
        command=tree.yview
        )
        scrollbar.place(x=1801, y=150, height=800)
        

        view.select(tree, connect)

        btn_exit = Button(view_window, text="Exit", font="Stylus", background="#CD1010", foreground="#FFFFFF", command=lambda:sgbDisconnection(connect, view_window, mnu))
        btn_exit.place(x=1725, y=0, width=200, height=50)

        view_window.mainloop()
    

    def updateBook(self, connect):
        mnu = Menu()
        upt = BOOKS()
        update_window = Tk()
        update_window.geometry("1900x1080")
        update_window.title("Library Management System")
        update_window.configure(background="#606060")

        label_window = Label(update_window, text="Update Book", font="Stylus 25", background="#404040", foreground="#FFFFFF")
        label_window.place(x=0, y=0, width=1920, height=50)

        field_id = Entry(update_window, font="Stylus 16")
        field_id.place(x = 100, y = 185, width=500, height=25)
        
        label_id = Label(update_window, text="Id:", font="Stylus", background="#606060", foreground="#FFFFFF")
        label_id.place(x = 70, y=150, width=100, height=20)
        
        
        field_title = Entry(update_window, font="Stylus 16")
        field_title.place(x = 100, y = 255, width=500, height=50)

        label_title = Label(update_window, text="Title:", font="Stylus", background="#606060", foreground="#FFFFFF")
        label_title.place(x = 70, y=220, width=100, height=20)

        field_author = Entry(update_window, font="Stylus 16")
        field_author.place(x = 100, y = 360, width=500, height=50)

        label_author = Label(update_window, text="Author:", font="Stylus", background="#606060", foreground="#FFFFFF")
        label_author.place(x = 80, y=325, width=100, height=20)

        field_publisher = Entry(update_window, font="Stylus 16")
        field_publisher.place(x = 100, y = 465, width=500, height=50)

        label_publisher = Label(update_window, text="Publisher:", font="Stylus", background="#606060", foreground="#FFFFFF")
        label_publisher.place(x = 95, y=430, width=100, height=20)

        field_pages = Entry(update_window, font="Stylus 16")
        field_pages.place(x = 100, y = 570, width=500, height=50)

        label_pages = Label(update_window, text="Number of Pages:", font="Stylus", background="#606060", foreground="#FFFFFF")
        label_pages.place(x = 85, y=535, width=200, height=20)

        field_genre = Entry(update_window, font="Stylus 16")
        field_genre.place(x = 100, y = 675, width=500, height=50)

        label_genre = Label(update_window, text="Genre:", font="Stylus", background="#606060", foreground="#FFFFFF")
        label_genre.place(x = 80, y=640, width=100, height=20)

        label_date = Label(update_window, text = "Publication date:",font="Stylus",  background="#606060", foreground="#FFFFFF")
        label_date.place(x = 927, y = 110, width = 500, height= 50)

        cal = Calendar(update_window, selectmode = "day")
        cal.place(x= 1100, y = 155, width=500)

        label_quantity = Label(update_window, text="Quantity of Books:", font="Stylus", background="#606060", foreground="#FFFFFF")
        label_quantity.place(x = 938, y = 465, width = 500, height = 50)

        spin_quantity = Spinbox(update_window, from_= 1, to = 10000, font="Stylus 20")
        spin_quantity.place(x = 1100, y = 510, width = 500, height = 50)

        btn_update = Button(update_window, text="OK", font="Stylus", background="#404040", foreground="#FFFFFF", command=lambda:upt.update(field_id, field_title, field_author, field_publisher, field_pages, field_genre, cal, spin_quantity, connect, update_window))
        btn_update.place(x = 860, y = 800, width= 200, height = 50)

        btn_exit = Button(update_window, text="Exit", font="Stylus", background="#CD1010", foreground="#FFFFFF", command=lambda:sgbDisconnection(connect, update_window, mnu))
        btn_exit.place(x=1725, y=0, width=200, height=50)

        update_window.mainloop()


    def deleteBook(self, connect):
        mnu = Menu()
        dlt = BOOKS()
        delete_window = Tk()
        delete_window.configure(background="#606060")
        delete_window.geometry("1900x1080")
        delete_window.title("Library Management System")
        label_window = Label(delete_window, text="Delete Book", font="Stylus 25", background="#404040", foreground="#FFFFFF")
        label_window.place(x=0, y=0, width=1920, height=50)

        label_id = Label(delete_window, text="Book id: ", font="Arial", background="#606060", foreground="#FFFFFF")
        label_id.place(x=645, y=340, width=100, height=25)
        id_field = Entry(delete_window, font="Stylus 20")
        id_field.place(x=650, y=370, width=600, height= 50)

        btn_delete = Button(delete_window, text="delete", font="Stylus", background="#404040", foreground="#FFFFFF", command=lambda:dlt.delete(id_field, connect, delete_window))
        btn_delete.place(x = 850, y = 450, width= 200, height = 50)
        
        btn_exit = Button(delete_window, text="Exit", font="Stylus", background="#CD1010", foreground="#FFFFFF", command=lambda:sgbDisconnection(connect, delete_window, mnu))
        btn_exit.place(x=1725, y=0, width=200, height=50)
        delete_window.mainloop()

    
    def addBook(self, connect):
        mnu = Menu()
        add = BOOKS()
        add_window = Tk()
        add_window.configure(background="#606060")
        add_window.geometry("1900x1080")
        add_window.title("Library Management System")
        label_window = Label(add_window, text="Add to stock", font="Stylus 25", background="#404040", foreground="#FFFFFF")
        label_window.place(x=0, y=0, width=1920, height=50)

        label_id = Label(add_window, text="Book id: ", font="Arial", background="#606060", foreground="#FFFFFF")
        label_id.place(x=645, y=340, width=100, height=25)
        id_field = Entry(add_window, font="Stylus 20")
        id_field.place(x=650, y=370, width=600, height= 50)


        label_quantity = Label(add_window, text="Quantity of Books:", font="Stylus", background="#606060", foreground="#FFFFFF")
        label_quantity.place(x = 490, y = 500, width = 500, height = 50)

        spin_quantity = Spinbox(add_window, from_= 1, to = 10000, font="Stylus 20")
        spin_quantity.place(x = 650, y = 550, width = 500, height = 50)


        btn_add = Button(add_window, text="Add", font="Stylus", background="#404040", foreground="#FFFFFF", command=lambda:add.plus_Book(id_field, spin_quantity, connect, add_window))
        btn_add.place(x = 850, y = 700, width= 200, height = 50)
        
        btn_exit = Button(add_window, text="Exit", font="Stylus", background="#CD1010", foreground="#FFFFFF", command=lambda:sgbDisconnection(connect, add_window, mnu))
        btn_exit.place(x=1725, y=0, width=200, height=50)
        add_window.mainloop()


    def regClient(self, connect):
        mnu = Menu()
        reg = CLIENT()
        register_window = Tk()
        register_window.geometry("1900x1080")
        register_window.title("Library Management System")
        register_window.configure(background="#606060")

        label_window = Label(register_window, text="Register Client", font="Stylus 25", background="#404040", foreground="#FFFFFF")
        label_window.place(x=0, y=0, width=1920, height=50)

        label_cpf = Label(register_window, text="CPF:", font="Arial", background="#606060", foreground="#FFFFFF")
        label_cpf.place(x=678, y=340, width=100, height=25)
        cpf_field = MaskedWidget(register_window, 'fixed', mask="999.999.999-99", font="Stylus 16")
        cpf_field.place(x=700, y=370, width=600, height= 50)

        label_name = Label(register_window, text="Name: ", font="Arial", background="#606060", foreground="#FFFFFF")
        label_name.place(x=692, y=450, width=100, height=25)
        name_field = Entry(register_window, font="Stylus 16")
        name_field.place(x=700, y=480, width=600, height=50)
        
        label_number = Label(register_window, text="Phone Number: ", font="Arial", background="#606060", foreground="#FFFFFF")
        label_number.place(x=682, y=560, width=200, height=25)
        number_field = MaskedWidget(register_window, 'fixed', mask="+XX (XX)XXXXX-XXXX", font="Stylus 16")
        number_field.place(x=700, y=590, width=600, height=50)

        btn_regClient = Button(register_window, text="Register", font="Stylus", background="#404040", foreground="#FFFFFF", command=lambda:reg.registerClient(cpf_field, name_field, number_field, connect, register_window))
        btn_regClient.place(x=825, y=690, width=250, height=50)
        
        btn_exit = Button(register_window, text="Exit", font="Stylus", background="#CD1010", foreground="#FFFFFF", command=lambda:sgbDisconnection(connect, register_window, mnu))
        btn_exit.place(x=1725, y=0, width=200, height=50)
        register_window.mainloop()
        

    def uptClient(self, connect):
        mnu = Menu()
        upt = CLIENT()
        update_window = Tk()
        update_window.geometry("1900x1080")
        update_window.title("Library Management System")
        update_window.configure(background="#606060")

        label_window = Label(update_window, text="Edit Client", font="Stylus 25", background="#404040", foreground="#FFFFFF")
        label_window.place(x=0, y=0, width=1920, height=50)

        label_cpf = Label(update_window, text="CPF:", font="Arial", background="#606060", foreground="#FFFFFF")
        label_cpf.place(x=678, y=340, width=100, height=25)
        cpf_field = MaskedWidget(update_window, 'fixed', mask="999.999.999-99", font="Stylus 16")
        cpf_field.place(x=700, y=370, width=600, height= 50)

        label_name = Label(update_window, text="Name: ", font="Arial", background="#606060", foreground="#FFFFFF")
        label_name.place(x=692, y=450, width=100, height=25)
        name_field = Entry(update_window, font="Stylus 16")
        name_field.place(x=700, y=480, width=600, height=50)
        
        label_number = Label(update_window, text="Phone Number: ", font="Arial", background="#606060", foreground="#FFFFFF")
        label_number.place(x=682, y=560, width=200, height=25)
        number_field = MaskedWidget(update_window, 'fixed', mask="+XX (XX)XXXXX-XXXX", font="Stylus 16")
        number_field.place(x=700, y=590, width=600, height=50)

        btn_uptClient = Button(update_window, text="Edit", font="Stylus", background="#404040", foreground="#FFFFFF", command=lambda:upt.editClient(cpf_field, name_field, number_field, connect, update_window))
        btn_uptClient.place(x=825, y=690, width=250, height=50)
        
        btn_exit = Button(update_window, text="Exit", font="Stylus", background="#CD1010", foreground="#FFFFFF", command=lambda:sgbDisconnection(connect, update_window, mnu))
        btn_exit.place(x=1725, y=0, width=200, height=50)
        update_window.mainloop()

    
    def dltClient(self, connect):
        mnu = Menu()
        dlt = CLIENT()
        delete_window = Tk()
        delete_window.geometry("1900x1080")
        delete_window.title("Library Management System")
        delete_window.configure(background="#606060")

        label_window = Label(delete_window, text="Delete Client", font="Stylus 25", background="#404040", foreground="#FFFFFF")
        label_window.place(x=0, y=0, width=1920, height=50)

        label_cpf = Label(delete_window, text="CPF:", font="Arial", background="#606060", foreground="#FFFFFF")
        label_cpf.place(x=678, y=340, width=100, height=25)
        cpf_field = MaskedWidget(delete_window, 'fixed', mask="999.999.999-99", font="Stylus 16")
        cpf_field.place(x=700, y=370, width=600, height= 50)

        btn_dltClient = Button(delete_window, text="Delete", font="Stylus", background="#404040", foreground="#FFFFFF", command=lambda:dlt.deleteClients(cpf_field, connect, delete_window))
        btn_dltClient.place(x=850, y=690, width=250, height=50)

        btn_exit = Button(delete_window, text="Exit", font="Stylus", background="#CD1010", foreground="#FFFFFF", command=lambda:sgbDisconnection(connect, delete_window, mnu))
        btn_exit.place(x=1725, y=0, width=200, height=50)
        delete_window.mainloop()


    def vwClient(self, connect):
        mnu = Menu()
        view = CLIENT()
        view_window = Tk()
        view_window.geometry("1900x1080")
        view_window.configure(background="#606060")
        view_window.title("Library Management System")

        label_window = Label(view_window, text="List of Clients", font="Stylus 25", background="#404040", foreground="#FFFFFF")
        label_window.place(x=0, y=0, width=1920, height=50)
        
        columns = ("Name", "Phone Number")
        tree = ttk.Treeview(view_window, columns=columns, show="headings")
        tree.place(x=100, y=150, width=1700, height=800)

        tree.heading("Name", text="Name")
        tree.heading("Phone Number", text="Phone Number")

        scrollbar = ttk.Scrollbar(
        view_window,
        orient='vertical',
        command=tree.yview
        )
        scrollbar.place(x=1801, y=150, height=800)
        

        view.select2(tree, connect)
        btn_exit = Button(view_window, text="Exit", font="Stylus", background="#CD1010", foreground="#FFFFFF", command=lambda:sgbDisconnection(connect, view_window, mnu))
        btn_exit.place(x=1725, y=0, width=200, height=50)
        view_window.mainloop()


    def regLoan(self, connect):
        mnu = Menu()
        reg = LOAN()
        reg_window = Tk()
        reg_window.geometry("1900x1080")
        reg_window.title("Library Management System")
        reg_window.configure(background="#606060")

        label_window = Label(reg_window, text="Register Book Loan", font="Stylus 25", background="#404040", foreground="#FFFFFF")
        label_window.place(x=0, y=0, width=1920, height=50)

        field_cpf = MaskedWidget(reg_window, 'fixed', mask='999.999.999-99', font="Stylus 16")
        field_cpf.place(x = 100, y = 150, width=500, height=50)

        label_cpf = Label(reg_window, text="CPF:", font="Stylus", background="#606060", foreground="#FFFFFF")
        label_cpf.place(x = 70, y=115, width=100, height=20)

        field_book1 = Entry(reg_window, font="Stylus 16")
        field_book1.place(x = 100, y = 255, width=500, height=50)

        label_book = Label(reg_window, text="Cod_Book 1, 2, 3:", font="Stylus", background="#606060", foreground="#FFFFFF")
        label_book.place(x = 70, y=220, width=500, height=20)

        field_book2 = Entry(reg_window, font="Stylus 16")
        field_book2.place(x = 100, y = 360, width=500, height=50)

        field_book3 = Entry(reg_window, font="Stylus 16")
        field_book3.place(x = 100, y = 450, width=500, height=50)


        label_date = Label(reg_window, text = "Loan date:",font="Stylus", background="#606060", foreground="#FFFFFF")
        label_date.place(x = 100, y = 500, width = 500, height= 50)

        cal = Calendar(reg_window, selectmode = "day")
        cal.place(x= 100, y = 575, width=500)


        label_date2 = Label(reg_window, text= "Devolution Date", font="Stylus", background="#606060", foreground="#FFFFFF")
        label_date2.place(x=900, y=150, width=500, height=50)

        cal2 = Calendar(reg_window, selectmode = "day")
        cal2.place(x= 900, y = 225, width=500)

        btn_regloan = Button(reg_window, text="Register", font="Stylus", background="#404040", foreground="#FFFFFF", command=lambda:reg.registerLoan(connect, reg_window, field_cpf, field_book1, field_book2, field_book3, cal, cal2))
        btn_regloan.place(x=900, y=575, width=200, height=50)

        btn_exit = Button(reg_window, text="Exit", font="Stylus", background="#CD1010", foreground="#FFFFFF", command=lambda:sgbDisconnection(connect, reg_window, mnu))
        btn_exit.place(x=1725, y=0, width=200, height=50)
        reg_window.mainloop()
    

    def editLoan(self, connect):
        mnu = Menu()
        edt = LOAN()
        edt_window = Tk()
        edt_window.geometry("1900x1080")
        edt_window.title("Library Management System")
        edt_window.configure(background="#606060")

        label_window = Label(edt_window, text="Edit Book Loan", font="Stylus 25", background="#404040", foreground="#FFFFFF")
        label_window.place(x=0, y=0, width=1920, height=50)

        label_id = Label(edt_window, text="Cod_Loan", font="Stylus", background="#606060", foreground="#FFFFFF")
        label_id.place(x=875, y=250, width=200, height=25)
        
        field_Cod = Entry(edt_window, font="Stylus 16")
        field_Cod.place(x=875, y=275, width=200, height=25)
        
        sts = StringVar(edt_window)
        Radiobutton(edt_window, text="PENDENCY", variable=sts, value='PENDENCY').place(x=775, y=300, width=200, height=50)
        Radiobutton(edt_window, text="CLOSE", variable=sts, value='CLOSE').place(x=975, y=300, width=200, height=50)

        
        btn_edtloan = Button(edt_window, text="Edit", font="Stylus", background="#404040", foreground="#FFFFFF", command=lambda:edt.edtLoan(field_Cod, sts.get(), connect, edt_window))
        btn_edtloan.place(x=875, y=400, width=200, height=50)

        btn_exit = Button(edt_window, text="Exit", font="Stylus", background="#CD1010", foreground="#FFFFFF", command=lambda:sgbDisconnection(connect, edt_window, mnu))
        btn_exit.place(x=1725, y=0, width=200, height=50)
        edt_window.mainloop()


    def vwLoan(self, connect):
        mnu = Menu()
        view = LOAN()
        view_window = Tk()
        view_window.geometry("1900x1080")
        view_window.configure(background="#606060")
        view_window.title("Library Management System")

        label_window = Label(view_window, text="List of loans", font="Stylus 25", background="#404040", foreground="#FFFFFF")
        label_window.place(x=0, y=0, width=1920, height=50)
        
        columns = ("Cod", "Loan date", "Devolution date", "status")
        tree = ttk.Treeview(view_window, columns=columns, show="headings")
        tree.place(x=100, y=150, width=1700, height=800)

        tree.heading("Cod", text="Cod")
        tree.heading("Loan date", text="Loan date")
        tree.heading("Devolution date", text="Devolution date")
        tree.heading("status", text="status")

        scrollbar = ttk.Scrollbar(
        view_window,
        orient='vertical',
        command=tree.yview
        )
        scrollbar.place(x=1801, y=150, height=800)
        

        view.select3(tree, connect)

        btn_exit = Button(view_window, text="Exit", font="Stylus", background="#CD1010", foreground="#FFFFFF", command=lambda:sgbDisconnection(connect, view_window, mnu))
        btn_exit.place(x=1725, y=0, width=200, height=50)
        view_window.mainloop()
    
    
    def vwPendency(self, connect):
        mnu = Menu()
        view = LOAN()
        view_window = Tk()
        view_window.geometry("1900x1080")
        view_window.configure(background="#606060")
        view_window.title("Library Management System")

        label_window = Label(view_window, text="List of pendencies", font="Stylus 25", background="#404040", foreground="#FFFFFF")
        label_window.place(x=0, y=0, width=1920, height=50)
        
        columns = ("Cod", "Loan date", "Devolution date", "status")
        tree = ttk.Treeview(view_window, columns=columns, show="headings")
        tree.place(x=100, y=150, width=1700, height=800)

        tree.heading("Cod", text="Cod")
        tree.heading("Loan date", text="Loan date")
        tree.heading("Devolution date", text="Devolution date")
        tree.heading("status", text="status")

        scrollbar = ttk.Scrollbar(
        view_window,
        orient='vertical',
        command=tree.yview
        )
        scrollbar.place(x=1801, y=150, height=800)
        

        view.select4(tree, connect)

        btn_exit = Button(view_window, text="Exit", font="Stylus", background="#CD1010", foreground="#FFFFFF", command=lambda:sgbDisconnection(connect, view_window, mnu))
        btn_exit.place(x=1725, y=0, width=200, height=50)
        view_window.mainloop()







