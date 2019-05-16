# -*- coding: utf-8 -*-
'''
Это файл является классом для работы с базой данных SQLighter
'''
import sqlite3
from config import debug

class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def select_all(self,table_numder):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM question'+table_numder).fetchall()

    def select_single(self, rownum,table_numder):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            if debug==1: print ('SQL '+'SELECT * FROM question'+table_numder+' WHERE id = ?', rownum,)
            return self.cursor.execute('SELECT * FROM question'+table_numder+' WHERE id = ?', (rownum,)).fetchall()[0]

    def count_rows(self,table_numder):
        """ Считаем количество строк """
        with self.connection:
            result = self.cursor.execute('SELECT * FROM question'+table_numder).fetchall()
            return len(result)

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()
