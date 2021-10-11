import MySql
query1 = "create database school"
query = "create table attendence(roll int unique, Name varchar(20))"
try:
    print("testing credentials.................", '\n')
    usr = input("please provide user name ")
    dbpswd = input("Password")
    try:
        MySql.exc(query1, usr, dbpswd,"mysql", get='exeonly')
        print("New data base successfully created...........")
    except:
        print("database already exist")
        pass
    MySql.exc(query, usr, dbpswd,"school", get='exeonly')
    print("table created..............")
    print("succesfully created all required file in MY Sql start using it.................")
    input()
except:
    print("IT SEEMS table already exist if provided credentials are correct")
    input()
    exit()
