'''set={10,20,10,20,'python','java'}
print(len(set))
print(type(set))
print(id(set))
print(eval(input("Eneter any set:")))

set1={'pava','java','python'}
print(max(set1))
print(min(set1))

#METHODS (SET)

s1= {1,2,3,4,5}
s2= {4,5,6,7,8}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print((s1.symmetric_difference(s2)))
print(s1.intersection_update(s2))
print(s1)
print(s1.symmetric_difference_update(s2))
print(s1)

s1 = { 1,2,3,4,5,6,7,8,9,10}
s2 = {4,5,6,7}
print(s1.issubset(s2))
print(s2.issubset(s1))
print(s1.isdisjoint(s2))

s={1,2,3,4}
s.add('python')
print(s)
 

s.update(['java','php'])
print(s)

s.remove('java')
print(s)

#s.remove('java')
#print(s) 

s.discard('java')
print(s)   



#frozen set

l=[10,20,'python',30,'java']
fs=frozenset(l)
print(fs)'''



#Type casting

x = 10
print(x,type(x))

y = float(x)
print(y,type(y))







