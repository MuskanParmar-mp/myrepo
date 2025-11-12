'''with open('n1.txt','ab+') as f:
    print(f.tell())
    data =b"this is python class"

    f.write(data)
    print(f.tell())

    data1 = f.read()
    print(data1)
    f.seek(0,0)
    print(f.tell())
    data2=f.read(20)
    print(data2)
    print(f.tell())'''


with open('n1.txt','rb+') as f:
    print(f.tell())
    f.read(10)
    print(f.tell())
    f.seek(-5,1)
    print(f.tell())