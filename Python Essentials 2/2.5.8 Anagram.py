def nospacelow(x):
    x=str(x)
    return x.replace(" ","").lower()

def strtolist(x):
    s=list(x)
    return sorted(s)
def ancheck (a="",b=""):
    a1 = strtolist(nospacelow(a))
    b1 = strtolist(nospacelow(b))
    if (len(a1) != len(b1)) or (len(a1)==0):
        return False
    for i in range(len(a1)):
        if a1[i] != b1[i]:
            return False
    return True

def run():
    in1 = input("Erster Text: ")
    in2 = input("Zweiter Text: ")
    if ancheck(in1,in2):
        print("YEP Anagram")
    else:
        print("NOP kein Anagram")


# print(ancheck("ab cdefg","bad cge f"))
run()
