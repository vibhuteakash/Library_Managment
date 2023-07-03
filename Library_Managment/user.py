from books import Book
from managment import Book_mang

mang=Book_mang()

def User():
    ch=0
    print("Wellcome to the User Dashboard\n")
    while(ch!=6):
        print('''User Acitivities are as follow:
        1.show all book details.
        2.search book on the basis of book id
        3.search book on the basis of book name
        4.issue the book to user using book id
        5.return the book.
        6.exit
        ''')
        ch=int(input("Enter the choice: "))
        if(ch==1):
            mang.show_all()
        
        elif(ch==2):
            id=int(input("Enter the book id to search the book details: "))
            mang.search_id(id)
        
        elif(ch==3):
            name=input("Enter the book name to search the book details: ")
            mang.search_name(name)
        
        elif(ch==4):
            id=int(input("Enter the book id to issue the book: "))
            mang.issue_book(id)
        
         
        elif(ch==5):
            id=input("Enter the book id to return the book: ")
            mang.returnbook(id)
        
        elif(ch==6):
            print("You are now out of User Dashboard\n")
        
        else:
            print("Please enter the correct choice\n")