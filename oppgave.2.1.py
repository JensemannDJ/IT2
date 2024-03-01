def bytt_plass(liste, i ,j):
    midlertidig = liste[i]
    liste[i]=liste[j]
    liste[j]=midlertidig

min_liste = [8,5,2,6,12]
bytt_plass(min_liste,1,3)
print(min_liste2)