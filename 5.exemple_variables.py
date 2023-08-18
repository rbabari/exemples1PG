# 1 - Listes
maListe = [1, 2, 3, 4, 5, 6]
print(maListe)
maListe.append(7)
maListe.remove(2)
print("Le type est : ", type(maListe))
print(maListe)

# 2 - tuples
maTuple = (1, 2, 3, 4, 5)
print(maTuple)
print("Le type est : ", type(maTuple))

# 3 - dictionnaires
dico = {"nom": "babari", "prenom": "raouf", "age": 33}
print(dico)
print("Le type est : ", type(dico))

# 4 - bool
estVisible = False
print(type(estVisible))
if not estVisible:
    print("c'est visible")

estVisible = True
print(type(estVisible))
if estVisible:
    print("c'est visible")

# 5 - none
p = None
print(type(p))