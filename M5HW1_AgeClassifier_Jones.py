# CTI-110 
# M5HW1 - Age Classifier 
# Reginald Jones 
# November 22
#

def main():
    age = int(input('Please enter the age of the person: '))

    if age >=20:
        print('Person is a Adult.')
    elif age >=13:
        print('Person is a Teenager.')
    elif age >=1:
        print('Person is a Child.')
    else:
        print('Person is an Infant.')

main()
