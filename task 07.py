#covert celsius to fahrenheit


degree_sign = u"\N{DEGREE SIGN}"

def conv(c):
    fahrenheit=(c * 9/5) + 32
    #celsius = (c - 32) * 5/9
    #print("Celsius entered:       ",c,degree_sign, "C")
    #fahrenheit=(fahrenheit,degree_sign,"F")
    return fahrenheit
    #print("Convert to celsius:   ",celsius,degree_sign, "C")
print(conv(50));

#covert fahrenheit to celsius
def conv2(c):
    #fahrenheit=(c * 9/5) + 32
    celsius = (c - 32) * 5/9
    #print("Fahrenheit entered:    ",c,degree_sign, "F")
    #print("Convert to fahrenheit:",fahrenheit,degree_sign, "F")
    #celsius=(celsius + degree_sign +"C")
    return celsius
print(conv2(120));