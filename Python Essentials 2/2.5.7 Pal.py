

def nospace(x):
    x=str(x)
    return x.replace(" ","")
    

def palCheck(z=""):
    y= str(z).lower()
    y = nospace(y)
    if y=="":
        pal = False
    else:
        pal = True
    for a in range(int(len(y)/2)):
        if y[a] != y[(-a-1)]:
            
            pal= False
            break
    if pal==True:
        print("YEP Palindrom! : ", z)
    else:
        print("Kein Palindrom! : ",z)



palCheck("Ten animals I slam in a net")
palCheck("Eleven animals I slam in a net ")
palCheck(input("Gib Text: "))