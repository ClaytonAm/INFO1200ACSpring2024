print("Clayton Registration App")
print() #spacing
firstName = str(input("First name:")) #declares variable for first name input string
lastName = str(input("Last name:")) #declares variable for last name input string
birthYear = str(input("Enter your birth year:")) #declares variable for birth year input string
print() #spacing
print("Welcome: ", firstName, lastName) #concatenates welcome with vars, then prints
print("Registration is complete") #prints registration completion user feedback
tempPass = str(firstName + "*" + birthYear) #creates temp pass string by concatenating first name, asterisk, birth year
print("Your temporary password is: " + tempPass) #prints temp pass