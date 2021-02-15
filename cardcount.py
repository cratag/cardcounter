import tkinter 

ventana = tkinter.Tk()
ventana.geometry("500x800")

etiqueta = tkinter.Label(ventana, text = "Cratag's Card Counter")


cartas = ["AD", "AT", "AC", "AP",
		  "KD", "KT", "KC", "KP",
		  "QD", "QT", "QC", "QP",
		  "JD", "JT", "JC", "JP",
		  "DD", "DT", "DC", "DP",
		  "ND", "NT", "NC", "NP",
		  "OD", "OT", "OC", "OP",
		  "SD", "ST", "SC", "SP",
		  "SSD", "SST", "SSC", "SSP",
		  "CD", "CT", "CC", "CP",
		  "CCD", "CCT", "CCC", "CCP",
		  "TD", "TT", "TC", "TP",
		  "DDD", "DDT", "DDC", "DDP"] #baraja completa
amount = 52 		 # cantidad de cartas
cardcount = 0 	 	 # contador de cartas



cartasrestantes = tkinter.Label(ventana, text = "Cartas restantes:") 
cartasrestantes.config(font =("Verdana", 14)) 
cartasrestantes.grid(column = 5)

# 	NUMERO DE CARTAS RESTANTES
cantidadcartas = tkinter.Label(ventana, text = amount) 
cantidadcartas.config(font =("Verdana", 24))
cantidadcartas.grid(column = 5)


numerodesuerte = tkinter.Label(ventana, text = "Número de suerte:") 
numerodesuerte.config(font =("Verdana", 14)) 
numerodesuerte.grid(column = 5, row = 4)

#	 CHANCE DE GANAR
chanceganar = tkinter.Label(ventana, text = cardcount) 
chanceganar.config(font =("Verdana", 30), bg = "gold")
chanceganar.grid(column = 5, row = 5)


#Funciones
def restar_carta():
    global amount
    amount -= 1
    cantidadcartas.config(text=amount)

def cardcount_add():
    global cardcount
    cardcount += 1
    chanceganar.config(text=cardcount)

def cardcount_substract():
    global cardcount
    cardcount -= 1
    chanceganar.config(text=cardcount)


#Funcion principal
def popCard(a,b):
    cartas.remove(a)
    b['state'] = tkinter.DISABLED
    global cant
    global cardcount
    if a == "AC" or a == "AD" or a == "AP"  or a == "AT"  or a == "KC"  or a == "KD" or a == "KP" or a == "KT" or a == "QC" or a == "QD" or a == "QT" or a == "QP" or a == "JC" or a == "JD" or a == "JT" or a == "JP"  or a == "DC" or a == "DD" or a == "DP" or a == "DT":
        restar_carta()
        cardcount_substract()
    elif a == "SC"  or a == "SD"  or a == "SP" or a == "ST"  or a == "OC"  or a == "OD" or a == "OP" or a == "OT" or a == "NC" or a == "ND" or a == "NT" or a == "NP":
        restar_carta()
    elif a == "SSC"  or a == "SSD"  or a == "SSP" or a == "SST"  or a == "CC"  or a == "CD" or a == "CP" or a == "CT" or a == "CCC" or a == "CCD" or a == "CCT" or a == "CCP" or a == "TC" or a == "TD" or a == "TT" or a == "TP" or a == "DDC" or a == "DDD" or a == "DDT" or a == "DDP":
        restar_carta()
        cardcount_add()


#CARTAS

#AS
AD = tkinter.Button(ventana, text= "A♦", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("AD", AD), state = tkinter.NORMAL)
AT = tkinter.Button(ventana, text= "A♣", padx = 6, pady = 18, command = lambda: popCard("AT", AT), state = tkinter.NORMAL)
AC = tkinter.Button(ventana, text= "A♥", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("AC", AC), state = tkinter.NORMAL)
AP = tkinter.Button(ventana, text= "A♠", padx = 6, pady = 18, command = lambda: popCard("AP", AP), state = tkinter.NORMAL)

#KING
KD = tkinter.Button(ventana, text= "K♦", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("KD", KD), state = tkinter.NORMAL)
KT = tkinter.Button(ventana, text= "K♣", padx = 6, pady = 18, command = lambda: popCard("KT", KT), state = tkinter.NORMAL)
KC = tkinter.Button(ventana, text= "K♥", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("KC", KC), state = tkinter.NORMAL)
KP = tkinter.Button(ventana, text= "K♠", padx = 6, pady = 18, command = lambda: popCard("KP", KP), state = tkinter.NORMAL)

#QUEEN
QD = tkinter.Button(ventana, text= "Q♦", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("QD", QD), state = tkinter.NORMAL)
QT = tkinter.Button(ventana, text= "Q♣", padx = 6, pady = 18, command = lambda: popCard("QT", QT), state = tkinter.NORMAL)
QC = tkinter.Button(ventana, text= "Q♥", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("QC", QC), state = tkinter.NORMAL)
QP = tkinter.Button(ventana, text= "Q♠", padx = 6, pady = 18, command = lambda: popCard("QP", QP), state = tkinter.NORMAL)

#JACK
JD = tkinter.Button(ventana, text= "J ♦", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("JD", JD), state = tkinter.NORMAL)
JT = tkinter.Button(ventana, text= "J ♣", padx = 6, pady = 18, command = lambda: popCard("JT", JT), state = tkinter.NORMAL)
JC = tkinter.Button(ventana, text= "J ♥", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("JC", JC), state = tkinter.NORMAL)
JP = tkinter.Button(ventana, text= "J ♠", padx = 6, pady = 18, command = lambda: popCard("JP", JP), state = tkinter.NORMAL)

#DIEZ
DD = tkinter.Button(ventana, text= "10♦", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("DD", DD), state = tkinter.NORMAL)
DT = tkinter.Button(ventana, text= "10♣", padx = 6, pady = 18, command = lambda: popCard("DT", DT), state = tkinter.NORMAL)
DC = tkinter.Button(ventana, text= "10♥", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("DC", DC), state = tkinter.NORMAL)
DP = tkinter.Button(ventana, text= "10♠", padx = 6, pady = 18, command = lambda: popCard("DP", DP), state = tkinter.NORMAL)

#NUEVE
ND = tkinter.Button(ventana, text= "9♦", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("ND", ND), state = tkinter.NORMAL)
NT = tkinter.Button(ventana, text= "9♣", padx = 6, pady = 18, command = lambda: popCard("NT", NT), state = tkinter.NORMAL)
NC = tkinter.Button(ventana, text= "9♥", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("NC", NC), state = tkinter.NORMAL)
NP = tkinter.Button(ventana, text= "9♠", padx = 6, pady = 18, command = lambda: popCard("NP", NP), state = tkinter.NORMAL)

#OCHO
OD = tkinter.Button(ventana, text= "8♦", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("OD", OD), state = tkinter.NORMAL)
OT = tkinter.Button(ventana, text= "8♣", padx = 6, pady = 18, command = lambda: popCard("OT", OT), state = tkinter.NORMAL)
OC = tkinter.Button(ventana, text= "8♥", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("OC", OC), state = tkinter.NORMAL)
OP = tkinter.Button(ventana, text= "8♠", padx = 6, pady = 18, command = lambda: popCard("OP", OP), state = tkinter.NORMAL)

#SIETE
SD = tkinter.Button(ventana, text= "7♦", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("SD", SD), state = tkinter.NORMAL)
ST = tkinter.Button(ventana, text= "7♣", padx = 6, pady = 18, command = lambda: popCard("ST", ST), state = tkinter.NORMAL)
SC = tkinter.Button(ventana, text= "7♥", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("SC", SC), state = tkinter.NORMAL)
SP = tkinter.Button(ventana, text= "7♠", padx = 6, pady = 18, command = lambda: popCard("SP", SP), state = tkinter.NORMAL)

#SEIS
SSD = tkinter.Button(ventana, text= "6♦", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("SSD", SSD), state = tkinter.NORMAL)
SST = tkinter.Button(ventana, text= "6♣", padx = 6, pady = 18, command = lambda: popCard("SST", SST), state = tkinter.NORMAL)
SSC = tkinter.Button(ventana, text= "6♥", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("SSC", SSC), state = tkinter.NORMAL)
SSP = tkinter.Button(ventana, text= "6♠", padx = 6, pady = 18, command = lambda: popCard("SSP", SSP), state = tkinter.NORMAL)

#CINCO
CD = tkinter.Button(ventana, text= "5♦", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("CD", CD), state = tkinter.NORMAL)
CT = tkinter.Button(ventana, text= "5♣", padx = 6, pady = 18, command = lambda: popCard("CT", CT), state = tkinter.NORMAL)
CC = tkinter.Button(ventana, text= "5♥", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("CC", CC), state = tkinter.NORMAL)
CP = tkinter.Button(ventana, text= "5♠", padx = 6, pady = 18, command = lambda: popCard("CP", CP), state = tkinter.NORMAL)

#CUATRO
CCD = tkinter.Button(ventana, text= "4♦", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("CCD", CCD), state = tkinter.NORMAL)
CCT = tkinter.Button(ventana, text= "4♣", padx = 6, pady = 18, command = lambda: popCard("CCT", CCT), state = tkinter.NORMAL)
CCC = tkinter.Button(ventana, text= "4♥", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("CCC", CCC), state = tkinter.NORMAL)
CCP = tkinter.Button(ventana, text= "4♠", padx = 6, pady = 18, command = lambda: popCard("CCP", CCP), state = tkinter.NORMAL)

#TRES
TD = tkinter.Button(ventana, text= "3♦", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("TD", TD), state = tkinter.NORMAL)
TT = tkinter.Button(ventana, text= "3♣", padx = 6, pady = 18, command = lambda: popCard("TT", TT), state = tkinter.NORMAL)
TC = tkinter.Button(ventana, text= "3♥", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("TC", TC), state = tkinter.NORMAL)
TP = tkinter.Button(ventana, text= "3♠", padx = 6, pady = 18, command = lambda: popCard("TP", TP), state = tkinter.NORMAL)

#DOS
DDD = tkinter.Button(ventana, text= "2♦", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("DDD", DDD), state = tkinter.NORMAL)
DDT = tkinter.Button(ventana, text= "2♣", padx = 6, pady = 18, command = lambda: popCard("DDT", DDT), state = tkinter.NORMAL)
DDC = tkinter.Button(ventana, text= "2♥", foreground = "red", padx = 6, pady = 18, command = lambda: popCard("DDC", DDC), state = tkinter.NORMAL)
DDP = tkinter.Button(ventana, text= "2♠", padx = 6, pady = 18, command = lambda: popCard("DDP", DDP), state = tkinter.NORMAL)

#LAYOUT
AD.grid(row = 0, column = 0)
AT.grid(row = 0, column = 1)
AC.grid(row = 0, column = 2)
AP.grid(row = 0, column = 3)

KD.grid(row = 1, column = 0)
KT.grid(row = 1, column = 1)
KC.grid(row = 1, column = 2)
KP.grid(row = 1, column = 3)

QD.grid(row = 2, column = 0)
QT.grid(row = 2, column = 1)
QC.grid(row = 2, column = 2)
QP.grid(row = 2, column = 3)

JD.grid(row = 3, column = 0)
JT.grid(row = 3, column = 1)
JC.grid(row = 3, column = 2)
JP.grid(row = 3, column = 3)

DD.grid(row = 4, column = 0)
DT.grid(row = 4, column = 1)
DC.grid(row = 4, column = 2)
DP.grid(row = 4, column = 3)

ND.grid(row = 5, column = 0)
NT.grid(row = 5, column = 1)
NC.grid(row = 5, column = 2)
NP.grid(row = 5, column = 3)

OD.grid(row = 6, column = 0)
OT.grid(row = 6, column = 1)
OC.grid(row = 6, column = 2)
OP.grid(row = 6, column = 3)

SD.grid(row = 7, column = 0)
ST.grid(row = 7, column = 1)
SC.grid(row = 7, column = 2)
SP.grid(row = 7, column = 3)

SSD.grid(row = 8, column = 0)
SST.grid(row = 8, column = 1)
SSC.grid(row = 8, column = 2)
SSP.grid(row = 8, column = 3)

CD.grid(row = 9, column = 0)
CT.grid(row = 9, column = 1)
CC.grid(row = 9, column = 2)
CP.grid(row = 9, column = 3)

CCD.grid(row = 10, column = 0)
CCT.grid(row = 10, column = 1)
CCC.grid(row = 10, column = 2)
CCP.grid(row = 10, column = 3)

TD.grid(row = 11, column = 0)
TT.grid(row = 11, column = 1)
TC.grid(row = 11, column = 2)
TP.grid(row = 11, column = 3)

DDD.grid(row = 12, column = 0)
DDT.grid(row = 12, column = 1)
DDC.grid(row = 12, column = 2)
DDP.grid(row = 12, column = 3)


# INSTRUCCIONES DE USO
instrucciones = tkinter.Label(ventana, text = "INSTRUCCIONES: BLACKJACK") 
instrucciones.config(font =("ARIAL BLACK", 14)) 
instrucciones.grid(column = 5, row = 8)
instrucciones = tkinter.Label(ventana, text = "El número de suerte está en 0 al comienzo") 
instrucciones.config(font =("ARIAL BLACK", 10)) 
instrucciones.grid(column = 5, row = 9)
instrucciones = tkinter.Label(ventana, text = "Mientras más alto, más deberías apostar:") 
instrucciones.config(font =("ARIAL BLACK", 10)) 
instrucciones.grid(column = 5, row = 10)
instrucciones = tkinter.Label(ventana, text = "Hay más chances de cartas altas") 
instrucciones.config(font =("ARIAL BLACK", 10)) 
instrucciones.grid(column = 5, row = 11)
instrucciones = tkinter.Label(ventana, text = "Si está negativo, deberías irte") 
instrucciones.config(font =("ARIAL BLACK", 10)) 
instrucciones.grid(column = 5, row = 12)
ventana.mainloop()

import tkinter as tk





#     cardSeen()

# def cardSeen():
#     print(cartas)
#     card = input()
#     if card in cartas:
#         popCard(card)
#     elif card == "end" or card == "END":
#         print("Mano terminada.")
#     else: 
#         print("No está esa carta.")
#         cardSeen()
