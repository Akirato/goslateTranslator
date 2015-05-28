"""
Program to translate sentences and files using
Goslate module of Python
"""
from __future__ import print_function
try:
    import sys
except:
    raise RuntimeError("Sys module or __future__ for python not present.\n")
try:
    import goslate
except:
    raise RuntimeError("Goslate module for python not present.\n Install using 'pip install goslate'")

gs = goslate.Goslate()

def getAllLanguages():
    return gs.get_languages()
    
def detectLanguage(sentence):
    return gs.detect(sentence)
    
def languageOfId(langid):
    return languages[langid]

def translate(sentence,langid):
    languages = gs.get_languages()
    for i in languages.items():
        if i[0] == langid:
            break
        if i[1] == langid:
            langid = i[0]
            break 
    if not(langid in languages.keys()):
        raise Exception("Language Id '"+str(langid)+"' does not exist.\n Please check the language list again.")
    try:
        return gs.translate(sentence,langid)  
    except:
        print("caught")

def translateSRT(filePath,langid):
    fileContent = open(filePath,"r").read()
    fileLines = fileContent.splitlines()
    outputFile=open(filePath[:-4]+"_"+langid+'.srt',"w")
    for i in fileLines:
        if not(i.startswith("<") or (len(i)>0 and i[0].isdigit())):
            print((translate(i,langid).encode('utf-8')),file=outputFile)
        else:
            print(i,file=outputFile)
    return 1

if __name__ == "__main__":
    if (len(sys.argv)) == 1:
        print("Give the srt file for translation.")
    elif (len(sys.argv)) == 2:
        print("Give the lang id for translation.")
    else:
        translateSRT(sys.argv[1],sys.argv[2])
    exit()
