# Dictionary me galat key
'''student = {"name": "Muskan"}
print(student["age"])'''


# List me galat index
'''numbers = [1, 2, 3]
print(numbers[5])'''



# List Operations Program (Intentional Errors)

'''numbers = [10, 20, 30]

for i in range(5):  # Error: loop index 3,4 out of range
    print("Value:", numbers[i])

# TypeError: Adding number and string
result = numbers[0] + "50"
print(result)'''





# File Program (Intentional Errors)

'''file_name = "data.txt"
f = open(file_name)  # FileNotFoundError (agar file na ho)

content = f.read()
f.close()

print(Content) '''  # NameError: Wrong variable name case sensitive
