# -*- coding: utf-8 -*-
"""
Создание файла формата GIFT c картинками из
Базы данных SQLLight и каталога с картинками img
Для номеров заданий из ОГЭ по информатике: 1-8,11,12,14-18
"""
import base64
import os
import utils
from SQLighter import SQLighter
import config
import random
random.seed()
#Функция для дебага, если дебаг включен, то для каждого вопроса генерируется один вариант
def for_count_r(j):
    if config.debug==1:
        return 2
    else:
        return utils.get_rows_count(j)


utils.count_rows() #подсчет строк в таблицах базы данных
db_worker = SQLighter(os.getcwd()+config.database_name) #Подключение к базе данных
start=0 #Переменная блокирующая создание множества файлов при  указании записи в один
#Генератор GIFT для заданий 1-6
for j in range(1,7):
    #Устанвока в один файл, или несколько
    if config.one_file==1 and start==0:
        f=open(os.getcwd()+"/testAll.txt","w")
        start=1
    if config.one_file==0:
        f=open(os.getcwd()+"/test"+str(j)+".txt","w")
    #Создание записи о категории
    f.write("\n")
    f.write("$CATEGORY: $cat$/top/ОГЭ Информатика/"+config.category[j-1])
    f.write("\n")
    f.write("\n")
    #Генератор GIFT для всех или одного варианта в вопросе, зависит от debug
    for i in range(1,for_count_r(j)):#,utils.get_rows_count(j)):
        row = db_worker.select_single(i,str(j)) #подключение к базе данных
        if j==5 or j==3:
            img_f = open(row[1], 'rb')
            data_url=base64.b64encode(img_f.read()).decode('ascii')
            img_f.close()
            wrong_answers=row[5].split(",")
            r=['','','','','','','']
            for r_i in [2,3,4,6]:
                r[r_i]=str(row[r_i])
                r[r_i]=r[r_i].replace("~","\\~")
                r[r_i]=r[r_i].replace("=","\\=")
                r[r_i]=r[r_i].replace("#","\\#")
                r[r_i]=r[r_i].replace("{","\\{")
                r[r_i]=r[r_i].replace("}","\\}")
                r[r_i]=r[r_i].replace("\n","<br>")
            vopros='[html]<p>{0}<img src\\="data:image/png;base64,{1}" class="img-responsive atto_image_button_text-bottom"><br>{2}</p>'.format(r[2],data_url,r[3])
            vopros=vopros+"{\n"+"="+r[4]+"\n"
            for n in range(3):
                wrong_answers[n]=wrong_answers[n].replace("~","\\~")
                wrong_answers[n]=wrong_answers[n].replace("=","\\=")
                wrong_answers[n]=wrong_answers[n].replace("#","\\#")
                wrong_answers[n]=wrong_answers[n].replace("{","\\{")
                wrong_answers[n]=wrong_answers[n].replace("}","\\}")
            vopros=vopros+"~"+wrong_answers[0]
            vopros=vopros+"#"+r[6]+"\n"
            vopros=vopros+"~"+wrong_answers[1]
            vopros=vopros+"#"+r[6]+"\n"
            vopros=vopros+"~"+wrong_answers[2]
            vopros=vopros+"#"+r[6]+"}\n"
            if utils.debug==1:print(vopros)
            f.write(vopros)
        elif j==4 or j==6:
            wrong_answers=row[5].split(",")
            r=['','','','','','','']
            for r_i in [1,2,3,4,6]:
                r[r_i]=str(row[r_i])
                r[r_i]=r[r_i].replace("~","\\~")
                r[r_i]=r[r_i].replace("=","\\=")
                r[r_i]=r[r_i].replace("#","\\#")
                r[r_i]=r[r_i].replace("{","\\{")
                r[r_i]=r[r_i].replace("}","\\}")
                r[r_i]=r[r_i].replace("\n","<br>")
            vopros="[html]<p>{0}<br>{1}<br>{2}</p>".format(r[2],r[1],r[3])
            vopros=vopros+"{\n"+"="+r[4]+"\n"
            for n in range(3):
                wrong_answers[n]=wrong_answers[n].replace("~","\\~")
                wrong_answers[n]=wrong_answers[n].replace("=","\\=")
                wrong_answers[n]=wrong_answers[n].replace("#","\\#")
                wrong_answers[n]=wrong_answers[n].replace("{","\\{")
                wrong_answers[n]=wrong_answers[n].replace("}","\\}")
            vopros=vopros+"~"+wrong_answers[0]
            vopros=vopros+"#"+r[6]+"\n"
            vopros=vopros+"~"+wrong_answers[1]
            vopros=vopros+"#"+r[6]+"\n"
            vopros=vopros+"~"+wrong_answers[2]
            vopros=vopros+"#"+r[6]+"}\n"
            if utils.debug==1:print(vopros)
            f.write(vopros)
        else:
            wrong_answers=row[5].split(",")
            r=['','','','','','','']
            for r_i in [3,4,5,6]:
                r[r_i]=str(row[r_i])
                r[r_i]=r[r_i].replace("~","\\~")
                r[r_i]=r[r_i].replace("=","\\=")
                r[r_i]=r[r_i].replace("#","\\#")
                r[r_i]=r[r_i].replace("{","\\{")
                r[r_i]=r[r_i].replace("}","\\}")
                r[r_i]=r[r_i].replace("\n","<br>")
            if j==2:
                r[3]=r[3].replace(": ",":<br>")
            vopros="[html]<p>{0}</p>".format(r[3])
            vopros=vopros+"{\n"+"="+r[4]+"\n"
            for n in range(3):
                wrong_answers[n]=wrong_answers[n].replace("~","\\~")
                wrong_answers[n]=wrong_answers[n].replace("=","\\=")
                wrong_answers[n]=wrong_answers[n].replace("#","\\#")
                wrong_answers[n]=wrong_answers[n].replace("{","\\{")
                wrong_answers[n]=wrong_answers[n].replace("}","\\}")
            vopros=vopros+"~"+wrong_answers[0]
            vopros=vopros+"#"+r[6]+"\n"
            vopros=vopros+"~"+wrong_answers[1]
            vopros=vopros+"#"+r[6]+"\n"
            vopros=vopros+"~"+wrong_answers[2]
            vopros=vopros+"#"+r[6]+"}\n"
            if utils.debug==1:print(vopros)
            f.write(vopros)
    if config.one_file==0:
        f.close()
#Генератор GIFT заданий 7,8,11,12,14-18
for j in [7,8,11,12,14,15,16,17,18]:
    #Устанвока в один файл, или несколько
    if config.one_file==1 and start==0:
        f=open(os.getcwd()+"/testAll.txt","w")
        start=1
    if config.one_file==0:
        f=open(os.getcwd()+"/test"+str(j)+".txt","w")
    f.write("\n")
    f.write("$CATEGORY: $cat$/top/ОГЭ Информатика/"+config.category[j-1])
    f.write("\n")
    f.write("\n")
    for i in range(1,for_count_r(j)):#utils.get_rows_count(j)):
        row = db_worker.select_single(i,str(j))
        r=['','','','','','','']
        for r_i in range(2,6):
            r[r_i]=str(row[r_i])
            r[r_i]=r[r_i].replace("~","\\~")
            r[r_i]=r[r_i].replace("=","\\=")
            r[r_i]=r[r_i].replace("#","\\#")
            r[r_i]=r[r_i].replace("{","\\{")
            r[r_i]=r[r_i].replace("}","\\}")
            r[r_i]=r[r_i].replace("\n","<br>")
        if j==8:
            r_i=1
            r[r_i]=str(row[r_i])
            r[r_i]=r[r_i].replace("~","\\~")
            r[r_i]=r[r_i].replace("=","\\=")
            r[r_i]=r[r_i].replace("#","\\#")
            r[r_i]=r[r_i].replace("{","\\{")
            r[r_i]=r[r_i].replace("}","\\}")
            r[r_i]=r[r_i].replace("\n","<br>")
        if j==12 or j==7:
            img_f = open(row[1], 'rb')
            data_url=base64.b64encode(img_f.read()).decode('ascii')
            vopros='[html]<p>{0}<img src\\="data:image/png;base64,{1}" class="img-responsive atto_image_button_text-bottom"><br>{2}</p>'.format(r[2],data_url,r[3])
            img_f.close()
            vopros=vopros+"{\n"+"="+r[4]
            vopros=vopros+"#"+r[5]+"}\n"
            if utils.debug==1:print(vopros)
            f.write(vopros)
        elif j==11 or j==18:
            img_f = open(row[1], 'rb')
            data_url=base64.b64encode(img_f.read()).decode('ascii')
            vopros='[html]<p><img src\\="data:image/png;base64,{0}" class="img-responsive atto_image_button_text-bottom"><br>{1}</p>'.format(data_url,r[3])
            img_f.close()
            vopros=vopros+"{\n"+"="+r[4]
            vopros=vopros+"#"+r[5]+"}\n"
            if utils.debug==1:print(vopros)
            f.write(vopros)
        elif j==8:
            vopros='[html]<p>{0}<br>{1}<br>{2}</p>'.format(r[2],r[1],r[3])
            vopros=vopros+"{\n"+"="+r[4]
            vopros=vopros+"#"+r[5]+"}\n"
            if utils.debug==1:print(vopros)
            f.write(vopros)
        else:
            vopros='[html]<p>{0}</p>'.format(r[3])
            vopros=vopros+"{\n"+"="+r[4]
            vopros=vopros+"#"+r[5]+"}\n"
            if utils.debug==1:print(vopros)
            f.write(vopros)
        if config.one_file==0:
            f.close()
# aлгоритм генерации 9-го задания
#Устанвока в один файл, или несколько
j=9
if config.one_file==1 and start==0:
    f=open(os.getcwd()+"/testAll.txt","w")
    start=1
if config.one_file==0:
    f=open(os.getcwd()+"/test"+str(j)+".txt","w")
f.write("\n")
f.write("$CATEGORY: $cat$/top/ОГЭ Информатика/"+config.category[j-1])
f.write("\n")
f.write("\n")
for i in range(1,for_count_r(j)):#utils.get_rows_count(j)):
    row = db_worker.select_single(i,str(j))
    r=['','','','','','','','','']
    for r_i in range(1,8):
            r[r_i]=row[r_i]
    for var in range(1):
        cods=['','','','']
        #генерим случайные числа для шаблонов программ
        s=random.randint(1,10)-1
        s1=random.randint(1,8)
        if r[6]=='mult' or r[6]=='aprog':
            r1=random.randint(1,3)
        else:
            r1=random.randint(4,9)
        if r[6]=='aprog':
            k1=random.randint(2,3)
        else:
            k1=random.randint(4,9)
        for code in range(2,6):
            #сохраняем в переменную текст шаюблона из базы данных
            result_code=r[code]
            #заменяем данные в шаблоне
            result_code=result_code.replace('{s}',str(s))
            result_code=result_code.replace('{k1}',str(k1))
            if code==5:
                result_code=result_code.replace('{k2}',str(k1+1+r1))
            else:
                result_code=result_code.replace('{k2}',str(k1+r1))
            result_code=result_code.replace('{s1}',str(s1))
            cods[code-2]="<pre>"+result_code+"</pre>"
            cods[code-2]=cods[code-2].replace("~","\\~")
            cods[code-2]=cods[code-2].replace("=","\\=")
            cods[code-2]=cods[code-2].replace("#","\\#")
            cods[code-2]=cods[code-2].replace("{","\\{")
            cods[code-2]=cods[code-2].replace("}","\\}")
            cods[code-2]=cods[code-2].replace("\n","<br>")
        for r_i in range(1,8):
            if r_i!=6:
                r[r_i]=row[r_i]
                r[r_i]=r[r_i].replace("~","\\~")
                r[r_i]=r[r_i].replace("=","\\=")
                r[r_i]=r[r_i].replace("#","\\#")
                r[r_i]=r[r_i].replace("{","\\{")
                r[r_i]=r[r_i].replace("}","\\}")
                r[r_i]=r[r_i].replace("\n","<br>")
        vopros=config.t_row1+"<tr>"
        vopros+=config.td_s+cods[0]+"</td>"
        vopros+=config.td_s+cods[1]+"</td></tr>"
        vopros+=config.t_row2+"<tr>"
        vopros+=config.td_s+cods[2]+"</td>"
        vopros+=config.td_s+cods[3]+"</td></tr></tbody></table>"
        vopros="<p>"+r[1]+"</p>"+vopros
        result_memorial=row[7]
        #заеняем данные в шаблоне
        result_memorial=result_memorial.replace('{s}',str(s))
        result_memorial=result_memorial.replace('{k1}',str(k1))
        result_memorial=result_memorial.replace('{k2}',str(k1+r1))
        result_memorial=result_memorial.replace('{s1}',str(s1))
        result_memorial=result_memorial.replace('{r}',str(r1+1))
        result_memorial=result_memorial.replace('{answer}',utils.generate_right_answer_9(r[6],s,s1,r1,k1))
        result_memorial=result_memorial.replace("~","\\~")
        result_memorial=result_memorial.replace("=","\\=")
        result_memorial=result_memorial.replace("#","\\#")
        result_memorial=result_memorial.replace("{","\\{")
        result_memorial=result_memorial.replace("}","\\}")
        result_memorial=result_memorial.replace("\n","<br>")
        vopros="[html]"+vopros+"{="+str(utils.generate_right_answer_9(r[6],s,s1,r1,k1))+"#"+result_memorial+"}\n"
    if utils.debug==1:print(vopros)
    f.write(vopros)
if config.one_file==0:
    f.close()
db_worker.close() #закрываем подключение к базе данных
if config.one_file==1 and start==1:
    f.close()
