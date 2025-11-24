'''list = [10,20,30,'python','java']
print(list , type(list))      

print(len(list))      #5
print(type(list))     #<class 'list>
print(id(list))       #1566523547840
print(list)           #[10, 20, 30, 'python', 'java']

print(max(list))      #error
print(min(list))      #error
print (sum(list))     #error

list1 = ['python', 'java' , 'PHP']
print(max(list1))      #python
print(min(list1))      #PHP 

l= [10,20,30,20.5,10+5j]
#print(max(l))         #error
#print(min(l))         #error
print(sum(l))          #(90.5+5j)


#methods in list

l=[2,4,6,'python','java']

l1 = l.copy()
print(l , l1, id(l), id(l1))      #[2, 4, 6, 'python', 'java'] [2, 4, 6, 'python', 'java'] 1534231142592 1534231290944

l.clear()
print(l)                           #[]
print(id(l))                       #2087154114752

del(l)                            #used for revoming the object 
print(l)  

s='python'
print(s)
del(s)
print(s)

l=[2,4,6,'python','java']
l.append('php')                           #[2, 4, 6, 'python', 'java', 'php']
print(l)

l.append([1,2,3,4])                       #[2, 4, 6, 'python', 'java', 'php', [1, 2, 3, 4]]
print(l)


l=[2,4,6,'python']
l.extend([1,3,5,'jave'])
print(l)

l=[1,2,4,5,8]
l.insert(0,100)
print(l)

l.insert(100,'python')
print(l)

l.insert(2,[10,20,30,40])

list = [2,4,6,8,'java']
list.pop()
print(list)

print(list.pop(0))
print(list.pop(5))

list = [2,4,6,8,'java' ,6,6]
list.remove(6)
print(list)


list = [2,4,6,8,'java' ,6,6]
firstele = list.index(6)
secele = list.index(6,(firstele+2))
print(secele)

list=[2,1,2,3,2,5]
print(list.count(2))
print(list.count(100))

list=[2,1,2,3,2,5]
list.sort()
print(list)

list.reverse()
print(list)'''

#list.sort(reverse=True)
#print(list)




