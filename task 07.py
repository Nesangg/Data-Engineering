#covert a number to celsius and fahrenheit


degree_sign = u"\N{DEGREE SIGN}"

def conv(c):
    fahrenheit=(c * 9/5) + 32
    celsius = (c - 32) * 5/9
    print("Number entered:       ",c)
    print("Convert to fahrenheit:",fahrenheit,degree_sign, "F")
    print("Convert to celsius:   ",celsius,degree_sign, "C")


conv(63)