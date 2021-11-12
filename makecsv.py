import csv

filename = "txtfile/175000.pdf_output.txt"

f = open(filename, 'r', encoding='UTF-8')

txt = f.readlines()

f.close()

print(txt)

#表の中で／で改行されてしまっているものを１列にする
for (i, text) in enumerate(txt):
    if(txt[i][0] == "／"):
        txt[i-1] = f'{txt[i-1]}{[i]}'
        txt[i] = '\n'

#構造体としてデータを整理する
class syllabus:
    def __init__(self,classname,teacher,classcategory,coc,classtype,period,faculty,classregicode,grade,classnumcode,credit,officehours,rtadvice,objective,goals,schedule,studyoutside,keywords,notice,textbooks,evaluation,related,link,notes):
        self.classname = classname
        self.teacher = teacher
        self.classcategory = classcategory
        self.coc = coc
        self.classtype = classtype
        self.period = period
        self.faculty = faculty
        self.classregcode = classregicode
        self.grade = grade
        self.classnumcode = classnumcode
        self.credit = credit
        self.officehours = officehours
        self.rtadvice = rtadvice
        self.objective = objective
        self.goals = goals
        self.schedule = schedule
        self.studyoutside = studyoutside
        self.keywords = keywords
        self.notice = notice
        self.textbooks = textbooks
        self.evaluation = evaluation
        self.related = related
        self.link = link
        self.notes = notes



#txtファイルに書き込む　空白改行は削除 
fw = open("maketxt.txt",'w', encoding="UTF-8")

for i in txt:
    if(i != '\n'):
        print(i)
        fw.write(i)

fw.close()


#CSV書き込み
with open("syllabus.csv", 'w')as csv_f:
    feildnames = ['classname','teacher','classcategory','coc','classtype','period','faculty','classregicode','grade','classnumcode','credit','officehours','rtadvice','objective','goals','schedule','studyoutside','keywords','notice','textbooks','evaluation','related','link','notes']
    writer = csv.DictWriter(csv_f,fieldnames=feildnames)
    writer.writeheader()

    writer.writerow