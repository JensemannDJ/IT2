import os
import sys
import json
from politiker import Politiker

#1 oppsett

def rens_terminal():
    if sys.platform== "Wimdows":
        os.system("cls")
    else:
        os.system("clear")

with open("representanter.json", "r" , encoding="utf-8") as fil:
    data = json.load(fil)
representanter = data["dagensrepresentanter_liste"]

politikere =[]
for representant in representanter:
    ny_politiker = Politiker(representant)
    politikere.append(ny_politiker)

#2. Gameloop
while True:
    rens_terminal()
    print("--Stortinget-Fantsasy--")
    print()#printer tom linje
    print("1:Hvis politikeroversikt")
    print("2:Avslutt")

    brukervalg = input("> ")

    if brukervalg == "1":
        rens_terminal()
        print("--Politikeroversikt--")
        for politiker in politikere:
            print(politiker)
        print("Trykk enter for å gå tilbake til hovedmenyen")
        input()#pauser koden til til brukeren trykker enter
    elif brukervalg == "2":
        rens_terminal()
        print("avslutter..")
        break # hopper ut av løkken (avslutter spillet)
    else:
        rens_terminal()
        print("Ugyldig valg, trykk enter for å gå tilbake til hovedmenyen!")
        input()
print("takk for nå")