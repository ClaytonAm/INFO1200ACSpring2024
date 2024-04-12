#!/usr/bin/env python3

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return  scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    # calculate average score
    scores_total = 0
    for score in scores:
        scores_total += score
    scores.sort()
    average_score = scores_total/len(scores)

    low_score = min(scores)
    high_score = max(scores)
   
    # format and display the result
    print()
    print("Score total:       ", scores_total)
    print("Number of Scores:  ", len(scores))
    print("Average Score:     ", average_score)
    print("Low score:         ", low_score)
    print("High score:        ", high_score)
    print("Median score:      ", process_median(scores))

def process_median(scores):
    median_index = (len(scores) // 2) - 1
    #checks if even
    if (len(scores) % 2) == 0:
        median_score = (scores[median_index] + scores[median_index + 1]) / 2
    #checks if the number of indexes is odd
    elif (len(scores) % 2) != 0:
        median_score = scores[median_index]
        
    return median_score

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


