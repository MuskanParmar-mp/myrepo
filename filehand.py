# f = open("a1.txt", "a")
# f.write("i am ankit  ")
# f.write("muskan")
# print(f)
# print(type(f))
# print(f)
# f.close()

# f = open("a1.txt", "r+")
# f.write("web develop")
# print(f.read())
# f.close()



#      READ         
'''f = open("a1.txt")
print(f.mode)
print(f.writable())   #false
print(f.readable())    #true
print(f)
print(f.closed)'''


'''f = open('a1.txt','r+')
print(f.name)                 #a1
print(f.mode)                 #r+
print(f.writable())             #True
print(f.readable())             #True
print(f.closed)
print(f.encoding)'''


# write  #

'''f = open("a1.txt", "w")
print(f.mode)          #w
print(f.writable())   #True
print(f.readable())    #False
print(f)
print(f.closed)


f = open('a1.txt','w+')
print(f.name)                 # a1.txt
print(f.mode)                 #w+
print(f.writable())            #True
print(f.readable())             #True
print(f.closed)                  #false
print(f.encoding)      '''           #cp1252



# append() 
'''f = open("demo.txt", "a")
print(f.name)                  #demo.txt
f.write("\nI want ms")
print(f.writable())             #True
print(f.readable())               #False
print(f.closed)  '''           


f = open('demo.txt','a+')
print(f.name)                  #demo.txt
print(f.mode)                   # a+
print(f.writable())            # True
print(f.readable())             # True
print(f.closed)               
print(f.encoding)                 # cp1252





 

