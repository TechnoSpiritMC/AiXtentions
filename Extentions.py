import os, time, requests

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

a1 = a1 + f"{c(100, 100, 100, f'Que voulez vous faire avec ces {a} extention(s)? Les')}{g('CHARGER (c)')}{c(100, 100, 100, 'les')}{b('INSTALLER (i)')}{c(100, 100, 100, 'ou')}{r('UTILISER CELLES DEJA INSTALLÉES (u)')}"
a1 = a1 + "\n"

chaINSign = input(a1)

if chaINSign == "c":

    if a == 0:
        print(c(100, 100, 100, f"Tentative d'installation de {a} extentions disponnibles..."))
        time.sleep(1)
        print(f"{c(100, 100, 100, 'Tentative de chargement')}{r('infructueuse : aucune extention n est installée.')}")
    else:
        print(f'{c(100, 100, 100, f"Action en cours:")}{g(f"tentative de chargement des {a} extentions disponnibles")}')
        i = 0
        TimeBefore = time.time()
        TestEN = os.path.exists("Test.aiext")
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




        print(f"{c(100, 100, 100, f'Opération effectuée en {truncate((TimeAfter-TimeBefore), 2)} secondes avec')}{g('succès.')}")
        
        
        
        
if chaINSign == "i":
  f = 0
  TestEN = os.path.exists("Test.py")
  if TestEN:
    f = f + 1  
    print("Test")


  TestEN = os.path.exists("AiScores.py")
  if TestEN:
    f = f + 1
    print("AiS")


  TestEN = os.path.exists("AiTrainer.py")
  if TestEN:
    f = f + 1
    print("Ait")


  TestEN = os.path.exists("AiGraphs.console.py")
  if TestEN:
    f = f + 1
    print("AiGC")


  TestEN = os.path.exists("AiGraphs.turtle.py")
  if TestEN:
    f = f + 1
  print(f)

  if f == 5:
        print(c(100, 100, 100, f"Tentative d'installation de {a} extentions disponnibles..."))
        time.sleep(1)
        print(f"{c(100, 100, 100, 'Tentative de téléchargement')}{r('annulée : toutes les extentions sont déjà présentes..')}")
  
  else:
        print(f'{c(100, 100, 100, f"Action en cours:")}{g(f"tentative de téléchargement des {(5 - f)} extentions absentes")}')
        i = 0
        TimeBefore = time.time()
        TestEN = os.path.exists("Test.py")
        if not TestEN:
            r = requests.get(Liens.Test, allow_redirects=True)
            open('Test.aiext', 'wb').write(r.content)


        TestEN = os.path.exists("AiScores.py")
        if not TestEN:
            r = requests.get(Liens.AiScores, allow_redirects=True)
            open('AiScores.aiext', 'wb').write(r.content)


        TestEN = os.path.exists("AiTrainer.py")
        if not TestEN:
            r = requests.get(Liens.AiTrainer, allow_redirects=True)
            open('AiTrainer.aiext', 'wb').write(r.content)


        TestEN = os.path.exists("AiGraphs.console.aiext")
        if not TestEN:
            r = requests.get(Liens.AiGraphsConsole, allow_redirects=True)
            open('AiGraphs.console.aiext', 'wb').write(r.content)


        TestEN = os.path.exists("AiGraphs.turtle.py")
        if not TestEN:
            r = requests.get(Liens.AiGraphsTurtle, allow_redirects=True)
            open('AiGraphs.turtle.aiext', 'wb').write(r.content)

        TimeAfter = time.time()




        print(f"{c(100, 100, 100, f'Opération effectuée en {truncate((TimeAfter-TimeBefore), 2)} secondes avec')}{g('succès.')}")
