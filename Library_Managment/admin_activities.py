from books import Book
from managment import Book_mang


 
mang=Book_mang()
def Admin():
    ch=0
     
    while(ch!=7):
        print('''Admin activities are as follow: 
        1.Add Books
        2.Show all Book details
        3.search book on the basis of book id.
        4.search book on the basis of book name
        5.edit book details using book id
        6.delete book using book id.
        7.Exit
        ''')
        ch=int(input("Enter the your choice: "))
        if(ch==1):
            id=int(input("Enter the book id: "))
            name=input("Enter the book name: ")
            author=input("Enter the books author: ")
            b=Book(id,name,author)
            mang.Add_book(b)
        
        elif(ch==2):
            mang.show_all()
        
        elif(ch==3):
            id=int(input("Enter the book id to find the book details: "))
            mang.search_id(id)
        
        elif(ch==4):
            name=input("Enter the book name to find the book details: ")
            mang.search_name(name)
        
        elif(ch==5):
            id=int(input("enter the id of the book to edit the book details: "))
            mang.edit_book(id)
        
        elif(ch==6):
            id=int(input("Enter the id to delete the book details: "))
            mang.delete(id)
        
        elif(ch==7):
            print("you are now came out of the Admin Activities Dashboard\n")
        
        else:
            print("Please select the correct choice")
    
