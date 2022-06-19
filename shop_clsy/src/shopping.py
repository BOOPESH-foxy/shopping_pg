# from cProfile import label
# from os import system
# from turtle import clear
# from unicodedata import name
# import psycopg2
# import pwinput
# from tkinter import *



# class user_page():
#     def print_result():
#         print("you are a user")
        

# class admin_page():
    
#     def print_result():
#         print("you are an admin")

# if __name__=="__main__":
    
#     connector=psycopg2.connect(database="shopclassy",user='shopclassy',host="127.0.0.1",password="classyclothes",port="5432")
#     cursor=connector.cursor()
#     def access():
        
        
#         window = tkinter.Tk() 
#         window.title("Log-In")
#         window.geometry("200x150")
#         usernametext=tkinter.Label(window,text="username")
#         usernameguess = tkinter.Entry(window)
#         passwordtext = tkinter.Label(window, text="Password:")
#         passwordguess = tkinter.Entry(window, show="*")
        
#         attemptlogin = tkinter.Button(text="Login", command=trylogin)
#         usernametext.pack()
#         usernameguess.pack()
#         passwordtext.pack()
#         passwordguess.pack()
#         attemptlogin.pack()
#         window.mainloop()


#         username=str(input("Enter username :"))
#         password=pwinput.pwinput(prompt="password :", mask="*")
#         sql_q= 'SELECT isadmin FROM Authentication where username like %s and passcode like %s'
#         data=(username,password)
#         cursor.execute(sql_q,data)
#         isadmin=cursor.fetchall()
#         print(isadmin[0][0])
#         if isadmin[0][0] == 0:
#             user_page.print_result()
#         elif isadmin[0][0] == 1:
#             admin_page.print_result()
#         else:
#             print("...")
    
#     access()

#     connector.commit()
#     connector.close()



# import json
# import time


# def login_sys():

    
#     print('''    \t Simple Python Login System
#     \t Welcome to Our Login Portal''')
#     try:
#         choice =int(input('\n Enter 1 to Login and Enter any key to Create an New Account:'))
        
#     except ValueError:
#         print('\n Oops .. read the above line correctly!!')
         
          
#     if choice == 1 and is_first()== True:
#         while True:
#             print('\n database is empty! create a new account\n')
#             print('\n create an account is first!!!!')
#             break
#     elif choice == 1 and is_first() == False:
#         login()
#     else:
#         new_account()


    
    

    

   
    
   
    

# #profile = {name : [name,passwd]}
# def new_account():
#     name = input(('\n Enter ur Name :'))
#     passwd = input(('Enter ur Passsword:'))
#     profile = {name : [name,passwd]}
#     if is_first() == False:
#         with open('ds.json','r') as file:
#             previous_data= json.load(file)
#             with open('ds.json','w') as file:
#                 new_data = { **previous_data,**profile}
#                 json.dump(new_data,file)
#                 print('your account is successfully created!!')
#                 print('lets login')
                

#     else:
#         with open('ds.json','w') as file:
#             json.dump(profile,file)
#             print('your account is successfully created!!')
#             print('lets login')
            
           
# def is_first():
#     is_first = True
#     with open('ds.json','r') as file:
#         data = file.read()
#         if len(data) > 0:
#             return False
#         else:
#             return True


# def login():
    
#     while True:
#         name = input(('\n Enter ur Name :'))
#         if check_name(name) == True:
#             passwd = input(' enter ur password:')
#             if check_passwd(name ,passwd) == True:
#                 print('you are logged in successfully')
#                 logout()
#                 break
#             else:
#                 print('enter the correct password!!')
#                 continue
#         else:
#             print('enter vaild username')
#             continue


# def check_name(name):
#     with open('ds.json','r') as file:
#         data = json.load(file)
#         if name in data:
#             return True
#         else:
#             return False

# def check_passwd(name,passwd):
#     with open('ds.json','r') as file:
#         data = json.load(file)
#         if name in data:
#             if data[name][1] == passwd:
#                 return True
#             else:
#                 return False

    

# def logout():
#     print('wait 3 sec')
#     time.sleep(3)
#     d = input('do you want logout? y/n:\t')
#     if d == 'y':
#         print('you are logged out successfully!!')
#     else:
#         print('inga onnum illa!!')


  

 
    

  
    
    



    

# if __name__ == "__main__":
#     login_sys()
