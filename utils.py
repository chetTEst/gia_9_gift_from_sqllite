# -*- coding: utf-8 -*-
'''
Телеграмм бот версии 0.12 для подготовки к ГИА по информатике
Бот написан учителем информатики Четверовым Алексеем Владимировичем
Бот основан на уроках по созданию музыкальной викторины https://www.gitbook.com/book/groosha/telegram-bot-lessons/details
Использована библиотека pyTelegramBotAPI https://github.com/eternnoir/pyTelegramBotAPI
В качестве источника данных для заданий используется база данных SQLLight
Информация о пользователях сохраняется в формете ключ-запись в отдельном файле
Этот файл функций работы с базами данных и форматирования ответов
'''
import shelve
from SQLighter import SQLighter
from config import shelve_name, database_name, debug
from random import shuffle
import os

def count_rows():
    """
    Данный метод считает общее количество строк в базе данных и сохраняет в хранилище.
    Потом из этого количества будем выбирать музыку.
    """
    print(os.getcwd()+database_name)
    db = SQLighter(os.getcwd()+database_name)
    rowsnum1 = db.count_rows('1')
    rowsnum2 = db.count_rows('2')
    rowsnum3 = db.count_rows('3')
    rowsnum4 = db.count_rows('4')
    rowsnum5 = db.count_rows('5')
    rowsnum6 = db.count_rows('6')
    rowsnum7 = db.count_rows('7')
    rowsnum8 = db.count_rows('8')
    rowsnum9 = db.count_rows('9')
    rowsnum10 = db.count_rows('10')
    rowsnum11 = db.count_rows('11')
    rowsnum12 = db.count_rows('12')
    rowsnum13=0
    rowsnum14 = db.count_rows('14')
    rowsnum15 = db.count_rows('15')
    rowsnum16 = db.count_rows('16')
    rowsnum17 = db.count_rows('17')
    rowsnum18 = db.count_rows('18')
    with shelve.open(os.getcwd()+shelve_name) as storage:
        storage['rows_count'] =[rowsnum1,rowsnum2,rowsnum3,rowsnum4,rowsnum5,rowsnum6,rowsnum7,rowsnum8,rowsnum9,rowsnum10,rowsnum11,rowsnum12,rowsnum13,rowsnum14,rowsnum15,rowsnum16,rowsnum17,rowsnum18]
        if debug==1: print (storage['rows_count'])


def get_rows_count(table_number):
    """
    Получает из хранилища количество строк в БД
    :return: (int) Число строк
    """
    with shelve.open(os.getcwd()+shelve_name) as storage:
        rowsnum = storage['rows_count']
        if debug==1: print ('rowsnum = ',rowsnum)
        if debug==1: print ('table_number = ',int(table_number)-1)
        if debug==1: print ('table_number_rowsnum = ',rowsnum [int(table_number)-1])
    return rowsnum [int(table_number)-1]

# функция вычисления правильного ответа для 9-го задания.
def generate_right_answer_9(right_answer,s,s1,r,k1):
    if right_answer=='add':
        return str(int(s+s1*(r+1)))
    if right_answer=='mult':
        return str(int(s*pow(s1,(r+1))))
    if right_answer=='aprog':
        for k in range(k1, k1+r+1):
            s = s+s1*k
        return str(int(s))
    if right_answer=='sub':
        return str(int(s-s1*(r+1)))

#функция вычисления правильного ответа для 10-го задания.
def generate_right_answer_10(right_answer,list1,k):
    if right_answer=='count':
        return str(list1.count(k))
    if right_answer=='min':
        return str(min(list1))
    if right_answer=='max':
        return str(max(list1))
    if right_answer=='minindex':
        return str(list1.index(min(list1)))
    if right_answer=='maxindex':
        return str(list1.index(max(list1)))
    if right_answer=='more':
        m=0
        for j in range(10):
            if list1[j]>k:
                m=m+1
        return str(int(m))
    if right_answer=='less':
        m=0
        for j in range(10):
            if list1[j]>k:
                m=m+1
        return str(int(m))
    if right_answer=='summ':
        m=0
        for j in range(10):
            if list1[j]>k:
                m=m+list1[j]
        return str(int(m))
#Функция перевода из одной системы счисления в другую
def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]
