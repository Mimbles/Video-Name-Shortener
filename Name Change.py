import shutil, os
import sys
SLASH = "\\"
SPACE  = " "
TYPE = "mkv"
DOT = "."
def main():
    print(sys.version)
    fromDir = ""
    toDir = ""
    dotNum = 0
    stop = "" 
    fromDir = validateDir(input("Current Folder: "))
    toDir = validateDir(input("Destination: "))
    print("found: %s Files" % str(copy(fromDir, "", dotNum, True)))
    dotNum = int(input("Enter number of words to be included: "))
    
    cancel = input("Continue Y/n?: ")
    if cancel == "Y" or cancel == "y":
        copy(fromDir, toDir, dotNum, Faslse)
    else:
        main()
    
def validateDir(inputDir):
    return inputDir.replace('"', '')
    
def copy(fromDir, toDir, dotNum, scan):
    itemNumber = 0
    dirList = os.listdir(fromDir)
    for i in os.listdir(fromDir):
        fileDirectory = fromDir + SLASH + i
        lst = i.split(DOT)
        if os.path.isdir(fileDirectory):
            print("Folder found")
            if scan == False:
                copy(fileDirectory, toDir, dotNum, False)
            elif scan == True:
                print("test")
                itemNumber = itemNumber + copy(fileDirectory, "", dotNum,  True)
        elif lst[-1] == TYPE:
            if scan == False:
                fileDirectory = fromDir + SLASH + i
                print(fileDirectory)
                shutil.move(fileDirectory,  toDir + SLASH + rename(i, dotNum) + DOT + TYPE)
                print("Converted: %s" % i)
            else:
                print(i)
                itemNumber = itemNumber + 1
    if scan == True:
         return itemNumber
        
def rename(name, dotNum):
    splitName = name.split(DOT)                        
    newName = ""
    for i in range(0, dotNum):
        newName = newName + splitName[i] + SPACE
    newName[-1] = ""
    return newName
main()

