
while True:
    try:
        alder = int(input("hvor gammel blir du i år"))
        if alder >= 0:
            break
        print("Ugyldig tall, prøv igjen")
    except:
        print("Ugyldig input,prøv igjen")
år_nå=2024
fødselsår = år_nå - alder
print(f"Du er født i {fødselsår}")