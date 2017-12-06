# This program is used to test the Average and Submit a Grade
# 12/6/2017
# CTI-110 M7HW1 - Test Average and Grade
# Reginald Jones
#

def main():
    #This will prompt the user to input 5 different scores
    score1 = int(input("Please enter score for the first grade: "))
    score2 = int(input("Please enter score for the second grade: "))
    score3 = int(input("Please enter score for the third grade: "))
    score4 = int(input("Please enter score for the fourth grade: "))
    score5 = int(input("Please enter score for the fifth grade: "))
    
    # This will add all 5 scores then divide by 5 to get the average
    average = (score1 + score2 + score3 + score4 + score5) / 5

    # Print out the test score
    print ("Your average score is: ", average)

    #After all scores are added it will then match the average score with the rubic listed below
    if average > 90:
        print("Your passing!")

    elif average > 80:
        print("Your doing great!")

    elif average > 70:
        print("Not bad.")

    elif average > 60:
        print ("You may want to study just a bit more...")

    elif average < 60:
        print ("Your not passing...")

main()
