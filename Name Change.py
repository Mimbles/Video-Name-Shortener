import shutil, os
SLASH = "\\"
SPACE  = " "
TYPE = "mkv"
DOT = "."
def main():
    fromDir = ""
    toDir = ""
    dotNum = 0
    option = options()
    print(option)
    fromDir = input("Current Folder: ")
    if option != 3:
        toDir = input("Destination: ")
    dotNum = int(input("Enter number of words to be included: "))
    print(str(copy(fromDir, "", dotNum, True)))
    
    discontinue = input("Continue Y/n?: ")
    

    if discontinue == "n":
        main()
    elif option == "1":
        copy(fromDir, toDir, dotNum)
    elif option == "2":
        copy(fromDir, toDir, dotNum)
    elif option == "3":
        copy(fromDir, fromDir, dotNum)
    else:
        print("Error")
        
def copy(fromDir, toDir, dotNum, scan):
    itemNumber = 0
    for i in os.listdir(fromDir):
        fileDirectory = fromDir + SLASH + i
        lst = i.split(".")
        if os.path.isdir(fileDirectory):
            if scan == False:
                #print("Found Folder")
                copy(fileDirectory, toDir, dotNum, False)
            else:
                itemNumber = itemNumber + copy(fileDirectory, "", dotNum,  True)
        if lst[len(lst) - 1] == "mkv" and not os.path.isdir(fileDirectory):
            if scan == False:
                fileDirectory = fromDir + SLASH + i
                shutil.move(fileDirectory,  toDir + SLASH + rename(i, dotNum) + DOT + TYPE)
                print("coppied %s" % i)
            else:
                print(i)
                itemNumber = itemNumber + 1
                return itemNumber
    if scan == True:
         return itemNumber
def rename(name, dotNum):
    splitName = name.split(".")
                           
    newName = ""
    for i in range(0, dotNum):
        newName = newName + splitName[i] + SPACE
    return newName    

def options():
    print("1.Copy + Rename")
    print("2.Copy")
    print("3.Rename")
    return input("Enter Option: ")

main()

