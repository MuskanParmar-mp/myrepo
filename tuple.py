#TUPLE
mytuple= ("muskan", "prachi", "ankit", "harsh")
mytuple1 = ("muskan", "prachi", "ankit", "harsh")
print(id(mytuple), id(mytuple1))
print(type(mytuple))

tuple=(10,20,30,40,'python')
print(len(tuple))      #5
print(id(tuple))      #id
print(type(tuple))      #<class 'tuple'>
print(sum(tuple))       #error

t=('java','python','php')
print(min(t))        #java
print(max(t))        #python

t=(10+5j , 20+3j)
print(sum(t))                   #(30+8j)


t=((1,2,3), (1,3,4), (1,4,5))
print(max(t))                            #(1, 4, 5)
print(min(t))     
print(sum(t))                      #(1, 2, 3)

t=(1,2,3,'python',1,2,1,2)
print(t.index(2))                       #1
print(t.count(2))                       #3






