import telebot

TOKEN = '5732193076:AAHMDBj2KG-DvfHF_LQW7Xak6hg9UgX-UaY'

#Init the  bot with token
bot = telebot.TeleBot(TOKEN)

#To catch the message you need to use this decorator. 
@bot.message_handler(commands=['start'])
def send_hello(message):
    bot.reply_to(message, "What do you want to learn?")

@bot.message_handler(func=lambda message: message.text == 'dragon design')  # When user types 'youtube' 
def youtube_line(message):  # Send the YouTube line 
    bot.reply_to(message, "https://youtu.be/2t6DFCekCV0")

@bot.message_handler(content_types=['text'])
def send_link(message):
    if message.text == 'design':
        bot.send_message(message, 'https://youtu.be/4a9OOpoA2k0')

@bot.message_handler(content_types=['text'])
def send_youtube_link(message):
    if message.text == 'vibrating circle design':
        bot.send_message(message, 'https://youtu.be/N1SXaowmTEM')



  
#Launches the bot in infinite loop mode with additional
#...exception handling, which allows the bot
#...to work even in case of errors. 
bot.infinity_polling()
