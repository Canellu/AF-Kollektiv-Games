
level = 1
vindu = [[1,2,3,4],
         [5,6,7,8],
         [1,2,3,4],
         [5,6,7,8]]

def printVindu(vindu):

    for rad in vindu:
        for element in rad:
            print("%2d" %(int(element)), end = ' ')
        print()

def fyllVindu(linje, vindu):

    for rad in range(len(vindu)):
        for element in range(len(vindu[rad])):
            vindu[rad][element] = int(linje.pop(1))


def beregn(vindu, start):


    def lagre(tall1, tall2):
        if tall1 % tall2 == 0:
            return tall1/tall2
        else:
            return tall1+tall2

    starten = int(start[0])
    rad1 = []
    rad2 = []
    rad3 = []
    rad4 = []

    #making all combinations and storing them in 4 lists
    for i in range(4):
        tmp1 = lagre(starten, vindu[0][i])
        rad1.append(tmp1)
        for j in range(4):
            tmp2 = lagre(tmp1, vindu[1][j])
            rad2.append(tmp2)
            for k in range(4):
                tmp3 = lagre(tmp2, vindu[2][k])
                rad3.append(tmp3)
                for l in range(4):
                    tmp4 = lagre(tmp3, vindu[3][l])
                    rad4.append(tmp4)

    ekteRute = False
    ruten = ""
    #check for a 1 rows
    for i in range(len(rad1)):
        if rad1[i] == 1:
            ekteRute = True
            ruten = ruten + str(starten) + " -> " + str(vindu[0][i]) + "\n"


    if ekteRute != True:
        for i in range(len(rad2)):
            if rad2[i] == 1:
                ekteRute = True
                tmp = divmod(i, 4)
                ruten = ruten + str(starten) + " -> " + str(vindu[0][tmp[0]]) + " -> " + str(vindu[1][tmp[1]]) + "\n"


    if ekteRute != True:
        for i in range(len(rad3)):
            if rad3[i] == 1:
                ekteRute = True
                tmp1 = divmod(i, 4)
                tmp = divmod(tmp1[0], 4)
                ruten = ruten + str(starten) + " -> " + str(vindu[0][tmp[0]]) + " -> " + str(vindu[1][tmp[1]]) + " -> " + str(vindu[2][tmp1[1]]) + "\n"


    if ekteRute != True:
        for i in range(len(rad4)):
            if rad4[i] == 1:
                ekteRute = True
                tmp2 = divmod(i, 4)
                tmp1 = divmod(tmp2[0], 4)
                tmp = divmod(tmp1[0], 4)
                ruten = ruten + str(starten) + " -> " + str(vindu[0][tmp[0]]) + " -> " + str(vindu[1][tmp[1]]) + " -> " + str(vindu[2][tmp1[1]]) + " -> " + str(vindu[3][tmp2[1]]) + "\n"


    minst = rad4[0]
    posisjon = 0
    if ekteRute != True:
        for x in range(len(rad4)):
            if rad4[x] < minst:
                minst = rad4[x] #x gir posisjon
        for x in range(len(rad4)):
            if minst == rad4[x]:
                posisjon = x
                tmp2 = divmod(posisjon, 4)
                tmp1 = divmod(tmp2[0], 4)
                tmp = divmod(tmp1[0], 4)
                ruten = ruten + str(starten) + " -> " + str(vindu[0][tmp[0]]) + " -> " + str(vindu[1][tmp[1]]) + " -> " + str(vindu[2][tmp1[1]]) + " -> " + str(vindu[3][tmp2[1]]) + "\n"



    f = open("AFrute.txt", "a+")

    level = starten
    print("\n\nLevel " + str(level) + ":\n" + ruten)
    tall = str(level)
    f.write("Level ")
    f.write(tall)
    f.write(":\n")
    f.write(ruten)
    f.write("\n")
    f.close()


def hovedprogram():
    svar = 0

    while svar != "exit":

        svar = input("linje: ")
        splitta = svar.split()
        if svar != "exit" and len(splitta) == 17:
            fyllVindu(splitta, vindu)
            print("\nStart: ", splitta)
            printVindu(vindu)
            beregn(vindu, splitta)



hovedprogram()
