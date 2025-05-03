import telebot 
import openai 

# Установка ключа API для OpenAI 
openai.api_key = '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'

# Установка прокси 
openai.proxy = { 
    "https": "13.38.176.104", 
} 

# Создание экземпляра бота 
bot = telebot.TeleBot('7622630770:AAHu_b5OrPxPfwTNqphMN688X2wSwx2l5RU') 

@bot.message_handler(commands=['start']) 
def welcome(message): 
    bot.send_message(message.chat.id, 'Привет, это ChatGPT в телеграм.') 

@bot.message_handler(content_types=['text']) 
def talk(message): 
    try: 
        # Получение ответа от GPT 
        response = openai.Completion.create( 
            model="text-davinci-003", 
            prompt=message.text, 
            temperature=0.5, 
            max_tokens=1000, 
            top_p=1.0, 
            frequency_penalty=0.5, 
            presence_penalty=0.5, 
        ) 
        gpt_text = response['choices'][0]['text'] 
        # Отправка ответа пользователю 
        bot.send_message(message.chat.id, gpt_text) 
    except Exception as e: 
        # Обработка ошибок 
        bot.send_message(message.chat.id, f"Ошибка: {e}") 

# Запуск бота 
bot.polling(non_stop=True)