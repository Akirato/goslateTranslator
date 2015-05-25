"""
Program to translate sentences and files using
Goslate module of Python
"""
try:
    import sys
except:
    raise RuntimeError("Sys module for python not present.\n")
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
    return gs.translate(sentence,langid)    

print getAllLanguages()
print translate("Hello world",'hi')
print translate("Hello world",'Hindi')
print translate("Hello world",'Chinese')
print translate("Hello world",'sdifkjsdf')
