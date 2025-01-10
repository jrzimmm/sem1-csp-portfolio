#Init

#Functions

def bottles(bottleCount):
    if bottleCount == 1:
        print(str(bottleCount) + " bottle of non-alcoholic root beer on the wall")
        print(str(bottleCount) + " bottle of non-alcoholic root beer")
        print("Take one down, pass it around,")
        print(str(bottleCount - 1) + " bottles of non-alcoholic root beer on the wall")

    else:
        print(str(bottleCount) + " bottles of non-alcoholic root beer on the wall")
        print(str(bottleCount) + " bottles of non-alcoholic root beer")
        print("Take one down, pass it around,")
        print(str(bottleCount - 1) + " bottles of non-alcoholic root beer on the wall")

#Main

bottleCount=99
for x in range(99):
    #Runs 99 times, after 99 times, program stops.
    bottles(bottleCount)
    bottleCount = bottleCount-1
