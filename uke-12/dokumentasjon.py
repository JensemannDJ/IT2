# som sier hvilken datatypen parametere
# skal ha og hvilken datatypen funksjoner
# returnerer
# fahrenheit :int sier at parameteren fahrenheit
# skaø være et int (heltall)
# -> float sier at funkjsone returnerer et float
# (desimaltall)
 
def fahrenheit_til_celcius(fahrenheit: int) -> float:
    return (fahrenheit - 32) * (5/9)  
 
# print 40 grader fahrenheit i celsius
 
print(fahrenheit_til_celcius(40))
 
# Docstrings er spesielle kommentarer som beskriver en
# klasse, en funksjon eller et program.
# de skrives mellom tre anførselstegn """ hei """ øverst i klassen/ funskjonen/ programmet
 
def celcius_til_fahrenheit(celsius: float) -> float:
    """
    en funksjon som konverterer celsius til fahrenheit
 
    parametere
        celsius (float): antall grader i celsius
    """
    return (9/5) * celsius  + 32
 
celcius_til_fahrenheit()
 
# Docstrings til en klasse:
 
class Elev:
    """
    Klasse for en elev på VGS
 
    attributter
        navn (str): navnet på eleven
        trinn (int): klassetrinnet til eleven
        klasse (str): bokstavklassen til eleven
        fag (list[str]): en liste med fag eleven tar
 
    metoder
        meld_opp_til_fag(fagnavn: str): Melder eleven opp til et fag
        dropp_ut_av_fag(fagnavn: str): fjerner et fag fra elevens fagliste
    
    """
    def __init__(self, navn: str, trinn: int, klasse: str):
        self.navn = navn
        self.trinn = trinn
        self.klasse = klasse
        self.fag = []
 
    def meld_opp_til_fag(self, fagnavn):
        self.fag.append(fagnavn)
 
    def dropp_ut_av_fag(self, fagnavn):
        self.fag.remove(fagnavn)
 
thor = Elev("Thor", 2, "STB")
ravi = Elev("Ravi", 2, "STG")
 