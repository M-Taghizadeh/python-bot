import telebot

TOKEN = '5821119327:AAG9ddgr14MYFeZIngOGDMh7w0qyH5s4hyY'
bot = telebot.TeleBot(TOKEN)
CHANNEL_ID = '@ai_news_farsi'

@bot.message_handler(commands=['send_text'])
def send_text_to_channel(message):
    try:
        text_to_send = message.text.replace('/send_text', '').strip()
        bot.send_message(CHANNEL_ID, text_to_send)
        bot.reply_to(message, 'متن با موفقیت در کانال ارسال شد.')
    except Exception as e:
        bot.reply_to(message, f'خطا در ارسال متن: {str(e)}')

# شروع پردازش ربات
bot.polling()
