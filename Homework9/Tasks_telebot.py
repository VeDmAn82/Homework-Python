# Задача 1. Добавьте telegram-боту возможность вычислять выражения: 1 + 4 * 2 -> 9

import telebot
import requests
import time
from random import randint

bot = telebot.TeleBot("TOKEN", parse_mode=None)

run_game = False
run_calc = False
result = None

@bot.message_handler(commands=['start', 'help', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Привет, как твои дела?")
   
@bot.message_handler(content_types=["text"])
def hello_user(message):

    global number
    global count
    global run_game
    global run_calc
    global result

    if run_game:       
        if message.text.isdigit():
            input_number = int(message.text)            
            if input_number > number:
                bot.send_message(message.from_user.id, 'Загаданное число меньше!')                
            elif input_number < number:
                bot.send_message(message.from_user.id, 'Загаданное число больше!')
            else:                
                run_game = False
                bot.send_message(message.from_user.id, f'Ты победил! Загаднное число {number}')
                bot.send_message(message.from_user.id, f'Количество твоих попыток: {count}')
            count = count + 1
        elif message.text == 'стоп':
            run_game = False
            bot.send_message(message.from_user.id, 'Игра закончена')
    
    elif run_calc:                
        exp = str(message.text)      
        if '+' in exp:
            exp = exp.split('+')            
            for number in exp:                       
                result = int(exp[0]) + int(exp[1])               
            bot.send_message(message.from_user.id, f'{message.text} = {result}')
            result = None
        elif '-' in exp:
            exp = exp.split('-')            
            for number in exp:                       
                result = int(exp[0]) - int(exp[1])
            bot.send_message(message.from_user.id, f'{message.text} = {result}')
            result = None
        elif '*' in exp:
            exp = exp.split('*')
            for number in exp:
                result = int(exp[0]) * int(exp[1])                    
            bot.send_message(message.from_user.id, f'{message.text} = {result}')
            result = None
        elif '/' in exp:
            exp = exp.split('/')
            for number in exp:
                result = int(exp[0]) / int(exp[1])                    
            bot.send_message(message.from_user.id, f'{message.text} = {result}')
            result = None
        elif message.text == 'стоп':
            run_calc = False
            bot.send_message(message.from_user.id, 'Вы вышли из калькулятора')

    else:
        if 'привет' in message.text:                           
            bot.reply_to(message, 'привет, ' + message.from_user.first_name)
        elif message.text == 'погода':                         
            r = requests.get('https://wttr.in/?0T')
            bot.reply_to(message, r.text)
        elif message.text == 'котик':                          
            r = f'https://cataas.com/cat?t=${time.time()}'
            bot.send_photo(message.chat.id, r)
        elif message.text == 'файл':                           
            data = open('user_message.txt', encoding='utf-8')  
            bot.send_document(message.chat.id, data)
            data.close()
        elif message.text == 'играть':
            number = randint(1, 1001)
            count = 0
            run_game = True
            bot.reply_to(message, f'Угадай число от 1 до 1000. Для выхода из игры введи слово "стоп".')
            bot.send_message(message.from_user.id, 'Введи число')
        elif message.text == 'калькулятор':
            run_calc = True
            result = None
            bot.reply_to(message, 'Введи выражение "a+b", используя знаки +, -, *, /')
            bot.send_message(message.from_user.id, 'Для выхода введи "стоп"')    

    data = open('user_message.txt', 'a+', encoding='utf-8')                                                                                              
    data.writelines(str(message.from_user.id) + ' ' + message.text + '\n')
    data.close()


bot.infinity_polling()