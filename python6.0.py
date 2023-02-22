x = input("Enter any string: ").strip()
if len(x)>=3:
    if x.endswith('ing'):
        x = x+'ly'
    else :
        x = x + 'ing'
print(x)
