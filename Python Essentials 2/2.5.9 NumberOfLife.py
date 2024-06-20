def qsum(x):
    erg = 0
    y =list(str(x))
    for i in range(len(y)):
        if str(y[i]).isdigit():
            erg += int(y[i])
    
    return erg

def numLife(x=""):
    if qsum(x) >=10:
        return numLife(qsum(x))
    else:
        return qsum(x)




print(numLife(19991229))
print(numLife("1999.12.29"))
print(numLife(20000101))
print(numLife("2000.01.01"))
print(numLife(input("Gib Datum ein, Format = Wayne: ")))