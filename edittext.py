import os

filename = "downloadtxt/175000.txt"

f = open(filename, 'r', encoding='UTF-8')

txt = f.readlines()

f.close()

#print(txt)

edit_txt = [e.replace('\xa0','').replace('\u3000','')for e in txt]

reedit_txt = []

for i in edit_txt:
    #レスポンシブデザインの切り替わりで中断する
    if(i == '\t\t\t\t\n'):
        break
    #改行コードじゃなかったらどんどん入れていくよ
    if(i != '\n'):
        reedit_txt.append(i)
    

#print(edit_txt)
print(reedit_txt)

fw = open("maketxt.txt",'w', encoding="UTF-8")

for i in reedit_txt:
    print(i)
    fw.write(i)

fw.close()