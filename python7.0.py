x = input("Enter any string: ")
y = x.lower()
a = y.find('not')
b = y.find('poor')
if b>a and a>0 and b>0:
    y = y[0:a]+'good'+y[b+4:]
    print(y)
else :
    print(x)

