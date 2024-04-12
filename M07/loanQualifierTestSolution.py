def main():
    min_salary = 60000
    min_years = 5
    choice = "y"

    while choice.lower() == "y":
        salary = float(input("Enter Salary: "))        if salary >= min_salary:
            years = float(input("Enter # of years worked: "))
            if years >= min_years:
                print("Qualified!")
            else:
                print(f"You must have worked at least {min_years} years"
        else:
            print(f"You must have a salary more than ${min_salary}"

        print()  
        choice = input("Try again? (y or n): ")
        

if __name__ == "__main__":
    main()
