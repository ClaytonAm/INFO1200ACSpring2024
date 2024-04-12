a = "Apple"
if a.lower() == "apple":
    if a!= "Apple":
        print()
    elif a.upper == "APPLE":
        print()
    else:
        print()
else: 
    print()

#elif statements
if invoice_total >= 500:
    discount_percent = .2
elif invoice_total >= 250:
    discount_percent = .1
elif invoice_total > 0:
    discount_percent = 0
else:
    print("Invoice total must be greater than zero.")

#while statements
count = 0
while count < 10:
    print(count)
    count = count - 1
    if count < 0:
        break
count = 0
while count < 5:
    print(count)
    count = count + 1

#for statements
count = 0
for value in range(5):
    print(value)
