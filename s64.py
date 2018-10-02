geheimnis = 1337
versuch = -1
zaehler = 0

while versuch != geheimnis:
    versuch = int(input("Raten Sie: "))

    if versuch < geheimnis:
        print("Zahl zu klein")

    if versuch > geheimnis:
        print("Zahl zu groß")

    zaehler = zaehler + 1

print("Super, Sie haben es in ", zaehler, "Versuchen geschaft!")