import shutil, os
SLASH = "\\"
SPACE  = " "
TYPE = "mkv"
DOT = "."
def main():
    fromDir = ""
    toDir = ""
    dotNum = 0
    stop = "" 
    
    fromDir = validateDir(input("Current Folder: "))
    
    
    toDir = validateDir(input("Destination: "))
    dotNum = int(input("Enter number of words to be included: "))
    print(str(copy(fromDir, "", dotNum, True)))
    
    #raw_input("Continue Y/n?: ") #Caused error due to input needing quotations
    
    copy(fromDir, toDir, dotNum, False)
    
def validateDir(inputDir):
    return inputDir.replace('"', '')
    
    
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
                print("Converted: %s" % i)
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


main()

