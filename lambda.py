'''x=lambda p,q,r: p+q+r
x(10,20,30)
print(x(10,20,30))
z=x(10,20,30)'''


'''x=lambda p,q  : p if p>q else q
print(x(10,20))'''


'''f=open("a1.txt", 'a+')
data="This ia python class"
f.write(data)'''


f=open("a1.txt", 'a+')
data="This ia python class\n"
data1="This is java class\n"
data2="This is c class\n"
f.writelines([data,data1,data2])
f.close()

'''f=open("a1.txt", 'r+')
data=f.read()
print(data)
#f.close()
data1=f.read()
print("data1:",data1)'''


'''f=open("a1.txt",'r+')
data = f.read(10)
print(data)
data1=f.read(15)
print(data1)
'''


'''data= f.readline()
print(data)
f.close()'''

'''data=f.readlines()
print(data)
f.close()
'''

'''with open('a1.txt' ,'a+') as f:
    data='python'
    f.write(data)
    print(f.closed)
print(f.closed)'''




###################################### Cursor position #######################################################

with open( 'a1.txt', 'a+') as f:
    print(f.tell())



with open( 'a1.txt', 'r+') as f:
    print(f.tell())    
    data=f.read(10)
    print(data)
    print(f.tell())



