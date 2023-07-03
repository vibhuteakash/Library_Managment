from admin_activities import Admin
from user import User


ch=0
print('''************Hello and wellcome to the Library Managment System*******************
    Please select your Choice:
    1.Library Admin
    2.User
    3.Exit
    ''')

while(ch!=3):
    
    ch=int(input("Enter your choice: "))
    if(ch==1):
        print("Please login: ")
        username=input("Enter your username: ")
        password=input("Enter your password: ")
        if(username=='Admin' and password=='Admin123'):
            print("you logined successfully")
            print("Wellcome back Admin\n")
            Admin()
        else:
            print("Your login details are invalid\n")

    elif(ch==2):
        print("Please Login: ")
        username=input("Enter your username: ")
        password=input("Enter your password: ")
        if(username=='User' and password=='User123'):
            print("you logined successfully")
            print("Wellcome back\n")
            User()

        else:
            print("Your login details are invalid\n")
    
    elif(ch==3):
        print("you are logged out")
        print("thanks\nMeet you soon")
    
    else:
        print("Please enter correct choice")