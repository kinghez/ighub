import sqlite3
import random
import pandas as pd
import time

#=====================================Sub Functions===============================
def Create_Acct():
    Name = input("Enter First Name: ")
    Mid_Name = input("Enter Middle Name: ")
    Sur_Name = input("Enter SurName: ")
    Address = input("Enter Your Address : ")
    Age = input("Specify Your Age: ")
    Pin = input("Enter A Four Digit Pin: ")
    if len(Pin) != 4:
        print("Wrong Pin, It Must Be Four Digits(1234)")
        Create_Acct()
    else:
        Pin_2 = input("Confirm  Pin: ")
        if Pin_2 != Pin:
            print("Your Pin Does Not Match!")
            Create_Acct()

        else:
            Acct_Balance = input("How Much Will Open Your Account With: ")
            n = random.sample(range(0, 10), 10) 
            num = "{}{}{}{}{}{}{}{}{}{}".format(n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7],n[8],n[9])
            acct_num = int(num)
            con = sqlite3.connect("FirstDataBase.db")   
            con.execute('''INSERT INTO ATM_1(
            FIRSTNAME,MIDNAME,SURNAME,ADDRESS,AGE,ACCOUNT_NUMBER,PIN,ACCOUNT_BALANCE)
            VALUES(?,?,?,?,?,?,?,?)''',(Name,Mid_Name,Sur_Name,Address,Age,acct_num,Pin,Acct_Balance))
            con.commit()
            con.close()
            print("Please Save Your Details")
            print("Your Pin Is: ", Pin)
            print("Your Account Number Is: {}".format(acct_num))
            print(" ===================================================")
            time.sleep(10)
            SIMPLE_ATM()
            
#-----------------------------------Withdrawal---------------------------------------

def Withdrawal(pin, num):
    con = sqlite3.connect("FirstDataBase.db")
    df = pd.read_sql_query("SELECT * FROM ATM_1", con)
    try:
        new = df[(df["PIN"] == pin) & (df["ACCOUNT_NUMBER"] == num)]
        lis = new.values.tolist()
        print("========================================================================")
        print(" ")
        print("Welcome: {}, Your Current Balance Is: {}".format(lis[0][2], lis[0][-1]))
        print(" ")
        print("=====================================================")
        withdraw = int(input("Enter Amount To Withdraw: "))
        if lis[0][-1] > withdraw:
            bal = lis[0][-1] - withdraw
            con.execute('''UPDATE ATM_1 SET ACCOUNT_BALANCE=? WHERE ACCOUNT_NUMBER=?''', (bal,num))
            con.commit()
            con.close()
            print("==================================================")
            print(" ")
            print("{} Withdrawn Successfully".format(withdraw))
            print("NEW BALANCE: {}".format(bal))
            print(" ===================================================")
            time.sleep(10)
            SIMPLE_ATM()
        else:
            print("============================================================")
            print(" ")
            print("Insufficient Funds, Enter Amount LessThan Your Balance!")
            time.sleep(3)
            SIMPLE_ATM()
    except:
        print("There Is No Account With This Details")
        print("=====================================================")
        print(" ")
        time.sleep(3)
        SIMPLE_ATM()
 #------------------------------------------------------------Deposit--------------
def Deposit(pin, num):
    con = sqlite3.connect("FirstDataBase.db")
    df = pd.read_sql_query("SELECT * FROM ATM_1", con)
    try:
        new = df[(df["PIN"] == pin) & (df["ACCOUNT_NUMBER"] == num)]
        lis = new.values.tolist()
        print("========================================================================")
        print(" ")
        print("Welcome: {}, Your Current Balance Is: {}".format(lis[0][2], lis[0][-1]))
        print(" ")
        print("=====================================================")
        deposit = int(input("Enter Amount To Deposit: "))
        bal = lis[0][-1] + deposit
        con.execute('''UPDATE ATM_1 SET ACCOUNT_BALANCE=? WHERE ACCOUNT_NUMBER=?''', (bal,num))
        con.commit()
        con.close()
        print("==================================================")
        print(" ")
        print("{} Deposited Successfully".format(deposit))
        print("NEW BALANCE: {}".format(bal))
        print(" ===================================================")
        time.sleep(10)
        SIMPLE_ATM()
    except:
        print("There Is No Account With This Details")
        print("=====================================================")
        print(" ")
        time.sleep(3)
        SIMPLE_ATM()


#----------------------------Enquiry------------------------------------------------
def Enquiry(pin, num):
    con = sqlite3.connect("FirstDataBase.db")
    df = pd.read_sql_query("SELECT * FROM ATM_1", con)
    try:
        new = df[(df["PIN"] == pin) & (df["ACCOUNT_NUMBER"] == num)]
        lis = new.values.tolist()
        print("========================================================================")
        print(" ")
        print("Welcome: {} {}".format(lis[0][2], lis[0][1]))
        print(" ")
        print("=====================================================")
        print(" ")
        print("1 Check Balance                                 2 View Pin And Account Number")
        enq = int(input("Select An Option: "))
        if enq == 1:
            print("==================================================")
            print(" ")
            print("YOUR ACCOUNT BALANCE IS: {}".format(lis[0][-1]))
            print(" ===================================================")
            time.sleep(10)
            SIMPLE_ATM()
            
        elif enq == 2:
            print("==================================================")
            print(" ")
            print("YOUR PIN IS: {}\n ACCOUNT NUMBER: {}".format(lis[0][6],lis[0][5]))
            print(" ===================================================")
            time.sleep(10)
            SIMPLE_ATM()
            
        else:
            print("Goodbye!")
            
            
    except:
        print("There Is No Account With This Details")
        print("=====================================================")
        print(" ")
        time.sleep(3)
        SIMPLE_ATM()
        
        

#=================================Main Function===================================
def SIMPLE_ATM():
    print("=========================================================================================")
    print("||                                                                                     ||")
    print("||        WELCOME USER, SELECT 5 TO CREATE ACCOUNT SELECT OTHER OPTION TO CONTINUE     ||")
    print("||                                                                                     ||")
    print("||                                                                                     ||")
    print("=========================================================================================")
    print("||                              SELECT A SERVICE                                       ||")
    print("||                                                                                     ||")
    print("||                                                                                     ||")
    print("|| 1 Withdrawal                                                  5 Create Account      ||")
    print("||                                                                                     ||")
    print("|| 2 Enquiry                                                     6 Airtime Top Up      ||")
    print("||                                                                                     ||")
    print("|| 3 Deposit Cash                                                7 Change Pin          ||")
    print("||                                                                                     ||")
    print("|| 4 Transfer Cash                                               8 FOR ADMIN LOGIN     ||")
    print("||                                                                                     ||")
    print("=========================================================================================")
    
    entry = int(input("Select An Option: "))
    if entry == 1:
        print(" ")
        print(" ")
        print("=========================================================================================")
        print("||                Enter Your Bank Details Below To Login                                ||")
        print("=========================================================================================")
        acct_n = int(input("Enter Your Acct Number: "))
        pin = int(input("Enter Your For Digit Pin: "))
        Withdrawal(pin, acct_n)
    elif entry == 2:
        print(" ")
        print(" ")
        print("=========================================================================================")
        print("||                Enter Your Bank Details Below To Login                                ||")
        print("=========================================================================================")
        acct_n = int(input("Enter Your Acct Number: "))
        pin = int(input("Enter Your For Digit Pin: "))
        Enquiry(pin, acct_n)
                
    elif entry == 3:
        print(" ")
        print(" ")
        print("=========================================================================================")
        print("||                Enter Your Bank Details Below To Login                                ||")
        print("=========================================================================================")
        acct_n = int(input("Enter Your Acct Number: "))
        pin = int(input("Enter Your For Digit Pin: "))
        Deposit(pin, acct_n)
                
    elif entry == 4:
        print(" ")
        print(" ")
        print("=========================================================================================")
        print("||                Enter Your Bank Details Below To Login                                ||")
        print("=========================================================================================")
        acct_n = int(input("Enter Your Acct Number: "))
        pin = int(input("Enter Your For Digit Pin: "))
                
    elif entry == 5:
        print(" ")
        print(" ")
        print("=========================================================================================")
        print("||                Fill The Form Below To Create Account                                ||")
        print("=========================================================================================")
        Create_Acct()
                
    elif entry == 6:
        print(" ")
        print(" ")
        print("=========================================================================================")
        print("||                Enter Your Bank Details Below To Login                                ||")
        print("=========================================================================================")
        acct_n = int(input("Enter Your Acct Number: "))
        pin = int(input("Enter Your For Digit Pin: "))
                
    elif entry == 7:
        print(" ")
        print(" ")
        print("=========================================================================================")
        print("||                Enter Your Bank Details Below To Login                                ||")
        print("=========================================================================================")
        acct_n = int(input("Enter Your Acct Number: "))
        pin = int(input("Enter Your For Digit Pin: "))
                
    elif entry == 8:    
        print(" ")
        print(" ")
        print("=========================================================================================")
        print("||                Enter Admin Login                                                      ||")
        print("=========================================================================================")
        acct_n = input("Enter Admin Username: ")
        pin = input("Enter Admin Password: ")
        
        if acct_n == "Admin" and pin == "191admin":
            con = sqlite3.connect("FirstDataBase.db")
            #con.execute()
            df = pd.read_sql_query("SELECT * FROM ATM_1", con)
            con.close()
            print("")
            print("CUSTOMER DATABASE:")
            print("")
            print(df)
        
        else:
            print("Wrong Username OR Password")
            print("=====================================================")
            print(" ")
            time.sleep(3)
            SIMPLE_ATM()
        
        
SIMPLE_ATM()