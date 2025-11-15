'''class Parent:
    city="Bhopal"
    def car(self):
        print("car from parent")
class child(Parent):
    pass
obj=child()
print(obj.city)
print(obj.car())'''


'''class parent:
    car = 'Mexon'
    def home(self):
        print("Home from parent")

class child(parent):
    car = 'Altroze'
    def home(self):
        print("Home from child")
obj = child()
print(obj.car)
print(obj.car)
obj.home() '''




'''class parent:
    car = 'Mexon'
    def home(self):
        print("Home from parent")

class child(parent):
    car = 'Altroze'
    def home(self):
        super().home()
        print("Home from child")
obj = child()
print(obj.car)
obj.home() '''



#multi-level


#3.
'''class father:
    def home(self):
        print("Home from father")
class Mother:
    def car(self):
        print("car ffrrom motheer")

    def home(self):
        print("home from mother")

class child(Mother,father):
    pass
obj=child()
obj.car()
obj.home()'''


'''class father:
    def home(self):
        print("Home from father")
        Mother.home(self)
class Mother:
    def car(self):
        print("car ffrrom motheer")

    def home(self):
        print("home from mother")
       

class child(father, Mother):
    pass
obj=child()
obj.car()
obj.home()'''




#4. Hierarchical

'''class parent:
    def home(self):
        print("home from parent")

    def car (self):
        print("car from parent")

    class child1(parent):
        pass
    class child2(parent):
        pass

    obj1=child1()
    obj2=child2()
    obj1.car()
    obj2.home()'''






#ABSTRACT 

'''from abc import ABC, abstractmethod
class Calculator(ABC):
    def add(self, a, b):
        print(a+b)
    def sub(self,a ,b ):
        print(a-b)
    def multi(self,a,b):
        print(a+b)

    @abstractmethod
    def div(self):
        pass
class junior(Calculator):
    pass
obj=junior()'''




'''class Parent:
    bank="HDFC"
    def add  (self):
        print("hello")
class child (Parent):
    pass
obj=child()
print(obj.bank)
obj.add()'''




class Parent:
    __bank="HDFC"
    def __add  (self):
        print("hello")
class child (Parent):
    pass
obj=child()
print(obj._Parent__bank)
obj._Parent__add()


                        

    