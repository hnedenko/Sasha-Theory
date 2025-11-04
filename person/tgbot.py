"""
import telebot


token = "8440596286:AAFFg_F58LnyO7a0wykk5B8FrirDAmHakp4"

bot = telebot.TeleBot(token)

bot.polling(none_stop=True, interval=0)

@bot.message_handler(content_types=['text'])
async def get_message(self, message):
    print(message)
    return message
"""