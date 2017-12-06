# This Program is used to measure Feet to Inches
# 12/6/17
# CTI-110 M7T2_FeetToInches 
# Reginald Jones
#

#Number of Inches per Foot 
INCHES_PER_FOOT = 12

def main():
    #Get a number of feet from the user.
    feet = int(input('Enter a number of feet: '))

    #Converts to inches
    print(feet, 'feet equals', feet_to_inches(feet), 'inches.')

#This function is used to convert feet to inches.
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

main()
