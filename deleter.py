# Description: This file contains functions that are used to delete files from the current directory.
# TO delete current graph images, del_current_img function is used.
# TO delete all old graph images, stock_cleaner function is used.
import os

def is_a_graph_img(fileFullName):  # fileFullName is a list that contains file name and extension

    try:
        fileName = fileFullName[0]
        fileExt = fileFullName[1]
        
        int(fileName)  # to check if file name consists of only numbers

        if fileExt == "jpeg":
            return True
        else:
            return False
        
    except ValueError:
        print("not a graph img Value Error")
        return False

    except IndexError:
        print("a folder or no extension Index Error")
        return False

def stock_cleaner():
    files = os.listdir()

    for rawFileName in files:
        
        filteredFileName = rawFileName.split(".")  # file name and extension

        if is_a_graph_img(filteredFileName):  # check if the file is a graph image
            
            os.remove(rawFileName)
            print(f"{rawFileName} is deleted")


def del_current_img(fileName):
    try:
        os.remove(fileName)
        
    except OSError as e:
        print(f"Error: {fileName} - {e.strerror}")
        

# stock_cleaner()  # delete all old graph images