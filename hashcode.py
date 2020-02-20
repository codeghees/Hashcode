import glob
import operator

Textfiles = glob.glob("*.txt")

def sort(List):
    return List.sort( reverse = True)

def filehandler(file):
    Info = {}
    lines = file.split("\n")
    FirstLine = list(map(int, lines[0].split(" ")))
    
    Info["nBooks"] = FirstLine[0]
    Info["nLib"] = FirstLine[1]
    Info["Days"] = FirstLine[2]

    SecondLine = list(map(int, lines[1].split(" ")))
    Info["Scores"] = [(k,SecondLine[k]) for k in range(len(SecondLine))]

    LinesLeft = lines[2:]
    LinesLeft = [list(map(int,Line.split(" "))) for Line in LinesLeft if Line != ""]
    for i in range(Info["nLib"]):
        Item1 = LinesLeft[2*i]
        Item2 = LinesLeft[2*i+1]
        TempLibDict = {}
        TempLibDict["nBooks_lib"] = Item1[0]
        TempLibDict["signup"] = Item1[1]
        TempLibDict["capacity"] = Item1[2]
        TempLibDict["BookList"] = [k for k,v in sorted([(Item2[i], Info["Scores"][Item2[i]][1]) for i in range(len(Item2))], key = operator.itemgetter(1), reverse=True)]
        Info["Lib"+str(i)] = TempLibDict

    print(Info)
    return Info




for file in Textfiles:
    print (file)
    f = open(file, "r")
    filehandler(f.read())
    f.close()
    break
