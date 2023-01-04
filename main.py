pot = int(input('combien de pots de fleurs ?: '))
graines = int(input('combien de sachets de graines ?: '))
terreau = int(input('combien de sacs de terreau ?: '))

prix_pot = 4.00
prix_graines = 1.00
prix_terreau = 5.00
taux_TVA = 0.20

total_HT = (pot * prix_pot) + (graines * prix_graines) + (terreau * prix_terreau)
print("total hors taxe : ")
print(total_HT)

total_TTC = total_HT + (total_HT * taux_TVA)
print("montant a payer : ")
print(total_TTC)
