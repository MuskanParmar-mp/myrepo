'''class student:
    def __init__(self,name,rollno):
        self.n= name
        self.r=rollno
obj=student()        
obj.c='12345


class student:
    def __init__(self,name,rollno):
        self.n=name
        self.r=rollno
    def addnew(self,contact):
        self.c=contact

obj=student('Muskan',19)
obj.addnew(123444425) 
obj.school='SHSS'   



class student:
    def __init__(self,name,rollno):
        self.n= name
        self.r=rollno
        print(self.n,self.r)
    def addnew (Self,contact):
        self.c=contact
        print(self.n,self.r,self.c)

obj=student('muskan',123)
obj.addnew(31974)
print(obj.n,obj.c,obj.r)    '''


#calling of class variable

'''class student:
    school ='BBPS'
    def __init__(self,name,rollno):
        self.n=name
        self.r=rollno
        print(student.school)
        student.principal='python'
    def addnew(self):
        student.school_code=101
    def show(self):
        print(student.school,student.principal,student.school_code)
    @classmethod
    def create_or_update(cls):
        print(student.school,student.principal,student.school_city)
obj=student("muskan",111)                    
obj.addnew()
obj.show()
student.school_city="Bhopal"
obj.create_or_update()
print(student.school)'''






'''class Student:
    def __init__(self,name,rollno):
        self.n=name
        self.r=rollno
        x=10
        print(x)
    def show(self):
        y=10
        print(y)
        print(x) 
    obj=Student ('sneha',102)
    obj.show()       
'''



'''class Book:
    price=100
    def __init__(self,title,branch):
        self.t=title
        self.b= branch

    obj = Book('python book', 'IT')
    print(obj,price)
    obj2=Book('python book' )    
    print(obj2.price)'''


class student:
    x=10
    def __init__(self,name):
        self.n=name
        
       
