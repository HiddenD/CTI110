# find the area of a rectangle
# given its width and height
# norrisa
# cti 110
# 6/12/17
	
# in future we will start using a main() function
# this is an example of how that works
# for now, just look at the code inside 'def main()'
def main():
    print ("This program will calculate the area " + \
           "of a rectangle.")
    width = int(input("Enter the width: "))
    height = int(input("Enter the height: "))
    
    # A = W * H
    area = width * height
	    
    # give the answer
    print("The area is:",area)

# code outside the def main() will run first, 
# so the program starts here and jumps to main()
main()
