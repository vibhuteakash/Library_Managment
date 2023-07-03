class Book():
    avalablity=1
    def __init__(self,id,name,author):
        self.id=id
        self.name=name
        self.author=author
        Book.avalablity
        self.avalablity=Book.avalablity
    
    def __str__(self):
        data= str(self.id) +','
        data+=str(self.name) +','
        data+=str(self.author) +','
        data+=str(self.avalablity) 
        return data


