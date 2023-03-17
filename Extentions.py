import os, time

testExtContent = ""
AiScoresExtContent = ""
AiTrainerExtContent = ""
AiGraphsCExtContent = ""
AiGraphsTExtContent = ""


def c(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def r(text):
    r = 255
    g = b = 50
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def g(text):
    g = 255
    r = b = 50
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def b(text):
    b = 255
    r = g = 100
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


a1 = f"{c(100, 100, 100, 'EXTENTIONS INSTALLÉES:')}"
a1 = a1 + "\n"
a = 0

TestEN = os.path.exists("test.aiext")
if TestEN:
    with open('test.aiext', 'r') as file:
        testExtContent = file.read()
    a = a + 1
    a1 = a1 + f"{c(100, 100, 100, 'Extention de test            : ')}{g('OUI')}\n"
else:
    a1 = a1 + f"{c(100, 100, 100, 'Extention de test            : ')}{r('NON')}\n"

TestEN = os.path.exists("AiScores.aiext")
if TestEN:
    with open('AiScores.aiext', 'r') as file:
        AiScoresExtContent = file.read()
    a = a + 1
    a1 = a1 + f"{c(100, 100, 100, 'Extention AiScores           : ')}{g('OUI')}\n"
else:
    a1 = a1 + f"{c(100, 100, 100, 'Extention AiScores           : ')}{r('NON')}\n"

TestEN = os.path.exists("AiTrainer.aiext")
if TestEN:
    with open('AiTrainer.aiext', 'r') as file:
        AiTrainerExtContent = file.read()
    a = a + 1
    a1 = a1 + f"{c(100, 100, 100, 'Extention AiTrainer          : ')}{g('OUI')}\n"
else:
    a1 = a1 + f"{c(100, 100, 100, 'Extention AiTrainer          : ')}{r('NON')}\n"

TestEN = os.path.exists("AiGraphs.console.aiext")
if TestEN:
    with open('AiGraphs.console.aiext', 'r') as file:
        AiGraphsCExtContent = file.read()
    a = a + 1
    a1 = a1 + f"{c(100, 100, 100, 'Extention AiGraphs.console   : ')}{g('OUI')}\n"
else:
    a1 = a1 + f"{c(100, 100, 100, 'Extention AiGraphs.console   : ')}{r('NON')}\n"

TestEN = os.path.exists("AiGraphs.turtle.aiext")
if TestEN:
    with open('AiGraphs.turtle.aiext', 'r') as file:
        AiGraphsTExtContent = file.read()
    a = a + 1
    a1 = a1 + f"{c(100, 100, 100, 'Extention AiGraphs.turtle    : ')}{g('OUI')}\n"
else:
    a1 = a1 + f"{c(100, 100, 100, 'Extention AiGraphs.turtle    : ')}{r('NON')}\n"

a1 = a1 + f"{c(100, 100, 100, f'Que voulez vous faire avec ces {a} extention(s)? Les')}{g('CHARGER (cha)')}{c(100, 100, 100, 'les')}{b('INSTALLER (ins)')}{c(100, 100, 100, 'ou les')}{r('IGNORER (ign)')}"
a1 = a1 + "\n"

chaINSign = input(a1)

if chaINSign == "cha":

    if a == 0:
        print(c(100, 100, 100, f"Tentative d'installation de {a} extentions disponnibles..."))
        time.sleep(1)
        print(f"{c(100, 100, 100, 'Tentative de chargement')}{r('infructueuse : aucune extention n est installée.')}")
    else:
        print(f'{c(100, 100, 100, f"Action en cours:")}{g(f"tentative de chargement des {a} extentions disponnibles")}')
        i = 0
        TimeBefore = time.time()
        TestEN = os.path.exists("test.aiext")
        if TestEN:
            with open("test.py", "w") as testWrite:
                testWrite.write(testExtContent)
                testC = 1


        TestEN = os.path.exists("AiScores.aiext")
        if TestEN:
            with open("AiScores.py", "w") as testWrite:
                testWrite.write(AiScoresExtContent)
                AiScoresC = 1


        TestEN = os.path.exists("AiTrainer.aiext")
        if TestEN:
            with open("AiTrainer.py", "w") as testWrite:
                testWrite.write(AiTrainerExtContent)
                AiTrainerC = 1


        TestEN = os.path.exists("AiGraphs.console.aiext")
        if TestEN:
            with open("AiGraphs.console.py", "w") as testWrite:
                testWrite.write(AiGraphsCExtContent)
                AiGraphsCC = 1


        TestEN = os.path.exists("AiGraphs.turtle.aiext")
        if TestEN:
            with open("AiGraphs.turtle.py", "w") as testWrite:
                testWrite.write(AiGraphsTExtContent)
                AiGraphsTC = 1

        TimeAfter = time.time()




        print(f"{c(100, 100, 100, f'Opération effectuée en {round((TimeAfter-TimeBefore))} secondes avec')}{g('succès.')}")
