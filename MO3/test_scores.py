#!/usr/bin/env python3
print("Clayton Test Scores App")
# display a welcome message
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
total_score = 0       # initialize the variable for accumulating scores
score1 = int(input("Enter test score: ")) #input for score 1
score2 = int(input("Enter test score: ")) #input for score 2
score3 = int(input("Enter test score: ")) #input for score 3
total_score = score1 + score2 + score3 #calculates total score from 3 input scores

# calculate average score
average_score = round(total_score / 3)
             
# format and display the result
print("======================")
print("Your Scores:  ", score1, score2, score3) #prints message and concatenated scores
print("Total Score:  ", total_score,
      "\nAverage Score:", average_score) #prints messages and concatenates with total score and average score variables
print()
print("Bye")


