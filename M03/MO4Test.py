a = 33
b = 200

if b > a:
    print(f"b({b}) is greater than a({a})") #functional string injects code into the print string

print("------------------------------")

#else if statement
a = 33
b = 32
if b > a:
    print(f"b({b}) is greater than a({a})")
elif a == b:
    print(f"a({a}) is equal to b({b})")
else:
    print(f"a: {a}\nb: {b}")

print("-----------------------------")

a = 200
b = 33
c = 500
if a > b and c > a:
    print(f"a({a}) is greater than b({b}) but less than c({c})")
