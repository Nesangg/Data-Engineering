#Prints vowels of a string

def Checker(string, vowels):
    Output = [each for each in string if each in vowels]
    print("Vowels: ",Output)
     

string = "nEsan"
vowels = "AaEeIiOoUu"

Checker(string.lower(), vowels);


