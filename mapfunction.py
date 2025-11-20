    #higher order function
'''l=[1,2,3,4,5]
def square(n):
    return n*n

ans=map(square,l)
print(tuple(ans))'''

######################################################################################
'''l=[1,2,3,4,5]
l1=[]
for i in l:
    l1.append(i*i)
print(l1)'''


######################################################################################
'''l=[1,2,3,4,5]
x=0
for i in l:
    l[x]=i*i
    x=x+1
print(l)  '''



'''l=[1,2,3,4,5]
def square(n):
    return n*n

ans=map(square,l)
print(list(ans))
print(tuple(ans))'''


'''l=[1,2,3,4,5]
l2=[3,4,5,6]
l3=[4,5]
def add(x,y,z):
    return x+y+z

res=map(add,l,l2,l3)
print(res)
'''


'''l1 ,l2, l3=[1,2,3,4] , [5,6,7,8] , [9,10,11,12]
def add(x,y,z):
    return x+y+z

print(list(map(add,l1,l2,l3)))'''


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Filter()
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#grade
'''s=[50,60,70,65,40,30,90]
def division(n):
    if n >= 60:
        return n

print(list(filter(division,s)))  '''


#even
'''n=eval(input("Enter a number:"))
def even(n):
    if n % 2== 0:
        return n
    
print(list(filter(even,n)))    '''


#odd
'''n=eval(input("Enter a number:"))
def odd(n):
    if n % 2 != 0:
        return n
    
print(list(filter(odd,n)))  '''


#String
'''s=input("Enter string:")
def vowel(n):
    if n in ('a','e','i','o','u','A','E','I','O','U'):
        return n
    
res = list(filter(vowel,s))
print(''.join(res)) '''   

#vowel
'''s=input("Enter string:")
v= c=0 
for i in s:
       if i in  ('a','e','i','o','u','A','E','I','O','U'):
            v=v+1
       elif i==' ':
            pass  
       else:
              c=c+1

print(v) '''  



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# REDUCE()
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


'''import functools
l=[1,2,3,4,5,6,7]
def sum(x,y):
    print(x,y)
    return x+y

res = functools.reduce(sum,l,0)
print(res)'''


#map
import functools
l=[10,5,20,7,25,8,2]
def max(x,y):
    if x>y:
        return x
    else:
        return y

res = functools.reduce(max,l)
print(res)  
    
