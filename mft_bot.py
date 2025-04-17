
import telebot
from telebot import types

BOT_TOKEN = '8094972689:AAFWi_wW6YZdCzJDGjUTm9AKDPYRIg6y1wI'
bot = telebot.TeleBot(BOT_TOKEN)

WELCOME_BONUS = 1000
REFERRAL_BONUS = 2500
MINIMUM_PAID_ORDER = 200
PAYMENT_NUMBER = '01760656083'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome to MFT Boost Bot!\n\nYou have received {WELCOME_BONUS} FREE TikTok Views as a Welcome Bonus!\nUse /order to place an order.\nUse /prices to check all services.\nRefer friends and earn {REFERRAL_BONUS} views!\n\nOwner: @maruf2611\nVisit: https://mftboost.com")


@bot.message_handler(commands=['prices'])
def send_prices(message):
    price_list = '''🔥 Our Service Price List 🔥

====================
🎯 TikTok Service
• Views: 10K = 20৳ | 1M = 1300৳
• Likes: 100 = 10৳ | 100K = 7000৳
• Followers: 1K = 430৳ | 10K = 4200৳
• Comments: 50 = 25৳
• Shares: 1K = 100৳
• Saves: 500 = 25৳

====================
📘 Facebook Service
• Views:
   - 10K = 20৳
   - 100K = 190৳
   - 500K = 900৳
   - 1M = 1700৳
• Followers:
   - 1K = 250৳
   - 10K = 2400৳
   - 100K = 23500৳
• Reactions:
   - 100 = 20৳
   - 1K = 180৳
   - 10K = 1700৳

====================
📸 Instagram Service
• Views:
   - 1K = 5৳
   - 10K = 45৳
   - 100K = 400৳
   - 500K = 1950৳
   - 1M = 3800৳
• Followers (Lifetime):
   - 1K = 500৳
   - 10K = 1000৳
• Likes:
   - 100 = 5৳
   - 1K = 40৳
   - 10K = 350৳

====================
▶️ YouTube Service
• Subscribers (Non Drop):
   - 1K = 500৳
   - 10K = 1000৳
   - 100K = 10000৳
• Watch Time:
   - 1K Hours = 4000৳
   - (More = Discount Available)
• Likes:
   - 1K = 150৳
   - 10K = 1400৳
• Comments:
   - 1 = 1৳
   - 100 = 99৳
   - 1000 = 990৳

====================
🔥 Free Fire Service
(Cooming Soon...)
Stay tuned for Diamond Top-Up, Elite Pass, Membership & more!

====================
💳 Payment Methods:
Bkash / Nagad / Upay (Personal): 01760656083

After payment, send screenshot using /submit_payment'''
    bot.send_message(message.chat.id, price_list)

bot.polling()
