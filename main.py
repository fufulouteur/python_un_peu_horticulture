
print("graines, terreau, pot, caisse ou exit : ")
pot = input()
if pot == 'pot':
    pot = int(input('combien de pots de fleurs ?: '))


print("graines, terreau, pot, caisse ou exit : ")
graines = input()
if graines == 'graines':
    graines = int(input('combien de graines ?: '))

print("graines, terreau, pot, caisse ou exit : ")
terreau = input()
if terreau == 'terreau':
    terreau = int(input('combien de terreau ?: '))

prix_pot = 4.00
prix_graines = 1.00
prix_terreau = 5.00
taux_TVA = 0.20

if print('caisse'):
    total_HT = 'pot' + 'terreau' + 'graines'
    print("total hors taxe : ")
    print(total_HT)

    total_TTC = total_HT + (total_HT * taux_TVA)
    print("montant a payer : ")
    print(total_TTC)

else:
    total_HT = (pot * prix_pot) + (graines * prix_graines) + (terreau * prix_terreau)
print("total hors taxe : ")
print(total_HT)

total_TTC = total_HT + (total_HT * taux_TVA)
print("montant a payer : ")
print(total_TTC)
