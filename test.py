

print("Bienvenue sur le tournoi de Graven. \nQuel est votre pseudo?")
pseudo = input("Entrez votre pseudo : ")
print("Quel est votre mot de passe", pseudo, " ?")
forbidden_words = ["Nutella", "Kichta", "Cool"]
print("Les mots suivants: ",forbidden_words,  "ne peuvent pas être votre mot de passe.")
mot_de_passe = input("Entrez votre mot de passe: \n")
fort =  13
iword = "Nutella" "Kichta" "Cool"
while mot_de_passe in iword:
    print("Vous ne pouvez pas mettre ce mot en mot de passe")
    mot_de_passe = input("Entrez votre mot de passe: ")
    if mot_de_passe in iword:
        continue
    else:
        break
if mot_de_passe == iword:
    input("Entrez votre mot de passe: ")
if len(mot_de_passe) < 7:
    print("Mot de passe trop court.")
if 6 < len(mot_de_passe) < 12:
    print("Mot de passe correct!")
if len(mot_de_passe) >= 13:
    print("Mot de passe fort")
if len(mot_de_passe) <= fort:
    manquant = fort - len(mot_de_passe)
    print("Il vous manque ", manquant, "caractéres pour avoir un mot de passe fort")
else:
    print("Mot de passe parfait de {}".format(len(mot_de_passe)), " caractéres")
