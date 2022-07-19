import collections
import mysql.connector

# create table if not exists Customer( c_id int not null auto_increment unique, s_name varchar(80) not null, s_age int not null, f_id int not null, book_issued int not null, fine double not null Default 0, book_id int not null, role_id int not null );
# create table if not exists Customer( c_id int not null auto_increment unique, 
#                                     s_name varchar(80) not null, 
#                                     s_age int not null, 
#                                     f_id int not null, 
#                                     book_issued int not null, 
#                                     fine double not null Default 0,
#                                     book_id int not null, 
#                                     role_id int not null );


class Database:
    def __init__(self,db_name="lms"):
        try:
            # self.collection_name=collection_name
            self.db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database=db_name
                    )
            self.mycursor = self.db.cursor()
            #mysql show tables #mycursor.execute("SHOW TABLES")
            # self.myclient=pymongo.MongoClient("mongodb://localhost:27017/")   #connect to mongo db
            # self.db=self.myclient[db_name]  #can be accessed by .db_name or [db_name]    
            # self.collection_name=collection_name        
            # if collection_name not in self.db.list_collection_names():
            #     self.posts=self.db.posts

        except:
            print("Error Occured")

    def close_conn(self):
        self.mycursor.close()

    def add_to_db(self,d1):       
        self.mycursor.execute(d1)
        self.db.commit()
        print(self.mycursor.rowcount, "record inserted.")
   

    def get_all(self,d1):
        self.mycursor = self.db.cursor()
        self.mycursor.execute(d1)
        x= self.mycursor.fetchall()
        # print(x)
        return x
    def update_db(self,d1):
        self.mycursor.execute(d1)
        self.db.commit()
        print(self.mycursor.rowcount, "record(s) affected")

    def delete_from_db(self,d1):
        self.mycursor.execute(d1)
        self.db.commit()
        print(self.mycursor.rowcount, "record(s) affected")
       
# db=Database('adventure')
# # db.add_to_db("INSERT INTO `adventure`(`id`,`adventure_name`, `location`, `photo`) VALUES (%s,%s,%s,%s)",('3','2test','e','r'))
# print(db.get_all("Select * from adventure"))



    # def add_to_db(self,d1):
    #     x=self.collection_name.insert_one(d1)
    #     print(x)

    # def get_one_from_db(self,d1):
    #     x=self.collection_name.find(d1)
    #     print(x) 
    
    # def get_all(self,d1):
    #     x=self.collection_name.find()
    #     print(x)

    # def update_db(self,d1,d2):
    #     d2={"$set":d2}
    #     x=self.collection_name.update_many(d1,d2)
    #     print(x,x.modified_count)

    # def delete_from_db(self,d1):
    #     x=self.collection_name.insert_one(d1)
    #     print(x,x.deleted_count) 
    
# class Customers_DB(Database):
#     def __init__(self,db_name="LMS"):
#         if db_name not in self.db.list_collection_names():
#                 self.posts=self.db.posts

#     def add_customer_to_db(self):
#         pass

#     def get_customer_from_db(self):
#         pass   

#     def update_customer_db(self):
#         pass

#     def delete_customer_from_db(self):
#         pass 

# class Book_DB(Database):
#     def __init__(self,db_name="LMS"):
#         if db_name not in self.db.list_collection_names():
#                 self.posts=self.db.posts
                    
#     def add_book_to_db(self):
#         pass

#     def get_book_from_db(self):
#         pass   

#     def update_book_db(self):
#         pass

#     def delete_book_from_db(self):
#         pass 

# class Category_DB(Database):
#     def __init__(self,db_name="LMS"):
#         if db_name not in self.db.list_collection_names():
#                 self.posts=self.db.posts
                    
#     def add_category_to_db(self):
#         pass

#     def get_category_from_db(self):
#         pass   

#     def update_category_db(self):
#         pass

#     def delete_category_from_db(self):
#         pass 


# class Role_DB(Database):
#     def __init__(self,db_name="LMS"):
#         if db_name not in self.db.list_collection_names():
#                 self.posts=self.db.posts
                
#     def add_role_to_db(self):
#         pass

#     def get_role_from_db(self):
#         pass   

#     def update_role_db(self):
#         pass

#     def delete_role_from_db(self):
#         pass 

# class Rule_DB(Database):
#     def __init__(self,db_name="LMS"):
#         if db_name not in self.db.list_collection_names():
#                 self.posts=self.db.posts
                
#     def add_rule_to_db(self):
#         pass

#     def get_rule_from_db(self):
#         pass   

#     def update_rule_db(self):
#         pass

#     def delete_rule_from_db(self):
#         pass 