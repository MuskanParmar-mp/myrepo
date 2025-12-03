'''def natural_no(n):
    if n==0:
        return
    print(n)
    natural_no(n-1)
    
n=int(input("enter a no:"))  
natural_no(n)'''



#even number
'''def even_no(n):
    if n == 0:
        return
    even_no(n-1)
    if n % 2 == 0:
        print(n)

n = int(input("enter a no: "))
even_no(n)'''


#sum of natural no
# def sum_natural(n):
#     if n==1:
#         return 1
    
#     return n+ sum_natural(n-1)

# n=int(input("Enetr a no:"))
# res = sum_natural(n)
# print(res)



#sum of even no
'''def sum_natural(n):
    if n==1:
        return 2*n
    
    return 2*n+ sum_natural(n-1)

n=int(input("Enetr a no:"))
res = sum_natural(n)
print(res)'''



#sum of natural no
def sum_natural(n):
    if n==1:
        return 2*n -1
    
    return 2*n+ sum_natural(n-1)

n=int(input("Enetr a no:"))
res = sum_natural(n)
print(res)
    
