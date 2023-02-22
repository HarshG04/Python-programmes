x = input("Enter any string: ")
y = x[0]
x = x.replace(y,"$")
x = y + x[1:]
print(x)