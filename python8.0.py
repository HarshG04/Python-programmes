def largest(string):
    length = len(string[0])
    y = string[0]
    for i in string:
        if length < len(i):
            length = len(i)
            y = i
    print(y,":",length)


x = input("Enter any string: ").split()
largest(x)