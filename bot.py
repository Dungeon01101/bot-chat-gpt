import telebot
import sqlite3
from config import *

bot = telebot.TeleBot(TOKEN)

DATABASE_FILE = 'telegram_users.db'

#subscribe = False

def create_table():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username_id TEXT UNIQUE NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def add_user(username_id):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username_id) VALUES (?)", (username_id,))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False


def check_user(username_id):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username_id = ?", (username_id,))
    user = cursor.fetchone()
    conn.close()
    return user is not None

@bot.message_handler(commands=['start'])
def lalala(message):
    chat_id = message.chat.id
    username_id = message.from_user.id
    
    bot.send_message(chat_id, "Привет!\nПиши эти команды:\n/start - Перезапустить бота\n/subscribe - проверить подписку\n/buy - купить подписку")

@bot.message_handler(commands=['subscribe'])
def lalalas(message):
    username_id = message.from_user.id
    chat_id = message.chat.id
    if check_user(username_id):
        bot.send_message(chat_id, f"У вас есть подписка.")
    else:
        bot.send_message(chat_id, f"У вас нет подписки.\nЧто бы её купить напишите /buy")

@bot.message_handler(commands=['buy'])
def lalalas(message):
    username_id = message.from_user.id
    chat_id = message.chat.id
    if check_user(username_id):
        bot.send_message(chat_id, f"У вас уже есть подписка.")
    else:
        def process_reply(message):
            if message.text == 'REG':
                add_user(username_id)
                bot.send_message(chat_id, "Вы приобрели подписку.")
            else:
                bot.send_message(chat_id, "Вы не то написали.")
        bot.send_message(chat_id, f"У нет подписки, напишите 'REG', чтобы её купить.")
        bot.register_next_step_handler(message, process_reply)


if __name__ == "__main__":
    create_table()
    bot.infinity_polling()