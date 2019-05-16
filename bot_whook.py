

@bot.message_handler(commands=['10'])
def game_10(message):
    code=utils.set_user_code_get(message.chat.id)
    if not code or code=='':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        markup.row('/schoolalgorithm')
        markup.row('/basic', '/pascal')
        markup.row('/python')
        bot.send_message(message.chat.id, 'ВНИМАНИЕ! Не выбран предпочитаемый язык программирования!\nВыбери предпочитаемый язык программирования:\n * shoolAlgorithm - Алгоритмический язык (КУМИР)\n * basic - бейсик\n * pascal - Паскаль\n * Pyhon - Пайтон (Питон)', reply_markup=markup)
    else:
        #получаем сообщение пользователя
        message_namber=message.text
        #разбиваем сообщение на части, делитель - символ /
        answer_number=message_namber.split('/')
        # Подключаемся к БД
        db_worker = SQLighter(config.database_name)
        # Получаем случайную строку из БД по номеру таблицы взятую из сообщения answer_number
        row = db_worker.select_single(random.randint(1, utils.get_rows_count(answer_number[1])),answer_number[1])
        #Отсоединяемся от БД
        db_worker.close()
        #Генерируем значение пременной для дополнительного сообщения:
        chat_message ={
        '2':'Алгоритмический язык',
        '3':'BASIC',
        '4':'Pascal',
        '5':'Pyhon'
        }
        #генерируем случайные числа для шаблона программы из базы данных
        Dat=[random.randint(10, 20) for i in range(10)]
        #Генерируем вспомогательное число для сравнения или подсчета
        t=random.randint(10, 20)
        #сохраняем в переменную текст шаюблона из базы данных
        result_code=row[int(code)]
        #заменяем данные в шаблоне
        for i in range(10):
            result_code=result_code.replace('{dat'+str(int(i))+'}',str(Dat[i]))
        result_code=result_code.replace('{t}',str(t))
        # Отправляем вводную часть вопроса
        bot.send_message(message.chat.id,row[1])
        # Отправляем основную часть вопроса c форматированием
        bot.send_message(message.chat.id, '<pre>'+result_code+'</pre>',parse_mode='HTML')
        # Отправляем дополнительное сообщение
        bot.send_message(message.chat.id,'Текст программы приведён на языке программирования: '+chat_message[code])
        #сохраняем в переменную текст шаюблона пояснения из базы данных
        result_memorial=row[7]
        #заеняем данные в шаблоне
        result_memorial=result_memorial.replace('{t}',str(t))
        result_memorial=result_memorial.replace('{answer}',utils.generate_right_answer_10(row[6],Dat,t))
        # Включаем "игровой режим"... ждем ответа от пользователя
        utils.set_user_game(message.chat.id, utils.generate_right_answer_10(row[6],Dat,t),result_memorial)

@bot.message_handler(commands=['13'])
def game_13(message):
    #получаем сообщение пользователя
    message_namber=message.text
    #разбиваем сообщение на части, делитель - символ /
    answer_number=message_namber.split('/')
    # Подключаемся к БД
    base1=random.randint(0,3)
    if base1==0 or base1==1 or base1==2:
        base2=3
    elif base1==3:
        base2=random.randint(0,2)
    chislo=random.randint(101,255)
    base_text1 =['двоичное','восьмиричное','шестнадцатеричное','десятичное']
    base_number=[2,8,16,10]
    base_text2 =['двоичную','восьмиричную','шестнадцатеричную','десятичную']
    text_mesaage='Переведите '+base_text1[base1]+' число '+utils.convert_base(chislo,base_number[base1],10)+' в '+base_text2[base2]+' систему счисления.'
    ra=utils.convert_base(chislo,base_number[base2],10)
    # Отправляем вопрос
    bot.send_message(message.chat.id,text_mesaage)
    # Включаем "игровой режим"... ждем ответа от пользователя
    utils.set_user_game(message.chat.id, ra,'Пример решения доступен по ссылке https://youtu.be/uETzw6WP_FM')
