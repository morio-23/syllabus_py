# coding: utf-8
import csv

#構造体としてデータを整理する
class syllabus:
    def __init__(self,classname='',teacher='',classcategory= '',coc='-',classtype= '',period= '',faculty= '',classregcode= '',grade= '',classnumcode='',credit= '',latestupdate='',officehours= '',rtadvice= '',objective= '',edugoals= '',goals= '',schedule= '',studyoutside= '',keywords= '',notice= '',textbooks= '',evaluation= '',related= '',link= '',notes= ''):
        self.classname = classname
        self.teacher = teacher
        self.classcategory = classcategory
        self.classtype = classtype
        self.coc = coc
        self.period = period
        self.faculty = faculty
        self.classregcode = classregcode
        self.grade = grade
        self.classnumcode = classnumcode
        self.credit = credit
        self.latestupdate = latestupdate
        self.officehours = officehours
        self.rtadvice = rtadvice
        self.objective = objective
        self.edugoals = edugoals
        self.goals = goals
        self.schedule = schedule
        self.studyoutside = studyoutside
        self.keywords = keywords
        self.notice = notice
        self.evaluation = evaluation
        self.textbooks = textbooks
        self.related = related
        self.link = link
        self.notes = notes


sy_title = ['富山大学 SYLLABUS\n','授業科目名\n','（英文名）\n','担当教員（所属）\n','授業科目区分\n','授業種別\n','COC+科目\n','開講学期\n','対象所属\n','対象学年\n','時間割コード\n','単位数\n','ナンバリングコード\n','最終更新日時\n','オフィスアワー（自由質問時間）\n','リアルタイム・アドバイス：更新日\n','授業のねらいとカリキュラム上の位置付け（一般学習目標）\n','教育目標\n','達成目標\n','授業計画（授業の形式、スケジュール等）\n','授業時間外学修\n','キーワード\n','履修上の注意\n','成績評価の方法\n','教科書・参考書等\n','関連科目\n','リンク先ホームページアドレス\n','備考\n']

sy = syllabus()

fw = open("maketxt.txt",'r', encoding="UTF-8")

txt = fw.readlines()

fw.close()

cnt = 1

for i in range(len(txt)):
    if(txt[i] == sy_title[1] and txt[i+1] != sy_title[2]):
        sy.classname = txt[i+1]
    if(txt[i] == sy_title[2] and txt[i+1] != sy_title[3]):
        sy.classname = sy.classname + txt[i+1]
    elif(txt[i] == sy_title[3] and txt[i+1] != sy_title[4]):
        sy.teacher = txt[i+1]
    elif(txt[i] == sy_title[4] and txt[i+1] != sy_title[5]):
        sy.classcategory = txt[i+1]
    elif(txt[i] == sy_title[5] and txt[i+1] != sy_title[6]):
        sy.classtype = txt[i+1]
    elif(txt[i] == sy_title[6] and txt[i+1] != sy_title[7]):
        sy.coc = txt[i+1]
    elif(txt[i] == sy_title[7] and txt[i+1] != sy_title[8]):
        sy.period = txt[i+1]
    elif(txt[i] == sy_title[8] and txt[i+1] != sy_title[9]):
        sy.faculty = txt[i+1]
    elif(txt[i] == sy_title[9] and txt[i+1] != sy_title[10]):
        sy.grade = txt[i+1]
    elif(txt[i] == sy_title[10] and txt[i+1] != sy_title[11]):
        sy.classregcode = txt[i+1]
    elif(txt[i] == sy_title[11] and txt[i+1] != sy_title[12]):
        sy.credit = txt[i+1]
    elif(txt[i] == sy_title[12] and txt[i+1] != sy_title[13]):
        sy.classnumcode = txt[i+1]
    elif(txt[i] == sy_title[13] and txt[i+1] != sy_title[14]):
        sy.latestupdate = txt[i+1]
    elif(txt[i] == sy_title[14] and txt[i+1] != sy_title[15]):
        while(txt[i+cnt]!=sy_title[15]):
            sy.officehours = sy.officehours + txt[i+cnt]
            cnt += 1
        cnt = 1
    elif(txt[i] == sy_title[15] and txt[i+1] != sy_title[16]):
        while(txt[i+cnt]!=sy_title[16]):
            sy.rtadvice = sy.rtadvice + txt[i+cnt]
            cnt += 1
        cnt = 1
    elif(txt[i] == sy_title[16] and txt[i+1] != sy_title[17]):
        while(txt[i+cnt]!=sy_title[17]):
            sy.objective = sy.objective + txt[i+cnt]
            cnt += 1
        cnt = 1
    elif(txt[i] == sy_title[17] and txt[i+1] != sy_title[18]):
        while(txt[i+cnt]!=sy_title[18]):
            sy.edugoals = sy.edugoals + txt[i+cnt]
            cnt += 1
        cnt = 1
    elif(txt[i] == sy_title[18] and txt[i+1] != sy_title[19]):
        while(txt[i+cnt]!=sy_title[19]):
            sy.goals = sy.goals + txt[i+cnt]
            cnt += 1
        cnt = 1
    elif(txt[i] == sy_title[19] and txt[i+1] != sy_title[20]):
        while(txt[i+cnt]!=sy_title[20]):
            sy.schedule = sy.schedule + txt[i+cnt]
            cnt += 1
        cnt = 1
    elif(txt[i] == sy_title[20] and txt[i+1] != sy_title[21]):
        while(txt[i+cnt]!=sy_title[21]):
            sy.studyoutside = sy.studyoutside + txt[i+cnt]
            cnt += 1
        cnt = 1
    elif(txt[i] == sy_title[21] and txt[i+1] != sy_title[22]):
        while(txt[i+cnt]!=sy_title[22]):
            sy.keywords = sy.keywords + txt[i+cnt]
            cnt += 1
        cnt = 1
    elif(txt[i] == sy_title[22] and txt[i+1] != sy_title[23]):
        while(txt[i+cnt]!=sy_title[23]):
            sy.notice = sy.notice + txt[i+cnt]
            cnt += 1
        cnt = 1
    elif(txt[i] == sy_title[23] and txt[i+1] != sy_title[24]):
        while(txt[i+cnt]!=sy_title[24]):
            sy.textbooks = sy.textbooks + txt[i+cnt]
            cnt += 1
        cnt = 1
    elif(txt[i] == sy_title[24] and txt[i+1] != sy_title[25]):
        while(txt[i+cnt]!=sy_title[25]):
            sy.evaluation = sy.evaluation + txt[i+cnt]
            cnt += 1
        cnt = 1
    elif(txt[i] == sy_title[25] and txt[i+1] != sy_title[26]):
        while(txt[i+cnt]!=sy_title[26]):
            sy.related = sy.related + txt[i+cnt]
            cnt += 1
        cnt = 1
    elif(txt[i] == sy_title[26] and txt[i+1] != sy_title[27]):
        while(txt[i+cnt]!=sy_title[27]):
            sy.link = sy.link + txt[i+cnt]
            cnt += 1
        cnt = 1
    elif(txt[i] == sy_title[27]):
        while(txt[i+cnt]== ''):
            sy.notes = sy.notes + txt[i+cnt]
            cnt += 1
        cnt = 1

#CSV書き込み
with open("syllabus.csv", 'w', encoding='UTF-8_sig', newline="")as csv_f:
    feildnames = ['classname','teacher','classcategory','classtype','coc','period','faculty','classregicode','grade','classnumcode','credit','latestupdate','officehours','rtadvice','objective','edugoals','goals','schedule','studyoutside','keywords','notice','textbooks','evaluation','related','link','notes']
    writer = csv.DictWriter(csv_f,fieldnames=feildnames)
    writer.writeheader()

    writetext =[sy.classname,sy.teacher,sy.classcategory,sy.coc,sy.classtype,sy.period,sy.faculty,sy.classregcode,sy.grade,sy.classnumcode,sy.credit,sy.latestupdate,sy.officehours,sy.rtadvice,sy.objective,sy.edugoals,sy.goals,sy.schedule,sy.studyoutside,sy.keywords,sy.notice,sy.textbooks,sy.evaluation,sy.related,sy.link,sy.notes]

    writer = csv.writer(csv_f)
    writer.writerow(writetext)

csv_f.close()