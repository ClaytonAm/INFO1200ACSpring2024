#!/usr/bin/env python3

TAX = 0.06

def sales_tax(t): #missing a colon
    sales_tax = t * TAX     #total needs to be named t because that's the argument passed to the function
    return sales_tax           #also TAX needs to be uppercase
                #now returns sales_tax properly
def main():
    print("Sales Tax Calculator\n")
    Total = float(input("Enter total: "))   #made Total a float so it can be multiplied by TAX
    total_after_tax = round(Total + sales_tax(Total), 2)    #capitalized Total. 
    print("Total after tax: ", total_after_tax) #missing underscore in total_after_tax
    
if __name__ == "__main__":      #__name__ only had one underscore on each side
    main()      #main needed to be lowercase. Object names are case-sensitive
