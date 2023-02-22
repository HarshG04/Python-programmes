x = input("Enter any string: ").strip()
y = input("Enter other string: ").strip()
z = y[0:2] + x[2:] + ' ' + x[0:2] + y[2:]
print(z)