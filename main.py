import datetime

mois = {1: ["janvier", 0], 2: ["fevrier", 3], 3: ["mars", 3], 4: ["avril", 6], 5: ["mai", 1], 6: ["Juin", 4],
        7: ["juillet", 6], 8: ["aout", 2], 9: ["septembbre", 5],
        10: ["octobre", 0], 11: ["novembre", 3], 12: ["decembre", 5]}

semaine = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]

annee = {16: 6, 17: 4, 18: 2, 19: 0, 20: 6, 21: 4}


def give_the_date(x):
    x = x.split("/")
    jj = int(x[0])
    mm = int(x[1])
    aaaa = int(x[2])
    ss = int(x[2][0:-2])
    soe = int(x[2][-2:])

    return jj, mm, aaaa, soe, ss


def leap_year(x):
    if x % 400 == 0:
        return True
    elif x % 100 == 0:
        return False
    elif x % 4 == 0:
        return True
    else:
        return False


#Debut du code
x = input("Saisissez une date avec le format jj/mm/aaa ")
jj, mm, aaaa, soe, ss = give_the_date(x)

if aaaa < 1600 and aaaa > 2199:
    print("Cette saisie est incorrecte, veuillez recommencer le processus")
elif jj > 31:
    print("Cette saisie est incorrecte, veuillez recommencer le processus")
else:
    soe = soe // 4 + soe + jj + mois[mm][1] + annee[ss]
    if leap_year(aaaa):
        if mm == 1 or mm == 2:
            soe = soe - 1
    jour = soe % 7

date = datetime.datetime.today()
year = int(date.year)
month = int(date.month)
day = int(date.day)

 #Optionnel
if aaaa<year :
    print("le %s était un %s" % (x, semaine[jour]))
elif aaaa==year :
    if mm<month :
        print("le %s était un %s" % (x, semaine[jour]))
    elif mm==month :
        if jj<day:
            print("le %s était un %s" % (x, semaine[jour]))
        elif jj==day:
            print("Aujourd'hui est un %s" % (semaine[jour]))
        else:
            print("le %s sera un %s" % (x, semaine[jour]))
    else:
        print("le %s sera un %s" % (x, semaine[jour]))
else:
    print("le %s sera un %s" % (x, semaine[jour]))