#Prints common characters

def characters(x,y):
    str1=x.lower()
    str2=y.lower()
    s=list(set(str1)&set(str2))
    print("The common letters are:")
    for i in s:
        print(i)

#str1 = "CoDe".lower()
#str2 = "Nesan".lower()

characters("nEsancol", "colEtte");