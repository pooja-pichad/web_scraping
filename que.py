def resister():
    db=open("database.txt","r")
    usrename=input("create username:")
    password=input("create password: ")
    password1=input("confirm password: ")

    d=[]
    f=[]
    for i in db:
        a,b=i.split(",")
        b=b.strip()
        d.append(b)
        f.append(b)
    data=dict(zip(d,f))
    print(data)
    if password != password1:
        print("password dont match ,resatart..")
        resister()
    else:
        if len (password)<=6:
            print("password too short , restart")
        elif usrename in d:
            print("username exits")
        else:
            db= open("database.txt","a")
            db.write(usrename+" ,"+password+"\n")
            print("success...")
            # db.write()
            # print(db)
resister()
# def access():
#     username1=input("enter a name: ")
#     password2=input("enter a password: ")
#     if not len (username1 or password2)<1:
#         d=[]
#         f=[]
#         for i in db:
#             a,b=i.split(",")
#             b=b.strip()
#             d.append(b)
#             f.append(b)
#         data=dict(zip(d,f))
#         try:
#             if data[username1]:
#                 try:
#                     if

