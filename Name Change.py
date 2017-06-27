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
                      
    if option == "1":
        change(fromDir, toDir, dotNum)
    elif option == "2":
        change(fromDir, toDir, dotNum)
    elif option == "3":
        change(fromDir, fromDir, dotNum)
    else:
        print("Error")
def change(fromDir, toDir, dotNum):
    for i in os.listdir(fromDir):
        fileDirectory = fromDir + SLASH + i
        lst = i.split(".")
        print(lst)
        if os.path.isdir(fileDirectory):
            print("Found Folder")
            print(fileDirectory)
            copy(fileDirectory, toDir)
        
        if lst[len(lst) - 1] == "mkv" and not os.path.isdir(fileDirectory):
            fileDirectory = fromDir + SLASH + i
            shutil.move(fileDirectory,  toDir + SLASH + rename(i, dotNum) + DOT + TYPE)
            print("coppied %s" % i)
            
def rename(name, dotNum):
    splitName = name.split(".")
                           
    newName = ""
    for i in range(0, dotNum):
        newName = newName + splitName[i] + SPACE
    return newName    
def directory():
    return input("Enter directory: ")

def options():
    print("1.Copy + Rename")
    print("2.Copy")
    print("3.Rename")
    return input("Enter Option: ")



main()

