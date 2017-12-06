#Reginald Jones
#M7T1 - Kilometer Converter
#CTI 110
#
#This program is used to convert Kilometers to Miles

CONVERSION_FACTOR = 0.6214 #Global Statement

def main():
    #Input to get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    #This display the distance converted to miles
    show_miles(kilometers)

#Kilometers will be converted to miles and displayed on screen
    
def show_miles(km):
    #This calculate the miles.
    miles = km * CONVERSION_FACTOR

    #This will display the miles
    print(km, 'kilometers equals', miles, 'miles.')

main()
