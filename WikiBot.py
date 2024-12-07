import telebot
from wikipedia import set_lang, summary

set_lang('ru')

TOKEN = 'BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я могу найти информацию в Википедии. Просто отправьте мне название статьи.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        article_title = message.text.strip()
        article_summary = summary(article_title, sentences=3)
        bot.reply_to(message, f'Вот краткая информация о статье "{article_title}":\n\n{article_summary}')

    except Exception as e:
        bot.reply_to(message, f'К сожалению, произошла ошибка при поиске статьи: {e}. Попробуйте ещё раз.')

if __name__ == '__main__':
    bot.polling(none_stop=True)