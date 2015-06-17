from __future__ import print_function
import goslate
gs = goslate.Goslate()
f1=open("Game.of.Thrones.S05E07.720p.HDTV.x264-0SEC.srt",'r')
f2=open('sentence_output.txt','w')
a = f1.read()
b = a.splitlines()
sentence,count = '',0
     
for i in b:
    if ((i.startswith('<') or ((len(i)>0 and i[0].isdigit()) or ((len(i)>3) and i[3].isdigit()))) and sentence=='') or len(i)==0:
        print(i,file=f2)
    else:
        if not(i.startswith('<') or (len(i)>0 and i[0].isdigit())) and not('.' in i):
            sentence = sentence+' '+i;
	elif ('.' in i):
	    sentence = sentence+' '+i;
	    print(gs.translate(sentence,'es').encode('utf-8')+'\n',file=f2)
	    sentence=''

exit()
	
