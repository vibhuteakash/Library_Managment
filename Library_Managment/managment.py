from books import Book
from os import path
from datetime import datetime , timedelta


class Book_mang():

    def Add_book(self,b):
       with open('Book_info','a') as fp:
           fp.write(str(b))
           fp.write('\n')
    
    def show_all(self):
        print("All Book details are:\n")
        if(path.exists('Book_info')):
            with open('Book_info','r') as fp:
                print(fp.read())
        else:
            print("file not exists")
    
    def search_id(self,id):
        data=[]
        with open('Book_info','r') as fp:
            for line in fp:
                data=line.split(',')
                if(data[0]==str(id)):
                    print('Record is present')
                    print(line)
                    break
            else:
                print("Record is not present")
    
    def search_name(self,name):
        data=[]
        with open('Book_info','r') as xp:
            for line in xp:
                data=line.split(',')
                if(data[1].lower()==name.lower()):
                    print('Record is present')
                    print(line)
                    break
            else:
                print("Record is not present")
    
    def edit_book(self,id):
        data=[]
        book_list=[]
        flag=False
        with open('Book_info','r') as fp:
            for line in fp:
                data=line.split(',')
                if(data[0]==str(id)):
                    flag=True
                    print('record is present')
                    ans=input("Do you want to edit name of the book(y/n)?: ")
                    if(ans.lower()=='y'):
                        name=input("Enter the new name of the book: ")
                        data[1]=name
                    
                    ans=input("Do you want to edit books author: ")
                    if(ans.lower()=='y'):
                        author=input("Enter the new author of the book: ")
                        data[2]=author
                    line=','.join(data)
                    book_list.append(line)
                     
                     
                else:
                    line=','.join(data)
                    book_list.append(line)
        if(flag):
            with open('Book_info','w') as fp:
                 for book in book_list:
                     fp.write(book)
            print("record is editted successfully")
        else:
            print("record is not present")
            print("file is not edited")
    
    def delete(self,id):
        flag=False
        data=[]
        new_list=[]
        with open('Book_info','r') as fp:
            for line in fp:
                data=line.split(',')
                if(data[0]==str(id)):
                    flag=True
                    print('record is present' )
                    print("now it will get deleted\n")
                else:
                    line=','.join(data)
                    new_list.append(line)
        if(flag):
            with open('Book_info','w') as fp:
                for book in new_list:
                    fp.write(book)
        else:
            print('record is not present')
            print("please enter correct id\n")
    
    def issue_book(self,id):
        data=[]
        flag=False
        book_list=[]
        with open('Book_info','r') as fp:
            for line in fp:
                data=line.split(',')
                if(data[0]==str(id)):
                    print('book id is correct')
 
                    if(data[3].strip('\n') =='1'):
                        flag=True
                        print("Book is available")
                    else:
                        print("book is not available")
                    break
                                    
            else:
                print('book id is wrong')
            
        if(flag):
            with open('Book_info','r') as fp:
                for line in fp:
                    data=line.split(',')
                    if(data[0]==str(id)):
                        name=input("Enter the name of borrower: ")
                        issuedate=input("Enter the issue date in this format(dd/mm/yyyy): ")
                        details=str(id) + ',' + str(data[1]) + ',' + name + ',' + issuedate
                        data[3]='0\n'
                        line=','.join(data)
                        book_list.append(line)
                    else:
                        line=','.join(data)
                        book_list.append(line)
            with open('issue_info','a') as xp:
                xp.write(details)
                xp.write('\n')
            print("Book is issued successfully")
            with open('Book_info','w') as fp:
                for line in book_list:
                    fp.write(line)
        else:
            print("Book is not issued")
                               
    
    def returnbook(self,id):
        flag=False
        data=[]
        list=[]
        info=[]
        with open('issue_info','r') as fp:
            for line in fp:
                data=line.split(',')
                if(data[0]==str(id)):
                    flag=True
                    print("book id is present\n")
                    
                    issuedate=data[3]
                    dateissue=issuedate.split('/')
                    dateissue=datetime(int(dateissue[2]) , int(dateissue[1]), int(dateissue[0]) )
                     
                    datesubmit=input("Enter the date of submit in this format(dd/mm/yyyy): ")
                    datesubmit=datesubmit.split('/')
                    datesubmit=datetime(int(datesubmit[2]) , int(datesubmit[1]) , int(datesubmit[0]) )
                    days=(datesubmit-dateissue).days
                    if(days>5):
                        fine=20*(days-5)
                        print("please pay the fine as you not return book on due date")
                        print('Fine=',fine,"rs")
                        print("book is returned")
                    else:
                        print('thank you for returning book in time')
                    
                else:
                    line=','.join(data)
                    list.append(line)
             
        
        
        if(flag):
            with open('issue_info','w') as xp:
             for Line in list:
                xp.write(Line)
                
            with open('Book_info','r') as fp:
                for line in fp:
                    data=line.split(',')
                    if(data[0]==str(id)):
                        data[3]='1\n'
                        line=','.join(data)
                        info.append(line)
                    else:
                        line=','.join(data)
                        info.append(line)
            with open('Book_info','w') as fp:
                for line in info:
                    fp.write(line)
                    
        else:
            print("book is not present ")
            print("book is not returned")



                
                
                
                






                

        
                    
             
        



                        


    
    
                     







                    

                

    
    
    
