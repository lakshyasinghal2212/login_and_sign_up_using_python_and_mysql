import mysql.connector as mc
mycon=mc.connect(host="localhost",user="",password="",database='')
cur=mycon.cursor()
print("---Welcome---\n")

def signup():
    print("Welcome...you can now signup")
    cur.execute("create table if not exists details(Username varchar(20) not null, Password varchar(10) not null)")
    cur.execute("select username from details")
    rows = cur.fetchall()

    name = input("Enter username:")
    if any(name in row for row in rows):
        print("Username exists. Go to login.")
        login()
    else:
        password = input("Enter password:")
        cur.execute("insert into details values (%s, %s)",(name,password))
        mycon.commit()
        print("Registration successful. You can now log in.")
        login()

    signup()


def loginmenu():
    print("What you want to choose:-\n1)Add a new Id name\n2)Delete a Id name\n3)Update a Id name\n4)show all id names with the particular account")
    option=int(input("select option:"))
    if(option==3):
        name=input("Enter new id name:")
        old=input("Enter existing id name:")
        cur.execute("update details set username= %s where username= %s ",(name,old))
        mycon.commit()
        
    elif(option==2):
        name=input("Enter user id name:")
        cur.execute("delete from details where username= %s ",(name))
        mycon.commit()

        
    elif(option==1):
        name=input("Enter new id name:")
        pswd=input("Enter new id password:")
        cur.execute("insert into details values(%s,%s)",(name,pswd))
        mycon.commit()
        
    elif(option==4):
        name=input("Enter id name:")
        cur.execute("Select * from details where username=%s",(name))
        res=cur.fetchall()
        print(res)
        
        
        
    else:
        print("invalid input")
        loginmenu()
    

def login():
    print("Welcome...you can now login")
    name=input("Enter username:")
    cur.execute("select username from details")
    rows = cur.fetchall()
    if not any(name in row for row in rows):
        print("Username doesn't exists. Go to signup.")
        signup()
    else:
        password = input("Enter password:")
        cur.execute("SELECT * FROM details WHERE username = %s AND password = %s", (name,password))

        user = cur.fetchone()

        if user:
            print("Login successful!")
            loginmenu()
            
        else:
            print("Invalid username or password.")
            main()
  
    login()


def reset():
    name=input("Enter username:")
    cur.execute("select username from details")
    rows = cur.fetchall()
    if not any(name in row for row in rows):
        print("Username doesn't exists. Go to signup.")
        signup()
    else:
        pswd=input("Enter new password:")
        cur.execute("update details set password= %s where username= %s ",(pswd,name))
        mycon.commit()
        print("Done...Now login")
        login()
    



def main():
    
    print("1)Log in\n2)Sign Up\n3)Reset Password")
    option=int(input("Choose your option:"))
    if(option==1):
        login()
    elif(option==2):
        signup()
    elif(option==3):
        reset()
    else:
        print("***************Choose a valid option***************")
        main()



main()
