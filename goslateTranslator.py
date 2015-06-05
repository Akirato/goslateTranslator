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

def translate(sentence,sourcelangId,langid):
    if sourcelangId == None:
        sourcelangId = detectLanguage(sentence)
    languages = gs.get_languages()
    for i in languages.items():
        if i[0] == langid:
            break
        if i[1].lower() == langid.lower():
            langid = i[0]
            break 
    for i in languages.items():
        if i[0] == sourcelangId:
            break
        if i[1].lower() == sourcelangId.lower():
            sourcelangId = i[0]
            break
    if not(langid in languages.keys()):
        langid == 'en'
    if not(sourcelangId in languages.keys()):
        sourcelangId == 'en'
    try:
        return gs.translate(sentence,langid)  
    except:
        print("Error in Connection or Permission.")

def translateSRT(filePath,sourcelangId,langid):
    fileContent = open(filePath,"r").read()
    fileLines = fileContent.splitlines()
    outputFile=open(filePath[:-4]+"_"+langid+'.srt',"w")
    length,h = len(fileLines),1
    for i in fileLines:
        print("Translating: "+str(h)+"/"+str(length)+" lines.")
	h=h+1
        if not(i.startswith("<") or (len(i)>0 and i[0].isdigit())):
            print((translate(i,sourcelangId,langid).encode('utf-8')),file=outputFile)
        else:
            print(i,file=outputFile)
    return 1

if __name__ == "__main__":
    if (len(sys.argv)) == 1:
        print("Give the srt file for translation.")
    elif (len(sys.argv)) == 2:
        if sys.argv[1] == "all":
            print(getAllLanguages())
        else:
            print("Give the lang id for translation.")
    elif len(sys.argv) == 3:
        if sys.argv[1] == "getIdOfForLang":
            print(languageOfId(sys.argv[1]))
        else:
            translateSRT(sys.argv[1],None,sys.argv[2])
    elif len(sys.argv) > 3:
        translateSRT(sys.argv[1],sys.argv[2],sys.argv[3])
    exit()
