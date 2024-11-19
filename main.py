from keep_alive import keep_alive
import telebot
from telebot.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
import os

# Start keep_alive to prevent bot from sleeping
keep_alive()

# Use environment variables from Repl.it secrets
BOT_TOKEN = os.environ['BOT_TOKEN']
WEBAPP_URL = os.environ['WEBAPP_URL']

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Create inline keyboard with multiple buttons
    markup = InlineKeyboardMarkup()
    
    # Game button
    webapp_button = InlineKeyboardButton(
        "Play PUMP GOLF", 
        web_app=WebAppInfo(url=WEBAPP_URL)
    )
    
    # X (Twitter) button
    x_button = InlineKeyboardButton(
        "X (Twitter)", 
        url="https://x.com/wegolfhere"
    )
    
    # Telegram button
    telegram_button = InlineKeyboardButton(
        "Telegram Group", 
        url="https://t.me/PUMPGOLF"
    )
    
    # Add buttons to markup
    markup.row(webapp_button)
    markup.row(x_button, telegram_button)
    
    bot.reply_to(
        message, 
        "Welcome to PUMP GOLF! Choose an option:", 
        reply_markup=markup
    )

# Start the bot
bot.polling()