#Print largest number

def max_num(x,y,z):
    if (x > y) and (x > z):
        largest = x
    elif (y > x) and (y > z):
        largest = y
    else:
        largest = z
    print("The Largest Number is:",largest) 

max_num(5,15,9)