while True:
    print("Hva heter du? ")
    navn = input("> ") # -> Jens Hallingstad Blymke
    navn_liste = navn.split(" ") # -> ["Jens", "Hallingstad", "Blymke"]
    if len(navn_liste) >= 2:
        break
    print("Ugyldig navn. Navnet må minst inneholde to navn")
 
fornavn = navn_liste[0]
første_bokstav_etternavn = navn_liste[-1][0]
mail = f"{fornavn}{første_bokstav_etternavn}@afk.no" # -> jensb@afk.no
mail = mail.lower() # -> jensb@afk.no
print(mail)