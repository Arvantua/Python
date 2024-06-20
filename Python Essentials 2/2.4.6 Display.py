a0 = ['### ','# # ','# # ','# # ','### ']
a1 = ['  # ','  # ','  # ','  # ','  # ']
a2 = ['### ','  # ','### ','#   ','### ']
a3 = ['### ', '  # ','### ','  # ','### ']
a4 = ['# # ','# # ','### ','  # ','  # ']
a5 = ['### ','#   ','### ','  # ','### ']
a6 = ['### ','#   ','### ','# # ','### ']
a7 = ['### ','  # ','  # ','  # ','  # ']
a8 = ['### ','# # ','### ','# # ','### ']
a9 = ['### ','# # ','### ','  # ','### ']
numbers = [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9]


row0=""
row1=""
row2=""
row3=""
row4=""
display=[row0,row1,row2,row3,row4]

def numberapp(nmbr):
    for i in range(5):
        #display[i].append(numbers[nmbr][i])
        display[i]=display[i]+numbers[nmbr][i]
    
def printdisplay(dsp):
    for i in range(5):
        print(display[i]) 
    
def cleardisplay():
    for i in range(5):
        display[i]=""
def generatedisplay(n):
    cleardisplay()
    n=str(n)
    for ch in n:
        numberapp(int(ch))

generatedisplay(123456789)
printdisplay(display)
