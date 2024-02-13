print("Clayton Pay Check Calculator App")
hoursWorked = int(input("Hours Worked: ")) #declares var for hours worked input integer
payRate = float(input("Hourly pay rate: ")) #declares var for pay rate input float
print() #spacing
grossPay = hoursWorked * payRate #calculates gross pay
print("Gross pay: " + str(grossPay)) #concatenates gross pay with text and prints
taxRate = 0.18 #declares var for tax rate
print("Tax rate: ", taxRate, "%") #concatenates tax rate with text and prints
taxAmount = grossPay * taxRate #calculates tax amount from pay and rate
print("Tax amount: ", taxAmount) #concatenates text with tax amount and prints
takeHomePay = round(grossPay - taxAmount, 2) #declares var and calculates take home pay
print("Take home pay: ", takeHomePay) #concatenates text with take home pay and prints