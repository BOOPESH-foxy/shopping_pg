from distutils.util import execute
from os import system
from secrets import choice
from turtle import clear
from unicodedata import name
import psycopg2
import pwinput
    
class admin_page():
    
    def add_product():
            product_id=input("1:product_id:")
            product_name=input("2:product_name:")
            product_price=input("3:price:")
            product_quantity=input("4:number of new stocks:")    
            
            
            sql_q='INSERT INTO STOCKS(product_code,product_name,product_price,a_quantity) VALUES(%s,%s,%s,%s);'
            data=(product_id,product_name,product_price,product_quantity)
            cursor.execute(sql_q,data)
            connector.commit()
            return 1;
        
    def view_products():
        sql_q="SELECT * FROM STOCKS;"
        cursor.execute(sql_q)
        stocks=cursor.fetchall()
        for data in stocks:
            print(data)
            print("\n")
        connector.close()
        
    def delete_product():
        q=str(input("Wanna delete stocks [y/n]:"))
        if q in ['y' or 'Y']:
            user=input("Enter username:")
            password=str(pwinput.pwinput(prompt="Enter password",mask="*"))
            sql_q="SELECT passcode from authentication WHERE user like %s"
            cursor.execute(sql_q,user)
            password_d=cursor.fetchall()
            out=password==password_d[0,0]
            if (out == 'True'):
                query="DELETE * from table stocks where product_code=%s"
                code=input("Enter product id to be removed:")
                cursor.execute(query,code)
            else:
                print("Wrong password")
        connector.commit()
        choise=input("wanna remove multiple stocks[y/n]:")
        if choise in ['y' or 'Y']:
            admin_page.delete_product()
        else:
            work()
        
        if q in ['n' or 'N']:
            work()
        
        
class user_page():
    
    def view_stock():
        sql_q="SELECT product_name,product_price FROM STOCKS;"
        cursor.execute(sql_q)
        stocks=cursor.fetchall()
        for data in stocks:
            print(data)
            print("\n")        
        
    def place_order():
        pass    
            
            
            
            
        
if __name__=="__main__":
    
    connector=psycopg2.connect(database="shopclassy",user='shopclassy',host="127.0.0.1",password="classyclothes",port="5432")
    cursor=connector.cursor()
    print(connector)
    
    
    
    def access():
        username=str(input("Enter username :"))
        password=pwinput.pwinput(prompt="password :", mask="*")
        sql_q= 'SELECT isadmin FROM Authentication where username like %s and passcode like %s'
        data=(username,password)
        cursor.execute(sql_q,data)
        isadmin=cursor.fetchall()
        
        if isadmin[0][0] == 0:
                print("1. View available stocks:\n2. Place your order\n3. Exit")
                op=int(input("Enter your choice:"))
                if op==1:
                    user_page.view_stock()
                elif op==2:
                    user_page.place_order()    
                elif op==3:
                    exit()
        elif isadmin[0][0] == 1:
            work()
        
        else:
            print("Not an authorised user or admin:")
            
    def work():
            print("1. Add new product \n2. View existing products \n3. Delete existing product\n4.View specific table\n5. Exit")
            case=int(input("Enter your process:"))
            if case == 1:
                progres=admin_page.add_product()
                if progres == 1:
                    print("updated new stocks..")
                else:
                    print("failed during updation.(retry!)")
                    
            elif case == 2:
                admin_page.view_products()
                
            elif case==3:
                admin_page.delete_product()
            choise=input("wanna exit..(y/n)")
            if choise in ['Y' or 'y']:
                exit()
            elif choise in ['N' or 'n']:
                work()

    def exit():
        connector.close()
        print("Exitting")
    
    access()
