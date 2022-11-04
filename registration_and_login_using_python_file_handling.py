def register():
    db = open("data_file.txt", "r")
    a = input("Enter username as __@__.__")
    z = []
    for i in db:
        x = i.split(",")
        z.append(x[0])
    if a in z:
        print("Try another username")
        register()
    if ((a.index('@')) - (a.index('.'))) == -1:
        print("Enter correctly!")
        register()
    if a.count('@') != 1 and a.count('.') != 1:
        print("Check again please")
        register()
    if a[0] == '1' or a[0] =='2' or a[0] =='3' or a[0] == '4' or a[0] == '5' or a[0] == '6' or a[0] =='7' or a[0] == '8' or a[0] =='9':
        print("Characters are only allowed")
        register()
    if a[0] == '@' or a[0] == '$' or a[0] == '_' or a[0] == '%' or a[0] == '!' or a[0] == '#' or a[0] == '*':
        print("Characters are only allowed")
        register()
    else:
        print("Hurray!Username Created")

    b = input("Create your password with least one capital letter one integer and one special character: ")
    s = False

    if len(b) < 5:
        print("Passwords length should be greater than 5")
        register()
    if len(b) > 16:
        print("passwords length should be less than 16")
        register()

    if len(b) > 5 and len(b) < 16:
        l, u, p, d = 0, 0, 0, 0
        for i in b:
            if i.isdigit():
                d += 1
            if i.islower():
                l += 1
            if i.isupper():
                u += 1
            if (i == '@' or i == '$' or i == '_' or i == '%' or i == '!' or i == '#' or i == '*' or i == '&'):
                p += 1
            if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(b)):
                s = True

    if s:
        c = input("Confirm Password: ")
        while (c != b):
            print("Password not match, Try Again")
            c = input("Try Again: ")

    else:
        print("Try again")
        register()

    file = open("data_file.txt", "a")
    file.write(a + "," + b + "\n")
    file.close()
    login()
def login():
    A = input("Enter your Username to login: ")
    A = A.strip()
    db = open("data_file.txt", "r")
    z = []
    for i in db:
        x = i.split(",")
        z.append(x[0])

    if A in z:
        B=input("Please Enter your password: ")
        B=B.strip()
        file=open("data_file.txt","r").readlines()
        for x in file:
            x=x.strip()
            info=x.split(",")
            if z==A and b==B:
                print("Welcome in the digital world")
                welcome()
            else:
                welcome()
                L = input("Forgot Password [Y/N] : ")

                if L == "N":
                    print("try")
                    login()

                if L == "Y":
                    b = input("Create your new password with least one capital letter one integer and one special character: ")
                    s = False

                    if len(b) < 5 and len(b) > 16:
                        print("Create Password with length between 5 an 16, Try Again")
                        register()

                    if len(b) > 5 and len(b) < 16:
                        l, u, p, d = 0, 0, 0, 0
                        for i in b:
                            if i.isdigit():
                                d += 1
                            if i.islower():
                                l += 1
                            if i.isupper():
                                u += 1
                            if (
                                    i == '@' or i == '$' or i == '_' or i == '%' or i == '!' or i == '#' or i == '*' or i == '&'):
                                p += 1
                            if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(b)):
                                s = True

                    if s:
                        c = input("Confirm Password: ")
                        while (c != b):
                            print("Password not match, Try Again")
                            c = input("Try Again: ")

                    else:
                        print("Sorry,Try again to login")
                        login()

                    file = open("data_file.txt", "w")
                    file.write(A + "," + b + "\n")
                    file.close()

    else:
        print("Unregister user you need to register first")
        register()

def welcome():
    print("WELCOME TO GUVI")
    print("If you already have an account please login,otherwise please register ")
    W=input("Login|Register[L/R]: ")
    if W=="L":
        login()
    elif W=="R":
        register()
    else:
        print("Enter correctly")
        welcome()
welcome()
