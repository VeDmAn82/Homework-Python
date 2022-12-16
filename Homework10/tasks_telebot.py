# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

# Задача 2. Добавьте боту модуль, который позволяет считывать из файла вопрос, 
# отвечать на него и отправлять ответ обратно пользователю

import telebot

bot = telebot.TeleBot("5821072722:AAEbVsW-Yp_soyzja3Gt99Fy7kZ975CvEJ0", parse_mode=None)

run_question = False
run_answer = False

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, как твои дела?")
   
@bot.message_handler(content_types=["text"])
def hello_user(message):

    global run_question
    global run_answer

    # Задача1
    if run_question:     
        data = open('questions.txt','a+', encoding='utf-8')
        data.writelines(f"{str(message.from_user.id)} {message.from_user.first_name}: {message.text} \n")
        data.close()
        bot.send_message(message.from_user.id, 'Ваш вопрос сохранен!')
        run_question = False

    # Задача2
    elif run_answer:
        data = open('questions.txt','r+', encoding='utf-8')
        answer = data.readlines()
        data.close()
        bot.send_message(message, message.text)                    
        run_answer = False

    elif message.text == 'вопрос':
        run_question = True
        bot.reply_to(message, 'Задайте ваш вопрос')
    elif message.text == 'ответ':
        run_answer = True
        data = open('questions.txt','r+', encoding='utf-8')
        answer = data.readlines()
        data.close()
        bot.reply_to(message, answer)        


bot.infinity_polling()