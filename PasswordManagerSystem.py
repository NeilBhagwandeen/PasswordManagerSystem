#imports start
from tkinter import*
import hashlib
import winsound
import pyperclip
#imports ends


#function starts
def clickSignupButton ():
    loginButton.place(x = 1000, y = 1000)
    signupButton.place(x = 1000, y = 1000)
    urlLable.place(x = 1000, y = 1000)
    backButton.place(x = 10, y = 10)
    label.place(x = 1000, y = 1000)
    emailEntry.place(x = 440, y = 200)
    labels1.place(x =300, y = 200)
    passwordEntry.place(x = 440, y = 300)
    labels2.place(x =300, y = 300)
    saveButton.place(x = 440, y = 400)
    addButton.place(x = 1000, y = 1000)
    descriptionText.place(x = 1000, y = 1000)
    searchButton.place(x = 1000, y = 1000)
    removeButton.place(x = 1000, y = 1000)
    return

def clickSaveButton ():
    email = str(emailEntry.get())
    password = str(passwordEntry.get())
    key = email+password
    hkey = hashlib.md5(key.encode())
    f = open("database.dat","w+")
    f.write(email)
    f.write(" ")
    f.write(hkey.hexdigest())
    f.close()
    emailEntry.delete(first = 0, last = 1000)
    passwordEntry.delete(first = 0, last = 1000)
    loginButton.place(x = 440, y = 300)
    signupButton.place(x = 440, y = 200)
    backButton.place(x = 1000, y = 1000)
    label.place(x = 30, y = 10)
    emailEntry.place(x = 1000, y = 1000)
    labels1.place(x =1000, y = 1000)
    passwordEntry.place(x = 1000, y = 1000)
    labels2.place(x =1000, y = 1000)
    saveButton.place(x = 1000, y = 1000)
    urlLable.place(x = 1000, y = 1000)
    addButton.place(x = 1000, y = 1000)
    descriptionText.place(x = 1000, y = 1000)
    searchButton.place(x = 1000, y = 1000)
    removeButton.place(x = 1000, y = 1000)
    return

def clickBackButton ():
    emailEntry.delete(first = 0, last = 1000)
    passwordEntry.delete(first = 0, last = 1000)
    loginButton.place(x = 440, y = 300)
    signupButton.place(x = 440, y = 200)
    backButton.place(x = 1000, y = 1000)
    label.place(x = 30, y = 10)
    emailEntry.place(x = 1000, y = 1000)
    labels1.place(x =1000, y = 1000)
    passwordEntry.place(x = 1000, y = 1000)
    labels2.place(x =1000, y = 1000)
    saveButton.place(x = 1000, y = 1000)
    login2Button.place(x = 1000, y = 1000)
    urlLable.place(x = 1000, y = 1000)
    addButton.place(x = 1000, y = 1000)
    descriptionText.place(x = 1000, y = 1000)
    searchButton.place(x = 1000, y = 1000)
    removeButton.place(x = 1000, y = 1000)
    return

def clickLoginButton ():
    loginButton.place(x = 1000, y = 1000)
    signupButton.place(x = 1000, y = 1000)
    label.place(x = 1000, y = 1000)
    backButton.place(x = 10, y = 10)
    passwordEntry.place(x = 440, y = 300)
    labels2.place(x = 300, y = 300)
    login2Button.place(x = 440, y = 400)
    urlLable.place(x = 1000, y = 1000)
    addButton.place(x = 1000, y = 1000)
    descriptionText.place(x = 1000, y = 1000)
    searchButton.place(x = 1000, y = 1000)
    removeButton.place(x = 1000, y = 1000)
    return

def clickLogin2Button ():
    f = open("database.dat","r")
    credentials = f.readline()
    f.close()
    (email,hkey) = credentials.split(" ")
    hkey = list(hkey)
    if "\n" in hkey:
        hkey.remove("\n")
    hkey = "".join(hkey)
    password = str(passwordEntry.get())
    key = email+password
    phkey = hashlib.md5(key.encode())
    phkey = phkey.hexdigest()
    if phkey != hkey:
        winsound.Beep(3000,1000)
        loginButton.place(x = 440, y = 300)
        signupButton.place(x = 440, y = 200)
        label.place(x = 30, y = 10)
        backButton.place(x = 1000, y = 1000)
        passwordEntry.place(x = 1000, y = 1000)
        labels2.place(x = 1000, y = 1000)
        login2Button.place(x = 1000, y = 1000)
        passwordEntry.delete(first = 0, last = 1000)
        urlLable.place(x = 1000, y = 1000)
        addButton.place(x = 1000, y = 1000)
        descriptionText.place(x = 1000, y = 1000)
        searchButton.place(x = 1000, y = 1000)
        removeButton.place(x = 1000, y = 1000)
    else:
        loginButton.place(x = 1000, y = 1000)
        signupButton.place(x = 1000, y = 1000)
        label.place(x = 1000, y = 1000)
        passwordEntry.place(x = 1000, y = 1000)
        labels2.place(x = 1000, y = 1000)
        login2Button.place(x = 1000, y = 1000)
        passwordEntry.delete(first = 0, last = 1000)
        urlLable.place(x = 50, y = 200)
        passwordEntry.place(x = 200, y = 200)
        addButton.place(x = 200, y = 250)
        searchButton.place(x = 200, y = 300)
        removeButton.place(x = 200, y = 350)
        descriptionText.place(x = 513, y = 3)
    return

def clickAddButton ():
    URL = str(passwordEntry.get())
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
    pyperclip.copy(hurlp)
    descriptionText.delete('1.0', END)
    p = "Your Password Generated For:"+"\n"+URL+"\n"+hurlp+"\n"+"Copied To Clipboard ..."
    descriptionText.insert("end-1c", p)
    hhurlp = hashlib.md5(hurlp.encode())
    hhurlp = hhurlp.hexdigest()
    f = open("database.dat","a")
    f.write("\n"+URL)
    f.write(" ")
    f.write(hhurlp)
    f.close()
    passwordEntry.delete(first = 0, last = 1000)
    return

def clickSearchButton ():
    check = 0
    url = str(passwordEntry.get())
    f = open("database.dat","r")
    for i in f:
        (URL,hhurlp) = i.split(" ")
        hhurlp = list(hhurlp)
        if "\n" in hhurlp:
            hhurlp.remove("\n")
        hhurlp = "".join(hhurlp)
        URL = list(URL)
        if "\n" in URL:
            URL.remove("\n")
        URL = "".join(URL)
        if url == URL:
            check = 1
            ff = open("database.dat","r")
            credentials = ff.readline()
            ff.close()
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
                pyperclip.copy(hurlp)
                descriptionText.delete('1.0', END)
                p = "Your Password For:"+"\n"+URL+"\n"+hurlp+"\n"+"Copied To Clipboard ..."
                descriptionText.insert("end-1c", p)
    if check == 0:
        descriptionText.delete('1.0', END)
        p = "No Password Stored For:"+"\n"+url
        descriptionText.insert("end-1c", p)
    passwordEntry.delete(first = 0, last = 1000)
    return

def clickRemoveButton ():
    s = []
    f = open("database.dat","r")
    for i in f:
        s.append(i)
    f.close()
    a = 0
    b = -1
    toDelete = (str(passwordEntry.get()))
    for i in s:
        if toDelete in i:
            b = a
        a = a+1
    if b != -1:
        s.pop(b)
        f = open("database.dat","w+")
        for i in s:
            f.write(i)
        descriptionText.delete('1.0', END)
        p = "Password Deleted For:"+"\n"+toDelete
        descriptionText.insert("end-1c", p)
    else:
        descriptionText.delete('1.0', END)
        p = "No Password For:"+"\n"+toDelete
        descriptionText.insert("end-1c", p)
    passwordEntry.delete(first = 0, last = 1000)
    return
    

#function ends


#main starts

window = Tk()
window.title("Password Manager System")
window.geometry("960x540")
window.config(bg = "#242424")

signupButton = Button(window, text = "Signup", font = ("Serif",14), command = clickSignupButton, relief = "groove", bg = "#242424", fg = "#f5cb5c")
signupButton.config(height = 1, width = 8)
signupButton.place(x = 440, y = 200)

loginButton = Button(window, text = "Login", font = ("Serif",14), command  = clickLoginButton, relief = "groove", bg = "#242424", fg = "#f5cb5c", activebackground = "#242424")
loginButton.config(height = 1, width = 8)
loginButton.place(x = 440, y = 300)

emailEntry = Entry(window, font = ("Serif",14))
emailEntry.place(x = 1000, y = 1000)

passwordEntry = Entry(window, font = ("Serif",14))
passwordEntry.place(x = 1000, y =1000)

saveButton = Button(window, text = "Save", font = ("Serif",14), command = clickSaveButton, relief = "groove", bg = "#242424", fg = "#f5cb5c", activebackground = "#242424")
saveButton.config(height = 1, width = 8)
saveButton.place(x = 1000, y = 1000)

login2Button = Button(window, text = "Login", font = ("Serif",14), command = clickLogin2Button,relief = "groove", bg = "#242424", fg = "#f5cb5c", activebackground = "#242424")
login2Button.config(height = 1, width = 8)
login2Button.place(x = 1000, y = 1000)

backButton = Button(window, text = "Back", font = ("Serif",14), command = clickBackButton, relief = "groove", bg = "#242424", fg = "#f5cb5c", activebackground = "#242424")
backButton.config(height = 1, width = 8)
backButton.place(x = 1000, y = 1000)

label = Label(window, text = " ", font = ("Serif",50), bg = "#242424", fg = "#f5cb5c", activebackground = "#242424")
label.config(height = 1, width = 23)
label.place(x = 30, y = 10)
label.config(text = "Password Manager System")

labels1 = Label(window, text = "Email :*", font = ("Serif",14), bg = "#242424", fg = "#f5cb5c", anchor = "e")
labels1.config(height = 1, width = 12)
labels1.place(x = 1000, y = 1000)

labels2 = Label(window, text = "Password :*", font = ("Serif",14), bg = "#242424", fg = "#f5cb5c", anchor = "e")
labels2.config(height = 1, width = 12)
labels2.place(x = 1000, y = 1000)

urlLable = Label(window, text = "URL :*",  font = ("Serif",14), bg = "#242424", fg = "#f5cb5c", anchor = "e")
urlLable.config(height = 1, width = 12)
urlLable.place(x = 1000, y = 1000)

descriptionText = Text(window,  font = ("Serif",14), bg = "#242424", fg = "#ff5d73", relief = "groove", width = 40)
descriptionText.place(x = 1000, y = 1000)

addButton = Button(window, text = "Add", font = ("Serif",14), command = clickAddButton, relief = "groove", bg = "#242424", fg = "#f5cb5c", activebackground = "#242424")
addButton.config(height = 1, width = 8)
addButton.place(x = 1000, y = 1000)

searchButton = Button(window, text = "Search", font = ("Serif",14), command = clickSearchButton, relief = "groove", bg = "#242424", fg = "#f5cb5c", activebackground = "#242424")
searchButton.config(height = 1, width = 8)
searchButton.place(x = 1000, y = 1000)

removeButton = Button(window, text = "Remove", font = ("Serif",14), command = clickRemoveButton,relief = "groove", bg = "#242424", fg = "#f5cb5c", activebackground = "#242424")
removeButton.config(height = 1, width = 8)
removeButton.place(x = 1000, y = 1000)

window.mainloop()
#main ends