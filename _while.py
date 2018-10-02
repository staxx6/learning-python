a = 1
while a == 1:
    print("stuff")
    if False:
        break
    a = a + 1;
else:
    print("a != 0") # not printed if "break" stops the while-loop