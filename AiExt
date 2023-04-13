import os, time, requests, sys, keyboard

Exit = 0
testExtContent = ""
AiScoresExtContent = ""
AiTrainerExtContent = ""
AiGraphsCExtContent = ""
AiGraphsTExtContent = ""


def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


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


class Liens:
    AiScores = 'https://gist.githubusercontent.com/TechnoSpiritMC/a54b406837625abac62afee4b108aa18/raw/050337a51be592df4ce70ad2c05f0920f778f260/AiScores.aiext'
    AiTrainer = 'https://gist.githubusercontent.com/TechnoSpiritMC/c908c04c284c6a875c04e9c776e4e987/raw/ec27d1dc9184722361bb70fd650bcf5d8cd4560b/AiTrainer_Test.aiext'
    Test = 'https://gist.githubusercontent.com/TechnoSpiritMC/c908c04c284c6a875c04e9c776e4e987/raw/ec27d1dc9184722361bb70fd650bcf5d8cd4560b/AiTrainer_Test.aiext'
    AiGraphsConsole = 'https://gist.githubusercontent.com/TechnoSpiritMC/ffcf88789709376b763ee69bf5855320/raw/3e3d2dd065257f4e2227a279c5ae73486af3ba47/AiGraphs.console.aiext'
    AiGraphsTurtle = 'https://gist.githubusercontent.com/TechnoSpiritMC/c477539269bbd27b9af09627bf861273/raw/8dc1bbd88f93f05cf22b146b4afc1d837caaddd9/AiGraphs.turtle.aiext'


a1 = f"{c(100, 100, 100, 'EXTENTIONS INSTALLÉES:')}"
a1 = a1 + "\n"
a = 0

TestEN = os.path.exists("Test.aiext")
if TestEN:
    with open('Test.aiext', 'r') as file:
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

print(a1)
sys.stdout.write("\rPour séléctionner, appuyez sur la touche [→] ou [←]. Puis, une fois votre choix effectué, faites [Entrée].")


Line = 2

one = f"{r('Charger')} | {c(200, 200, 255, 'Installer')} | {c(200, 255, 200, 'Utiliser les extentions actuelles')}"
two = f"{c(255, 200, 200, 'Charger')} | {b('Installer')} | {c(200, 255, 200, 'Utiliser les extentions actuelles')}"
three = f"{c(255, 200, 200, 'Charger')} | {c(200, 200, 255, 'Installer')} | {g('Utiliser les extentions actuelles')}"


def linePrint(LineInt=1, TmpDown=0, TmpUp=0):
    if LineInt == 1:
        sys.stdout.write(f"\r{one}")
    if LineInt == 2:
        sys.stdout.write(f"\r{two}")
    if LineInt == 3:
        sys.stdout.write(f"\r{three}")


time.sleep(3)







Down = 0
Up = 0

_Down = 0
_Up = 0
Line = 1
linePrint(1, _Down, _Up)
while Exit != 1:
    if keyboard.is_pressed("Left"):
        Up = 1
        _Up = 1

    if _Up != Up:
        if Line == 1:
            Line = 3
        else:
            Line = Line - 1
        linePrint(Line, _Down, _Up)
        _Up = 0

    if keyboard.is_pressed("Right"):
        Down = 1
        _Down = 1

    if _Down != Down:
        if Line == 3:
            Line = 1
        else:
            Line = Line + 1
        linePrint(Line, _Down, _Up)
        _Down = 0

    if not keyboard.is_pressed("z"):
        Up = 0

    if not keyboard.is_pressed("s"):
        Down = 0

    if keyboard.is_pressed("Return"):
        Exit = 1



if Line == 1:
    chaINSign = "c"

if Line == 2:
    chaINSign = "i"

if Line == 3:
    sys.stdout.write("\rVous avez choisi: Télécharger")

if chaINSign == "c":

    if a == 0:
        print(c(100, 100, 100, f"\rTentative d'installation de {a} extentions disponnibles..."))
        time.sleep(1)
        print(f"{c(100, 100, 100, 'Tentative de chargement')}{r('infructueuse : aucune extention n est installée.')}")
        exit(925)
    else:
        print(f'\r{c(100, 100, 100, f"Action en cours:")}{g(f"tentative de chargement des {a} extentions disponnibles")}')
        i = 0
        TimeBefore = time.time()
        TestEN = os.path.exists("Test.aiext")
        sys.stdout.write(c(255, 255, 255, "\r00% - ") + c(50, 50, 50, "__________"))
        if TestEN:

            with open("test.py", "w") as testWrite:
                testWrite.write(testExtContent)
                testC = 1
                sys.stdout.write(c(50, 50, 255, "\r20% - __") + c(50, 50, 50, "________"))

        TestEN = os.path.exists("AiScores.aiext")
        if TestEN:

            with open("AiScores.py", "w") as testWrite:
                testWrite.write(AiScoresExtContent)
                AiScoresC = 1
                sys.stdout.write(c(200, 75, 200, "\r40% - ____") + c(50, 50, 50, "______"))

        TestEN = os.path.exists("AiTrainer.aiext")
        if TestEN:

            with open("AiTrainer.py", "w") as testWrite:
                testWrite.write(AiTrainerExtContent)
                AiTrainerC = 1
                sys.stdout.write(c(200, 75, 75, "\r60% - ______") + c(50, 50, 50, "____"))

        TestEN = os.path.exists("AiGraphs.console.aiext")
        if TestEN:

            with open("AiGraphs.console.py", "w") as testWrite:
                testWrite.write(AiGraphsCExtContent)
                AiGraphsCC = 1
                sys.stdout.write(c(200, 175, 75, "\r80% - ________") + c(50, 50, 50, "__"))

        TestEN = os.path.exists("AiGraphs.turtle.aiext")
        if TestEN:

            with open("AiGraphs.turtle.py", "w") as testWrite:
                testWrite.write(AiGraphsTExtContent)
                AiGraphsTC = 1
                sys.stdout.write(c(75, 200, 75, "\r100% - __________") + c(50, 50, 50, ""))

        TimeAfter = time.time()

        print(
            f"{c(100, 100, 100, f'Opération effectuée en {truncate((TimeAfter - TimeBefore), 2)} secondes avec')}{g('succès.')}")

if chaINSign == "i":
    f = 0
    TestEN = os.path.exists("Test.aiext")
    if TestEN:
        f = f + 1

    TestEN = os.path.exists("AiScores.aiext")
    if TestEN:
        f = f + 1

    TestEN = os.path.exists("AiTrainer.aiext")
    if TestEN:
        f = f + 1

    TestEN = os.path.exists("AiGraphs.console.aiext")
    if TestEN:
        f = f + 1

    TestEN = os.path.exists("AiGraphs.turtle.aiext")
    if TestEN:
        f = f + 1

    if f == 5:
        print(c(100, 100, 100, f"\rTentative d'installation de {a} extentions disponnibles..."))
        time.sleep(1)
        print(
            f"\r{c(100, 100, 100, 'Tentative de téléchargement')}{r('annulée : toutes les extentions sont déjà présentes..')}")

    else:
        print(
            f'\r{c(100, 100, 100, f"Action en cours:")}{g(f"tentative de téléchargement des {(5 - f)} extentions absentes")}')
        i = 0
        TimeBefore = time.time()
        sys.stdout.write(c(255, 255, 255, "\r00% - ") + c(50, 50, 50, "__________"))
        TestEN = os.path.exists("Test.aiext")
        if not TestEN:
            r = requests.get(Liens.Test, allow_redirects=True)
            open('Test.aiext', 'wb').write(r.content)
            sys.stdout.write(c(50, 50, 255, "\r20% - __") + c(50, 50, 50, "________"))

        TestEN = os.path.exists("AiScores.aiext")
        if not TestEN:

            r = requests.get(Liens.AiScores, allow_redirects=True)
            open('AiScores.aiext', 'wb').write(r.content)
            sys.stdout.write(c(200, 75, 200, "\r40% - ____") + c(50, 50, 50, "______"))

        TestEN = os.path.exists("AiTrainer.aiext")
        if not TestEN:

            r = requests.get(Liens.AiTrainer, allow_redirects=True)
            open('AiTrainer.aiext', 'wb').write(r.content)
            sys.stdout.write(c(200, 75, 75, "\r60% - ______") + c(50, 50, 50, "____"))

        TestEN = os.path.exists("AiGraphs.console.aiext")
        if not TestEN:

            r = requests.get(Liens.AiGraphsConsole, allow_redirects=True)
            open('AiGraphs.console.aiext', 'wb').write(r.content)
            sys.stdout.write(c(200, 175, 75, "\r80% - ________") + c(50, 50, 50, "__"))

        TestEN = os.path.exists("AiGraphs.turtle.aiext")
        if not TestEN:

            r = requests.get(Liens.AiGraphsTurtle, allow_redirects=True)
            open('AiGraphs.turtle.aiext', 'wb').write(r.content)
            sys.stdout.write(c(75, 200, 75, "\r100% - __________") + c(50, 50, 50, ""))

        TimeAfter = time.time()

        print(
            f"{c(100, 100, 100, f'Opération effectuée en {truncate((TimeAfter - TimeBefore), 5)} secondes avec')}{g('succès.')}")
