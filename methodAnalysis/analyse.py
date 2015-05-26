import goslate
import sys
def phrase_wise(filePath):
    print 0
    a=open(filePath,"r").read()
    lines = a.splitlines()
    need = []
    for i in lines:
        print 1
        if len(i)>0:
            if not i[0].isdigit():
                need.append(i)
    print 2
    return need

def word_wise(filePath):
    a=open(filePath,"r").read()
    lines = a.splitlines()
    need = []
    for i in lines:
        if not i[0].isdigit():
            for j in i.split():
            	need.append(i+" ")
    return need

def fullSentence_wise(filePath):
    a=open(filePath,"r").read()
    lines = a.splitlines()
    need = ""
    for i in lines:
        need = need + i + " "
    return [need]

def translate(need,langid):
    print 3
    translated=[]
    for i in need:
        translated.append(goslate.Goslate().translate(i,langid))
    return translated

for i in translate(phrase_wise(sys.argv[0]),'hi'):
    print i
exit()

