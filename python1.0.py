def length(string):
    count = 0
    for i in string:
        count += 1
    return count

x = input("Enter any String: ")
y = length(x)
print("length:",y)