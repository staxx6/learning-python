a = 3
if a == 1:
    print("TRUE")
elif a == 2:
    print("nope")
else:
    print("perhaps")

#short versions
x = 1; a = 1; b = 2

var = (20 if x == 1 else 30) #Parenthesis not needed

print("x has the value 1" if x == 1 else "x isn't equal 1")

xyz = (a * 2 if (a > 10 and b < 5) else b * 2)