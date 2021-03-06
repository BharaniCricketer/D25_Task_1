import os.path
import json
import re

# IF FILE EXISTS ACCESS THE FILE, IF NOT CREATE A NEW FILE #
if os.path.isfile('credentials.json'):
    pass
else:
    print("creating new file")
    with open('credentials.json',"w") as fw:
        json.dump({"email":'password'},fw)
        pass

def validator(email,password):
    email_regex='^[A-Za-z0-9]+.*[A-Za-z0-9]+@[A-Za-z]+\.(com|in)$'
    pass_regex='^(?=.{5,16}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W).*$'
    if(re.search(email_regex,email) == None or re.search(pass_regex,password) == None):
        return False
    else:
        return True

def forgot_password(email):
    with open ('credentials.json','r') as fr:
        data=json.load(fr)
    if email in data.keys():
        print("Your password is: ",data[email])
        m=input("Press 'Y' to Home Page: ").strip().lower()
        if m=='y':
          choice()
        else:
          print("Exit")
    else:
        k=input("Please enter a valid email, Press 'Y' to continue : ").strip().lower()
        if k=='y':
          l=input("\nEnter EMAIL ID: ").strip().lower()
          forgot_password(l)
        else:
          print("Exit")
        
        
    return True

def register():
    data={}
    val=False
    forgot=False
    email=input("\nRegistration \nEMAIL ID: ").strip().lower()
    password=input("PASSWORD: ").strip()
    isFileEmpty=False
    final_validator=validator(email,password)
    if(final_validator == False):
        x=input("Please Enter a valid EMAIL ID and PASSWORD, Press 'Y' to continue : ").strip().lower()
        val=True
        if x=='y':
            register()
        else:
            print("Exit")
    else:
        with open("credentials.json","r") as fr:
            try:
                data=json.load(fr)
                #print(data)
            except:
                isFileEmpty=True
        if not isFileEmpty:
            if email in data.keys():
                print("You already have an existing account")
                fp=input("If you want to recover your password Please enter 'Y': ").strip().lower()
                if(fp == 'y'):
                    forgot=forgot_password(email)
            else:
                data.update({email:password})
                with open ('credentials.json',"w") as fw:
                    json.dump(data,fw)
        else:
            data.update({email:password})
            with open ('credentials.json',"w") as fw:
                json.dump(data,fw)
    if(forgot):
        choice()
    elif val:
        pass
    else:
        print("Registration Sucessfull")
        z=input("Press 'Y' to Home Page: ").strip().lower()
        if z=='y':
          choice()
        else:
          print("Exit")


def login():
    forgot=False
    email=input("\nLogin \nEMAIL ID: ").strip().lower()
    password=input("PASSWORD: ").strip()
    with open('credentials.json',"r") as fr:
        try:
            data=json.load(fr)
        except:
            pass
    if email in data.keys():
        if(password==data[email]):
            print("You are logging in...")
        else:
            print("You have entered wrong password")
            fp=input("If you want to recover your password Please enter 'Y': ").strip().lower()
            if(fp == 'y'):
                forgot=forgot_password(email)
    else:
        print("Entered Mail ID is not Registered")
        f=input("Press 'Y' to Register: ").strip().lower()
        if f=='y':
            register()
        else:
            print("Exit")


def choice():
    log=input("\nHOME \nPlease enter \n1 Login \n2 Register\n3 Forgot password \n").strip()
    if(log=='1'):
        login()
    elif(log=='2'):
        register()
    elif(log=='3'):
        email=input("\nForgot Password \nEnter EMAIL ID: ").strip().lower()
        forgot_password(email)
        pass
    else:
        print("Please enter a valid choice")
        choice()

choice()
