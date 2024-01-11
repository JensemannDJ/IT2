land= input("hvilket land kommer du fra?")

if land== "Norge":
    print("du får 0.44$ per sang")
elif land ==" Sverige":
    print("Du får 0.34$ per sang")
else:
    print(" du får 0.22$ per sang")

stream=int(input("Hvor mange streamer har du?"))

if stream > 30000000:
    print("Du tjener 70% av pengrer tjent av sangen")
elif stream > 1400000:
    print("Du tjener 40% av penge tjent påm sangen ")
else:
    ("DU TJENER INGEN TING")

    