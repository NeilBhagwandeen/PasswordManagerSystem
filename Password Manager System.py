import hashlib
import pyperclip
import time


def signup ():
    email = input ("Please Enter Your Email : ")
    password = input ("Please Enter A Password : ")
    key = email+password
    hkey = hashlib.md5(key.encode())
    f = open("database1.dat","w+")
    f.write(email)
    f.write(" ")
    f.write(hkey.hexdigest())
    f.close()
    return

def login ():
    f = open("database1.dat","r")
    credentials = f.readline()
    f.close()
    (email,hkey) = credentials.split(" ")
    hkey = list(hkey)
    if "\n" in hkey:
        hkey.remove("\n")
    hkey = "".join(hkey)
    password = input ("Please Enter Your Password : ")
    key = email+password
    phkey = hashlib.md5(key.encode())
    phkey = phkey.hexdigest()
    if phkey == hkey:
        return (True)
    else:
        return (False)

def addpassword ():
    URL = input ("Please Enter The URL : ")
    f = open("database1.dat","r")
    credentials = f.readline()
    f.close()
    (email,hkey) = credentials.split(" ")
    hkey = list(hkey)
    if "\n" in hkey:
        hkey.remove("\n")
    hkey = "".join(hkey)
    urlp = URL+hkey
    hurlp = hashlib.md5(urlp.encode())
    hurlp = hurlp.hexdigest()
    print ("The Password Generated is :"+hurlp)
    pyperclip.copy(hurlp)
    print("Copied into Clipboard...")
    hhurlp = hashlib.md5(hurlp.encode())
    hhurlp = hhurlp.hexdigest()
    f = open("database1.dat","a")
    f.write("\n"+URL)
    f.write(" ")
    f.write(hhurlp)
    f.close()
    return

def retrievepassword ():
    f = open("database.dat","r")
    print("\n"+"Passwords For These Websites Are Stored")
    counter  = 0
    for i in f:
        if counter != 0:
            (URL,hhurlp) = i.split(" ")
            hhurlp = list(hhurlp)
            if "\n" in hhurlp:
                hhurlp.remove("\n")
            hhurlp = "".join(hhurlp)
            URL = list(URL)
            if "\n" in URL:
                URL.remove("\n")
            URL = "".join(URL)
            print(str(counter)+") "+ URL)
        counter = counter+1
    f.close()

    num = input("\n"+"Please Insert The URL Number Which You Want The Password For : ")
    f = open("database.dat","r")
    num = int(num)
    if num >= counter:
        print("Sorry The Number You Have Selected Is Incorrect")
        return
    if num <= 0:
        print("Sorry The Number You Have Selected Is Incorrect")
        return
    counter = 0
    for i in f:
        if counter != 0:
            if counter == num:
                (URL,hhurlp) = i.split(" ")
                hhurlp = list(hhurlp)
                if "\n" in hhurlp:
                    hhurlp.remove("\n")
                hhurlp = "".join(hhurlp)
                URL = list(URL)
                if "\n" in URL:
                    URL.remove("\n")
                URL = "".join(URL)
        counter = counter+1
    f.close()
    f = open("database.dat","r")
    credentials = f.readline()
    f.close()
    (email,hkey) = credentials.split(" ")
    hkey = list(hkey)
    if "\n" in hkey:
        hkey.remove("\n")
    hkey = "".join(hkey)
    urlp = URL+hkey
    hurlp = hashlib.md5(urlp.encode())
    hurlp = hurlp.hexdigest()
    copy = hurlp
    phhurlp = hashlib.md5(copy.encode())
    phhurlp = phhurlp.hexdigest()
    if phhurlp == hhurlp:
        print ("The Password is :"+hurlp)
        pyperclip.copy(hurlp)
        print("Copied into Clipboard...")
    return


checker = True
while(checker):
    print("Password Manager System")
    option = input("Press 1 to SignUp, Press 2 to Login or Anyother to Exit : ")
    print("-----------------------------------------------------------------------------------------")
    if option == "1":
        signup()
        print("-----------------------------------------------------------------------------------------")
    
    elif option == "2":
        valid = login()
        if valid == True:
            checker2 = True
            while(checker2):
                option2 = input("Press 1 to Generate Password, Press 2 to Retrieve Password or Press # to Logout : ")
                if option2 == "1":
                    addpassword()
                    print("-----------------------------------------------------------------------------------------")
                elif option2 == "2":
                    retrievepassword()
                    print("-----------------------------------------------------------------------------------------")
                else:
                    checker2 = False
                    #print("-----------------------------------------------------------------------------------------")
        if valid != True:
            print("Login Failed")
        print("-----------------------------------------------------------------------------------------")
    
    else:
        checker = False
