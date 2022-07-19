import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import *
from click import password_option
from db import Database
# db=Database('adventure')
# # db.add_to_db("INSERT INTO `adventure`(`id`,`adventure_name`, `location`, `photo`) VALUES (%s,%s,%s,%s)",('3','2test','e','r'))
# print(db.get_all("Select * from adventure"))

# create table if not exists Customer( c_id int not null auto_increment unique, 
#                                     s_name varchar(80) not null, 
#                                     s_age int not null, 
#                                     f_id int not null, 
#                                     book_issued int not null, 
#                                     fine double not null Default 0,
#                                     book_id int not null, 
#                                     role_id int not null,
#                                   	Constraint c1 foreign key (book_id) references Book(book_id),
#                                   	Constraint c1 foreign key (role_id) references Role(role_id) 
#                                    );
class Login:
    def __init__(self,username,password,role_id):
        self.username=username
        self.password=password 
        self.role_id=role_id

class Customer:
    def __init__(self,student_id,name,age,faculty,num_of_books_issued,fine,bookid,role):
        self.student_id=student_id        
        self.name=name
        self.age=age
        self.faculty=faculty
        self.num_of_books_issued=num_of_books_issued
        self.fine=fine
        self.bookid=bookid
        self.role_id=role

# create table if not exists faculty ( faculty_id int not null auto_increment primary key , faculty_name varchar(80) not null unique );
class Faculty:
    def __init__(self,faculty_id,faculty_name):
        self.faculty_id=faculty_id
        self.faculty_name=faculty_name
    
# create table if not exists Book( book_id int not null auto_increment unique, c_id int not null, book_name varchar(80) not null unique, author_name varchar(80) not null, isbn varchar(30) not null default 000000, total_number int not null default 1, books_left int not null default 0, Constraint f1 Foreign key (c_id) references category(category_id) );
class Book:
    def __init__(self,root):#,book_id,category_id,book_name,author_name,isbn,total_number,books_left
        self.__book_id=tk.StringVar()
        self.__category_id=tk.StringVar()
        self.__book_name=tk.StringVar()
        self.__author_name=tk.StringVar()
        self.__isbn=tk.StringVar()
        self.__total_number=tk.StringVar()
        self.__books_left=tk.StringVar()
        self.__screen=ttk.LabelFrame(root).pack(side="top")

    def book_screen(self,var_name,varName):
        self.main_label=ttk.Label(self.__screen,text="Enter "+var_name)
        self.main_label.pack(side="top")
        self.main_entry=ttk.Entry(self.__screen,width=20,textvariable=varName)
        self.main_entry.pack(side="top")

    def book_render(self):
        self.__book_id=tk.StringVar()
        self.__category_id=tk.StringVar()
        self.__book_name=tk.StringVar()
        self.__author_name=tk.StringVar()
        self.__isbn=tk.StringVar()
        self.__total_number=tk.StringVar()
        self.__books_left=tk.StringVar()
        self.__screen=ttk.LabelFrame(root).pack(side="top")
        self.book_screen("Category Id",self.__category_id)    
        self.book_screen("book Name",self.__book_name)
        self.book_screen("author_name",self.__author_name)
        self.book_screen("isbn",self.__isbn)
        self.book_screen("total Number of Books",self.__total_number)
        ttk.Button(self.__screen,text="Add Books",command=self.add_to_db).pack(side="top")
        ttk.Button(self.__screen,text="Home Screen",command=self.home).pack(side="top")

    def add_to_db(self):
        print(f"{self.__book_name.get()} ")
        db=Database()
        query=f"INSERT INTO `book`(`c_id`, `book_name`, `author_name`, `isbn`, `total_number`, `books_left`) VALUES  ('{self.__category_id.get()}','{self.__book_name.get()}','{self.__author_name.get()}','{self.__isbn.get()}','{self.__total_number.get()}','{self.__total_number.get()}')";
        print(query)
        db.add_to_db(query)
        db.close_conn()

    def home(self):
        # screen_render("login_screen")
        self.__screen.destroy()
        login_form()


# create table if not exists Category( category_id int not null auto_increment primary key, category_name varchar(80) not null unique );
class Category:
    def __init__(self,category_id,category_name):        
        self.category_id=category_id
        self.category_name=category_name

# create table if not exists Role( role_id int not null primary key, role_name varchar(80) not null unique );
class Role:
    def __init__(self,role_id,role_name):
        self.role_id=role_id
        self.role_name=role_name

class Rule:
    def __init__(self,rule_name,rule_for):
        self.rule_name=rule_name
        self.rule_for =rule_for  

class Table:
    def __init__(self,root,query,tuple1):
        db=Database()
        data=db.get_all(query)
        print(len(data),data[0])
        total_row=len(data)
        total_cols=len(data[0])
        self.treeview1 = ttk.Treeview(root, columns=(1, 2, 3,4,5,6), show='headings')
        self.treeview1.pack()
        self.treeview1.heading(1, text="ID")
        self.treeview1.heading(2, text="Name")
        self.treeview1.heading(3, text="Email")
        self.treeview1.heading(4, text="Age")
        self.treeview1.heading(5, text="Faculty")
        self.treeview1.heading(6, text="Role")
        for i in data:
            print(i,type(i),i[0])
            self.treeview1.insert(parent='', index=i[0], iid=i[0], values=i)

    # print(f"Login credentials are {username1.get()} and {password.get()}")


root=tk.Tk(baseName="Basename")
root.minsize(width=400,height=500)
root.title("Login Form")
def login_form(x=0):
    # if x!=0:        
    #     x.destroy()
    # main_frame=ttk.LabelFrame(root,text="Grouping the frames") 
    main_frame=ttk.LabelFrame(root,text="Grouping the frames")
    main_frame.pack(expand=True,padx=1,pady=2,fill="both")   
    main_label=ttk.Label(main_frame,text="Login Form",background="red",foreground="white")
    main_label.pack(side="top",padx=(6,4),expand=False,fill="both")
    name_label=ttk.Label(main_frame,text="Username",background="blue",foreground="white")
    name_label.pack(side="top")
    username_entry=ttk.Entry(main_frame,width=20,textvariable=email)
    username_entry.pack(side="top")
    password_label=ttk.Label(main_frame,text="Password",background="red",foreground="white")
    password_label.pack(side="top")
    password_entry=ttk.Entry(main_frame,width="20",textvariable=password)
    password_entry.pack(side="top")
    login_button=ttk.Button(main_frame,text="Log In",command=login)
    login_button.pack(side="top")

def add_user(root):      
    # main_frame=ttk.LabelFrame(root,text="Grouping the frames")
    # main_frame.destroy()    
    global main_frame
    main_frame=ttk.LabelFrame(root,text="Grouping the frames")
    main_frame.pack(expand=True,side="left",fill="both",padx=3,pady=8)
    # username_frame=ttk.LabelFrame(main_frame)
    unifunc(main_frame,"name",name)
    unifunc(main_frame,"email",email)
    unifunc(main_frame,"password",password)
    unifunc(main_frame,"confirm_password",confirm_password)
    unifunc(main_frame,"age",age)
    unifunc(main_frame,"faculty",faculty)
    unifunc(main_frame,"book_id",book_id)
    unifunc(main_frame,"role_id",role_id)
    ttk.Button(main_frame,text="Sign Up",command=signing_up).pack(side="left")
    ttk.Button(main_frame,text="Log In",command=lambda:screen_render("login_screen")).pack(side="left")

def screen_render(x):
    main_frame.destroy()   
    if x=="login_screen":
        login_form()
    elif x=="signup_screen":
        pass
    elif x=="checkout_screen":
        pass
    elif x=="see_details":
        pass
    elif x=="search_books":
        pass

def login():
    pass
def unifunc(password_frame,var_name,varName):
    # password_frame=ttk.LabelFrame(main_frame)
    password_label=ttk.Label(password_frame,text="Enter "+var_name)
    password_label.pack(side="top")
    password_entry=ttk.Entry(password_frame,width=20,textvariable=varName)
    password_entry.pack(side="top")

def signing_up():
    db=Database()
    query=f"INSERT INTO `customer`(`s_name`, `s_age`, `email`,`f_id`,  `role_id`) VALUES ('{name.get()}','{age.get()}','{email.get()}','{faculty.get()}','{role_id.get()}')"
    db.add_to_db(query);
    db.close_conn();
    db=Database()
    query=f"INSERT INTO `login`(`username`, `password`, `status`, `role_id`) VALUES ('{email.get()}','{password.get()}','1','{role_id.get()}')"
    db.add_to_db(query);
    print(f"Values are {name.get()} {email.get()} {password.get()} {age.get()} {faculty.get()} {book_id.get()} and {role_id.get()}")  
    db.close_conn()

def add_books():
    db=Database()
    query=f"INSERT INTO `book`(`book_id`, `c_id`, `book_name`, `author_name`, `isbn`, `total_number`, `books_left`)  VALUES ('{name.get()}','{age.get()}','{email.get()}','{faculty.get()}','{role_id.get()}')"
    db.add_to_db(query);
    db.close_conn();


def see_books():
    pass

def see_all_users():
    pass

def sell_all_checkouts():
    pass

def checkout():
    pass

name=tk.StringVar()
password=tk.StringVar()
confirm_password=tk.StringVar()
email=tk.StringVar()
age=tk.StringVar()
faculty=tk.StringVar()
book_id=tk.StringVar()
role_id=tk.StringVar()

# main_frame=ttk.LabelFrame(root,text="Grouping the frames")

# add_user(root)
# tb=Table(root,"Select * from customer limit 0,25",('ID','Name','Age'))

book=Book(root)
book.book_render();
root.mainloop()