import os
import glob

filelist = glob.glob("./downloadtxt/*.txt")

print(filelist)

file_path = os.path.abspath('./edittxt')
if os.path.exists(file_path) != True:
    os.mkdir(file_path)

for filename in filelist:
    print(filename)
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

    path, file = os.path.split(filename)
    fw = open("./edittxt/"+file,'w', encoding="UTF-8")

    for i in reedit_txt:
        fw.write(i)

    fw.close()