# -*- coding: utf-8 -*-
"""
Конфигурационный файл
База данных с заданиями
debug - Режим Дебага (Установить в 0 для отключения)
one_file - генерация одного или нескольких файлов по вопросам (Установить в 0 для отключения)
var9 - кол-во примеров для каждого варианта 9-го задания
var10 - кол-во примеров для каждого варианта 10-го задания
var13 - кол-во примеров для каждого варианта 13-го задания
"""
database_name = '/db/inf9gia.db'  # Файл с базой данных
shelve_name = '/db/shelve'  # Файл с хранилищем
debug=1
one_file=0
var9=1
var10=1
var13=1
category=[
"Количественные параметры информационных объектов",
"Значение логического выражения",
"Формальные описания реальных объектов и процессов",
"Файловая система организации данных",
"Формульная зависимость в графическом виде",
"Алгоритм для конкретного исполнителя с фиксированным набором команд",
"Кодирование и декодирование информации",
"Линейный алгоритм, записанный на алгоритмическом языке",
"Простейший циклический алгоритм, записанный на алгоритмическом языке",
"Циклический алгоритм обработки массива чисел, записанный на алгоритмическом языке",
"Анализирование информации, представленной в виде схем",
"Осуществление поиска в готовой базе данных по сформулированному условию",
"Дискретная форма представления числовой, текстовой, графической и звуковой информации",
"Простой линейный алгоритм для формального исполнителя",
"Скорость передачи информации",
"Алгоритм, записанный на естественном языке, обрабатывающий цепочки символов или списки",
"Информационно-коммуникационные технологии",
"Осуществление поиска информации в Интернете"
]
t_row1="""
<table>
<tbody><tr>
<td style="text-align: center; border-width: 1px; border-style: solid; border-color: rgb(51, 51, 51);"><b>Алгоритмический язык</b></td>
<td style="text-align: center; border-width: 1px; border-style: solid; border-color: rgb(51, 51, 51);"><b>BASIC</b></td>
</tr>
"""
td_s='<td style="border-width: 1px; border-style: solid; border-color: rgb(51, 51, 51);">'
t_row2="""
<tr>
<td style="text-align: center; border-width: 1px; border-style: solid; border-color: rgb(51, 51, 51);"><b>Pascal</b></td>
<td style="text-align: center; border-width: 1px; border-style: solid; border-color: rgb(51, 51, 51);"><b>Python</b></td>
</tr>
"""
