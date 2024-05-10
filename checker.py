import os
    
def isCSV(file):  # checks if the file is a csv file
    if os.path.isfile(file):
        
        ext = os.path.splitext(file)[1]
        
        if ext.lower() == ".csv":
            return True
        
        else:
            return False
    else:
        return False
    
def isPDF(file):  # checks if the file is a pdf file
    if os.path.isfile(file):
        
        ext = os.path.splitext(file)[1]
        
        if ext.lower() == ".pdf":
            return True
        
        else:
            return False
    else:
        return False
    
def isXLSX(file):  # checks if the file is a xlsx file
    if os.path.isfile(file):
        
        ext = os.path.splitext(file)[1]
        
        if ext.lower() == ".xlsx":
            return True
        
        else:
            return False
    else:
        return False