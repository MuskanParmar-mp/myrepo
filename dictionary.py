'''dic={'name': 'Muskan','age':'37'}
print(dic,type(dic)) 
print(len(dic))
print(id(dic))
print(dic)
print(max(dic))
print(min(dic))

d ={4:'Muskan',5:19}
print(min(d))                #4
print(max(d))    '''            #5




# METHODS XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx


d= {'name':'muskan', 'age':37, 'qualification':'M.tech'}

print(d)
print(d.get('name'))
print(d.get('Name'))
print(d.get('Name','Guest'))

print(d.keys())
print(d.values())
print(d.items())

d2={'x':10, 'y': 20}
d.update(d2)
print(d)
print(d2)


#SET DEFAULT

d.setdefault(('name','rahul'))
print(d)    


d.setdefault(('name','rahul'))

print(d)
print(d)
print(d)
print(d)
print(d)
print(d)
print(d)
print(d)