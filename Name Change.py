import shutil, os
SLASH = "\\"
SPACE  = " "
TYPE = "mkv"
DOT = "."
def main():
    option = options()
    if option == "1":
        copyTo = input("Where do you want to copy to: ")
        copy(directory(), copyTo)
        rename(copyTo)
    elif option == "2":
        copyTo = input("Where do you want to copy to: ")
        copy(directory(), copyTo)
    else:
        rename(directory())

def copy(fromDir, toDir):
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
            shutil.move(fileDirectory,  toDir + SLASH + i)
            print("coppied %s" % i)
    
def rename(targetDir):
    dotNum = int(input("Enter Number of '.'"))
    for i in os.listdir(targetDir):
        fileDirectory = targetDir + SLASH + i
        shutil.move(fileDirectory, targetDir + SLASH + name(i, dotNum) + DOT + TYPE)
        print(i)
        
def directory():
    return input("Enter directory: ")

def name(file, dotNum):
    returnString = ""
    fileSplit = file.split(".")
    print(fileSplit)
    for i in range (0,dotNum):
        returnString = returnString + fileSplit[i] + SPACE    
    return returnString

def options():
    print("1.Copy + Rename")
    print("2.Copy")
    print("3.Rename")
    return input("Enter Option: ")



main()

