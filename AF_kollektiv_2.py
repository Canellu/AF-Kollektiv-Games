import time
import cv2
import numpy as np

from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController



mouse = MouseController()
keyboard = KeyboardController()


brett = [[0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]

def taScreen():


    #mouse.position = (1595, 1365)
    #mouse.click(Button.left, 1)
    time.sleep(0.35)
    with keyboard.pressed(Key.shift):
        keyboard.press(Key.print_screen)
        keyboard.release(Key.print_screen)
    time.sleep(0.165)

def klikkBrett(brettet):

    delay = 0.005
    listen = [] #liste for alle 36 verdier i brettet
    for i in range(len(brettet)):
        listen += brettet[i]

    #start posisjon
    x = 1570
    y = 400

    for i in range(36):

        if i % 6 == 0 and i != 0:
            x = 1570
            y += 140

        mouse.position = (x, y)

        if listen[i] == '1':
            mouse.click(Button.left, 1)
        if listen[i] == '2':
            mouse.click(Button.left, 2)

        x += 140
        time.sleep(delay)

def lesBildet():

    path = r'C:\Users\Anton\Desktop\test.png'
    img = cv2.imread(path)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.imshow("Test", img)
    x = 70
    y = 70

    linje = ""
    for i in range(36):

        if i % 6 == 0 and i != 0:
            x = 70
            y += 150
            linje += " "

        #HSV: blaa = 95, gul = 24
        if hsv[y][x][0] == 95:
            linje += '1'
        elif hsv[y][x][0] == 24:
            linje += '2'
        else:
            linje += '0'

        x += 150

    splitta = linje.split()

    def splitter(splitz):
        return list(splitz)

    for i in range(len(splitta)):
        brett[i] = splitter(splitta[i])

def printBrett():
    print()
    for i in range(6):
        print(i+1, ": ", brett[i], "\n")
    print()

def kalkuler(brettet):

    def tre_en_rad(brettet): #tre av samme farge i en rad

        blaa = []
        gul = []
        tom = []

        for i in range(6): #rad
            for j in range(6): #kolonne
                if brettet[i][j] == '1':
                    blaa.append(j)
                elif brettet[i][j] == '2':
                    gul.append(j)
                else:
                    tom.append(j)

            if len(blaa) == 3 and len(tom) != 0:
                for j in range(6):
                    if brettet[i][j] == '0':
                        brettet[i][j]= '2'

            if len(gul) == 3 and len(tom) != 0:
                for j in range(6):
                    if brettet[i][j] == '0':
                        brettet[i][j] = '1'

            blaa.clear()
            gul.clear()
            tom.clear()

    def tre_en_kol(brettet): #tre av samme farge i en kolonne

            blaa = []
            gul = []
            tom = []

            for i in range(6): #rad
                for j in range(6): #kolonne
                    if brettet[j][i] == '1':
                        blaa.append(j)
                    elif brettet[j][i] == '2':
                        gul.append(j)
                    else:
                        tom.append(j)

                if len(blaa) == 3 and len(tom) != 0:
                    for j in range(6):
                        if brettet[j][i] == '0':
                            brettet[j][i]= '2'

                if len(gul) == 3 and len(tom) != 0:
                    for j in range(6):
                        if brettet[j][i] == '0':
                            brettet[j][i] = '1'

                blaa.clear()
                gul.clear()
                tom.clear()

    def to_sammen_rad(brettet):#to vedsiden av hverandre i rad

        for i in range(6): #6 sjekker alle rader 0 - 5
            for j in range(5): #5 fordi: sjekker ikke siste plass mot en plass utenfor brettet

                if brettet[i][j] == '1' and brettet[i][j] == brettet[i][j+1]: #hvis blå og neste er blå
                    if j == 0:
                        brettet[i][j+2] = '2'
                    elif j == 4:
                        brettet[i][j-1] = '2'
                    else:
                        brettet[i][j+2] = '2'
                        brettet[i][j-1] = '2'

                if brettet[i][j] == '2' and brettet[i][j] == brettet[i][j+1]: #hvis blå og neste er blå
                    if j == 0:
                        brettet[i][j+2] = '1'
                    elif j == 4:
                        brettet[i][j-1] = '1'
                    else:
                        brettet[i][j+2] = '1'
                        brettet[i][j-1] = '1'

    def to_sammen_kol(brettet):#to vedsiden av hverandre i kolonne

        for i in range(6): #6 sjekker alle rader 0 - 5
            for j in range(5): #5 fordi: sjekker ikke siste plass mot en plass utenfor brettet

                if brettet[j][i] == '1' and brettet[j][i] == brettet[j+1][i]: #hvis blå og neste er blå
                    if j == 0:
                        brettet[j+2][i] = '2'
                    elif j == 4:
                        brettet[j-1][i] = '2'
                    else:
                        brettet[j+2][i] = '2'
                        brettet[j-1][i] = '2'

                if brettet[j][i] == '2' and brettet[j][i] == brettet[j+1][i]: #hvis gul og neste er gul
                    if j == 0:
                        brettet[j+2][i] = '1'
                    elif j == 4:
                        brettet[j-1][i] = '1'
                    else:
                        brettet[j+2][i] = '1'
                        brettet[j-1][i] = '1'

    def to_split_rad(brettet):#to like med space mellom seg - rad

        for i in range(6):
            for j in range(4): #sjekker 4 splits (dette dekker en hel rad)

                if brettet[i][j] == '1' and brettet[i][j] == brettet[i][j+2]:
                    brettet[i][j+1] = '2'

                if brettet[i][j] == '2' and brettet[i][j] == brettet[i][j+2]:
                    brettet[i][j+1] = '1'

    def to_split_kol(brettet):#to like med space mellom seg - kol

        for i in range(6):
            for j in range(4): #sjekker 4 splits (dette dekker en hel rad)

                if brettet[j][i] == '1' and brettet[j][i] == brettet[j+2][i]:
                    brettet[j+1][i] = '2'

                if brettet[j][i] == '2' and brettet[j][i] == brettet[j+2][i]:
                    brettet[j+1][i] = '1'

    def sammenlign_rad(brettet): #sammenligner fullRad med rader med fire

        fullRad = []
        fireRad = []
        funnet = False
        for i in range(6): #finner fulle rader og rader med 4.
            radZero = 0
            for j in range(6):
                if brettet[i][j] == '0':
                    radZero += 1

            if radZero == 0:
                fullRad.append(i)
            elif radZero == 2:
                fireRad.append(i)

        if fullRad != [] and fireRad != []: #finnes både full rad og 4rad. finn match.

            for x in fullRad: #posisjon til fullRad
                if funnet == False:
                    for y in fireRad: #posisjon til fireRad

                        count = 0
                        for i in range(6): #kjør gjennom elementer i raden
                            if brettet[x][i] == brettet[y][i]:
                                count += 1

                        if count == 4: #hvis to rader matcher
                            funnet = True
                            for i in range(6): #fyll empty slots på 4-raden
                                if brettet[y][i] == '0': #sjekker for empty slot

                                    if brettet[x][i] == '1': #sjekker korresponderende element i fullRad
                                        brettet[y][i] = '2' #angir motsatt av fullRad verdi til empty slot.

                                    if brettet[x][i] == '2':
                                        brettet[y][i] = '1'
                            break

    def sammenlign_kol(brettet): #sammenligner fullKol med kol med fire

        fullKol = []
        fireKol = []
        funnet = False
        for i in range(6): #finner fulle kolonner og kolonner med 4.
            kolZero = 0
            for j in range(6):
                if brettet[j][i] == '0':
                    kolZero += 1

            if kolZero == 0:
                fullKol.append(i)
            elif kolZero == 2:
                fireKol.append(i)

        if fullKol != [] and fireKol != []: #finnes både full kolonne og 4kol. Finn match.

            for x in fullKol: #posisjon til fullKol
                if funnet == False:
                    for y in fireKol: #posisjon til fireKol

                        count = 0
                        for i in range(6): #kjør gjennom elementer i kolonnen
                            if brettet[i][x] == brettet[i][y]:
                                count += 1

                        if count == 4: #hvis to kolonner matcher
                            funnet = True
                            for i in range(6): #fyll empty slots på 4-kolonnen
                                if brettet[i][y] == '0': #sjekker for empty slot

                                    if brettet[i][x] == '1': #sjekker korresponderende element i fullRad
                                        brettet[i][y] = '2' #angir motsatt verdi av fullKol til empty slot

                                    if brettet[i][x] == '2':
                                        brettet[i][y] = '1'

                            break


    test = 0 # 0 ikke ferdig, 1 ferdig
    count = 0
    while test == 0 and count < 10:

        count += 1
        print("Count: ", count)
        tre_en_rad(brettet)
        tre_en_kol(brettet)
        to_sammen_rad(brettet)
        to_sammen_kol(brettet)
        to_split_rad(brettet)
        to_split_kol(brettet)
        sammenlign_rad(brettet)
        sammenlign_kol(brettet)

        test = 1 #setter lik Ferdig
        for i in range(6):
            for j in range(6):
                if brettet[i][j] == '0':
                    test = 0 #Dersom 0 finnes, setter lik 0, ikke ferdig
                    break



#BLAA = 1
#GUL = 2

def hovedprogram():

    svar = 0 #eks: 010102 000100 200002 010100 000002 000000
    while svar != "exit":

        svar = input("linje: ")
        if svar == "go":
            taScreen()
            lesBildet()
            kalkuler(brett)
            printBrett()
            klikkBrett(brett)



hovedprogram()
