import random                                                                                                           #Skráin er opnuð
with open("kindur.txt") as kindur:
    frsl = kindur.read().split("  ")
randomicer = random.sample(range(52), 52)                                                                               #Spilin eru stokkuð til að randomica þau og listarnir eru búnir til
player1spil = []
cpuspil = []
player1 = []
cpu = []
Jafntefli = []
for x in randomicer:
    if x % 2 == 0:
        cpuspil.append(x)
    else:
        player1spil.append(x)
for x in player1:													#spilin eru sett í annaðhvort
    player1.append(frsl[x])
for x in cpu:
    cpu.append(frsl[x])
while len(cpu) > 0 and len(player1) > 0:
    print("Leikmaður á að gera")
    print(player1)
    spil = player1[0].split("  ")
    spil1 = cpu[0].split("  ")
    print("1: Þyngd")                                                                                                   #Hérna eru flokkarnir skrifaðir út
    print("2: Mjólkurlagni")
    print("3: Einkunn ullar")
    print("4: Fjöldi afkvæma")
    print("5: Einkunn læris")
    print("6: Frjósemi")
    print("7: þykkt bakvöðva")
    print("8: Einkunn")
    print("Efsta spilið er:")
    print(spil)
    val = int(input("Veldu 1-8 "))                                                                                      #sýnt er fyrsta spil í bunkanum og er leyft þér að velja hvað þú vilt gera
    flokkur1 = spil[1].split(",")
    print(flokkur1[val - 1])
    flokkur2 = spil1[1].split(",")
    if (flokkur2[val - 1]) > (flokkur1[val - 1]):
        print("Cpu vann")
        print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
        if len(Jafntefli) > 0:
            for kindur1 in Jafntefli:
                cpu.append(kindur1)
            Jafntefli.clear()
        cpu.append(cpu[0])
        cpu.remove(cpu[0])
        cpu.append(player1[0])
        player1.remove(player1[0])
        print(player1)
    if (flokkur1[val - 1])(flokkur2[val - 1]):
        print("Leikmaður vann")
        print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
        if len(Jafntefli) > 0:
            for kindur1 in Jafntefli:
                player1.append(kindur1)
            Jafntefli.clear()
        player1.append(player1[0])
        player1.remove(player1[0])
        player1.append(cpu[0])
        cpu.remove(cpu[0])
        print(cpu)
    else:
        print("Jafntefli")
        Jafntefli.append(player1[0])
        Jafntefli.append(cpu[0])
        player1.remove(player1[0])
        cpu.remove(cpu[0])
        print(Jafntefli)
        print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
        print("cpu á að gera")
        val = random.randint(0, 7)
        flokkur1 = spil[1].split(",")
        flokkur2 = spil1[1].split(",")
        Jafntefli = []
    if (flokkur1[val]) > (flokkur2[val]):
        print("Leikmaður vann")
        print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
        if len(Jafntefli) > 0:
            for kindur1 in Jafntefli:
                player1.append(kindur1)
            Jafntefli.clear()
        player1.append(player1[0])
        player1.remove(player1[0])
        player1.append(cpu[0])
        cpu.remove(cpu[0])
    if (flokkur2[val]) > (flokkur1[val]):
        print("Cpu vann")
        print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
        if len(Jafntefli) > 0:
            for kindur1 in Jafntefli:
                cpu.append(kindur1)
            Jafntefli.clear()
        cpu.append(Jafntefli)
        cpu.append(cpu[0])
        cpu.remove(cpu[0])
        cpu.append(player1[0])
        player1.remove(player1[0])
        print(player1)
    else:                                                                                                               #hérna er skrifað hver sigurvegarinn er eða hvort það var jafntefli.
        print("jafntefli")
        Jafntefli.append(player1[0])
        Jafntefli.append(cpu[0])
        print(Jafntefli)
        print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
if len(player1) == 0:
    print("Cpu vann")
    print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
elif len(cpu) == 0:
    print("Leikmaður vann")
    print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
