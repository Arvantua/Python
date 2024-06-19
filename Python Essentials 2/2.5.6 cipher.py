import sys
import os
def inputshift():
    shift= None
    while shift == None:

        try:
         shift=input("Shift eingeben (1-25, 0 für abbruch): ")
         shift = int(shift)

         if shift<0 or shift > 25:
              raise ValueError
         if shift==0:
               print("0: Abbruch! ")
               sys.exit()
         return shift
       # except SystemExit:
       #  print("Abbruch bei Shift-input! !")
       #  return 0
        except (ValueError,TypeError):
          shift=None
          print("Etwas ist schiefgelaufen. Bitte Bildschirm einschalten oder support anrufen! (Shift-input)")

def encrypt(x="",y=1):
   encr = ""                                    # wird das Ergebnis
   try:                                         # da wir casten kann immer was schiefgehen
      x=str(x)
      for ch in x:
        o = ord(ch)
        if ch.isalpha() == True:                # bearbeitung nur für Buchstaben (Groß- und Kleinbuchstaben)
            if ch.islower():                    # Prüfen, ob lowercase
               if (o+y)>ord("z"):               # gehen wir über "z" hinaus ?
                  o -= (ord("z")-ord("a")+1)    # dann zurückgehen auf "a"
            else:                               # else: uppercase Buchstabe
               if (o+y)>ord("Z"):               # gehen wir über "Z" hinaus ?
                  o -= (ord("Z")-ord("A")+1)    # dann zurückspringen auf "A"
            
            ch = chr(o+y)                       # Verschlüsseln des Buchstaben

        encr += ch                              # fügt verschlüsselte Buchstaben oder unveränderte andere zeichen dem Ergebnis hinzu
   except:
                                                # keine Ahnung ob das auch schöner geht ¯\_(ツ)_/¯
        print("Fehler ! Abbruch! (encryption)") 
        sys.exit() 
   return encr

def inputtext():
   return input("Zu verschlüsselnder Text: ")

def run():
   inp = inputtext()
   sh = inputshift()
   print(encrypt(inp,sh))

#  main:

#print(encrypt("abcxyzABCxyz 123",2))        # testcase 1
#print(encrypt("The die is cast",25))        # testcase 2
run()

