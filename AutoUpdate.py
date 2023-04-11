import requests, difflib, os

if not os.path.exists("CurrentVersion.txt"):
  print("Merci de réinstaller ce programme. Une erreur fatale s'est produite.")
  exit(666)

class Links:
  LastVersionFloat = 'https://raw.githubusercontent.com/TechnoSpiritMC/AiXtentions/main/Lastest%20version.AiStat'
  SnapVersion = 'https://raw.githubusercontent.com/TechnoSpiritMC/AiXtentions/main/ExtentionsArrws.py'
  OffVersion = 'https://raw.githubusercontent.com/TechnoSpiritMC/AiXtentions/main/ExtentionsLtrs.py'

class Commands:
  GetActualVersion = 'AiScores -i version'         #GAV
  GetLastestVersion = 'AiScores -iL version'       #GLV
  UpdateOfficial = 'AiScores -u Official'          #UO
  UpdateSnapshot = 'AiScores -u Snapshot'          #US
  Info = 'info'                                    #I

class Answers:
  AnswerGAV = "La version de votre programme"

command = input("InAuthUser - AiXtentions 1.1 - ")

if command == Commands.GetActualVersion:
  with open("CurrentVersion.txt", "r") as file:
    CVersion = file.read()
  print(Answers.AnswerGAV + CVersion)

if command == Commands.GetLastestVersion:
  LV = requests.get(Links.LastVersionFloat, allow_redirects = True)
  print(Answers.AnswerGAV + str(LV.content).replace("\n", "").replace("b", ""))
