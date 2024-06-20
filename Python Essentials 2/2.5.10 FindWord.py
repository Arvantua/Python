def findWord(x="",y=""):
    x1=str(x).upper()
    y1=str(y).upper()
    pos=0
    for ch in x1:
        if y1.find(ch,pos)==(-1):
            return False
        else:
            pos= y1.find(ch,pos)+1
    
    return True
    

print(findWord("donor","Nabucodonosor"))
print(findWord("donut","Nabucodonosor"))





