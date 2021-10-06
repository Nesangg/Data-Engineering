#covert celsius to fahrenheit


degree_sign = u"\N{DEGREE SIGN}"

def conv(c):
    fahrenheit=(c * 9/5) + 32
    return fahrenheit
    
print(conv(50));

#covert fahrenheit to celsius
def conv2(c):
    celsius = (c - 32) * 5/9
    return celsius
    
print(conv2(120))