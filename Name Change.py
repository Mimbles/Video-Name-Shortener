import shutil, os
SLASH = "\\"
SPACE  = " "
TYPE = "mkv"
DOT = "."
def main():
    targetDir = directory()
    
    for i in os.listdir(targetDir):
        fileDirectory = targetDir + SLASH + i
        shutil.move(fileDirectory, targetDir + SLASH + name(i) + DOT + TYPE)
        print(i)
def directory():
    return input("Enter directory: ")
def name(file):
    returnString = ""
    dotNum = int(input("Enter Number of '.'"))
    fileSplit = file.split(".")
    print(fileSplit)
    for i in range (0,dotNum):
        returnString = returnString + fileSplit[i] + SPACE    
    return returnString





main()

