#!/usr/bin/env python3
import csv, os

def write_trips(trips):
    with open('trips.csv', 'w', newline='') as file:   #opens the csv so we can actually write to it
        writer = csv.writer(file)   #csv writer object
        writer.writerows(trips)     #write the trip data to the csv. Each trip just takes one row.

def read_trips():
    trips = []      #creates the list to pass values to
    with open("trips.csv", newline='') as file:     #open the csv
        for row in csv.reader(file):    #iterate over each row (trip) in the csv
            trips.append(row)       #appends the trips list with each row of the csv
    return trips

def list_trips(trips):
    print("  Distance\t Gallons\tMPG")      #prints the heading labels. Formatted weird so it looks nicer in the console.
    for index, trip in enumerate(trips, start=1):       #iterate over each trip in the list, add a number for each
        print(f"{index}. {trip[0]} \t {trip[1]}\t\t{trip[2]}")  #print each data point from that trip(with numbering)

def get_miles_driven():
    while True:     #this is basically the same code but I made it more readable because it was confusing me
        miles_driven = float(input("Enter miles driven: "))
        if miles_driven <= 0:
            print("Entry must be greater than zero. Please try again.")
        else:
            return miles_driven
          
def get_gallons_used():
    while True:     #this is basically the same code but I made it more readable because it was confusing me
        gallons_used = float(input("Enter gallons of gas: "))
        if gallons_used <= 0:
            print("Entry must be greater than zero. Please try again.")
        else:
            return gallons_used

def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    trips = read_trips()    #calls read_trips, returns the trips list

    if trips:       #if there is trip data in the csv,
        print("Existing trips:")
        list_trips(trips)       #print it to the console
        print()

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        trips.append([miles_driven, gallons_used, mpg]) #adds the user entered info to the trips list
        
        more = input("More entries? (y or n): ")

    write_trips(trips)  #writes the trips list to the csv file
    print()
    print("All Trips:")
    list_trips(trips)   #prints the updated trips list.
    
    print("Bye!")

if __name__ == "__main__":
    main()

