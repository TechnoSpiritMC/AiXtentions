import os


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

TestEN = os.path.exists("file.txt")
if TestEN:
    with open('file.txt', 'r') as file:
        testExtContent = file.read()
    a = a + 1
    a1 = a1 + f"{c(100, 100, 100, 'Extention de test            : ')}{g('OUI')}\n"
else:
    a1 = a1 + f"{c(100, 100, 100, 'Extention de test            : ')}{r('NON')}\n"

TestEN = os.path.exists("AiScores.py")
if TestEN:
    a = a + 1
    a1 = a1 + f"{c(100, 100, 100, 'Extention AiScores           : ')}{g('OUI')}\n"
else:
    a1 = a1 + f"{c(100, 100, 100, 'Extention AiScores           : ')}{r('NON')}\n"

TestEN = os.path.exists("AiTrainer.py")
if TestEN:
    a = a + 1
    a1 = a1 + f"{c(100, 100, 100, 'Extention AiTrainer          : ')}{g('OUI')}\n"
else:
    a1 = a1 + f"{c(100, 100, 100, 'Extention AiTrainer          : ')}{r('NON')}\n"

TestEN = os.path.exists("AiGraphs.console.py")
if TestEN:
    a = a + 1
    a1 = a1 + f"{c(100, 100, 100, 'Extention AiGraphs.console   : ')}{g('OUI')}\n"
else:
    a1 = a1 + f"{c(100, 100, 100, 'Extention AiGraphs.console   : ')}{r('NON')}\n"

TestEN = os.path.exists("AiGraphs.turtle.aiext")
if TestEN:
    a = a + 1
    a1 = a1 + f"{c(100, 100, 100, 'Extention AiGraphs.turtle    : ')}{g('OUI')}\n"
else:
    a1 = a1 + f"{c(100, 100, 100, 'Extention AiGraphs.turtle    : ')}{r('NON')}\n"

a1 = a1 + f"{c(100, 100, 100, f'Que voulez vous faire avec ces {a} extentions? Les')}{g('CHARGER (cha)')}{c(100, 100, 100, 'les')}{b('INSTALLER (ins)')}{c(100, 100, 100, 'ou les')}{r('IGNORER (ign)')}"
a1 = a1 + "\n"




chaINSign = input(a1)

if chaINSign == "cha":
    print(f'{c(100, 100, 100, f"Action en cours:")}{g(f"chargement des {a} extentions disponnibles")}')
    with open("test.py", "w") as testWrite:
        testWrite.write(testExtContent)




