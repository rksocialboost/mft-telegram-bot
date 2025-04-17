import telebot from telebot import types

BOT_TOKEN = '8094972689:AAFWi_wW6YZdCzJDGjUTm9AKDPYRIg6y1wI' ADMIN_ID = 6713400609 bot = telebot.TeleBot(BOT_TOKEN)

WELCOME_BONUS = 1000 REFERRAL_BONUS = 2500 MINIMUM_PAID_ORDER = 200 PAYMENT_NUMBER = '01760656083'

user_data = {}  # Stores user_id: {'bonus_used': False, 'referrals': [], 'balance': int, 'orders': list}

@bot.message_handler(commands=['start']) def send_welcome(message): user_id = message.from_user.id if user_id not in user_data: user_data[user_id] = { 'bonus_used': False, 'referrals': [], 'balance': WELCOME_BONUS, 'orders': [] } if len(message.text.split()) > 1: referrer_id = int(message.text.split()[1]) if referrer_id != user_id and referrer_id in user_data: user_data[referrer_id]['referrals'].append(user_id) user_data[referrer_id]['balance'] += REFERRAL_BONUS bot.send_message(referrer_id, f"You got {REFERRAL_BONUS} bonus views from a new referral!") bot.send_message(user_id, f"Welcome to MFT Boost Bot!\n\nYou have received {WELCOME_BONUS} FREE TikTok Views as a Welcome Bonus!\nUse /order to place an order.\nUse /prices to check all services.\nUse /refer to get your invite link.\nRefer friends and earn {REFERRAL_BONUS} views!")

@bot.message_handler(commands=['refer']) def send_referral_link(message): user_id = message.from_user.id link = f"https://t.me/Rksocialboostbot?start={user_id}" count = len(user_data.get(user_id, {}).get('referrals', [])) bot.send_message(user_id, f"Invite your friends using this link:\n{link}\n\nYou’ve referred {count} friend(s). Earn {REFERRAL_BONUS} views per referral!")

@bot.message_handler(commands=['balance']) def check_balance(message): user_id = message.from_user.id if user_id in user_data: balance = user_data[user_id]['balance'] bot.send_message(user_id, f"Your current balance: {balance} views") else: bot.send_message(user_id, "You don't have an account yet. Please send /start to begin.")

@bot.message_handler(commands=['submit_payment']) def submit_payment(message): msg = bot.send_message(message.chat.id, "Please send your payment details below in the following format:\n\nAmount: 100৳\nTransaction ID: XXXXX\nNumber Used: 017XXXXXXXX") bot.register_next_step_handler(msg, forward_payment_to_admin)

def forward_payment_to_admin(message): user = message.from_user text = f"Payment Submission\nFrom: @{user.username} ({user.id})\nMessage: {message.text}" bot.send_message(ADMIN_ID, text) bot.send_message(user.id, "Your payment has been submitted to admin. You will receive points shortly if verified.")

@bot.message_handler(commands=['add_points']) def add_points(message): if message.from_user.id != ADMIN_ID: return try: _, user_id, points = message.text.split() user_id = int(user_id) points = int(points) if user_id in user_data: user_data[user_id]['balance'] += points bot.send_message(user_id, f"Your balance has been updated. You received {points} views.") bot.send_message(ADMIN_ID, f"Successfully added {points} views to user {user_id}.") else: bot.send_message(ADMIN_ID, "User not found.") except Exception as e: bot.send_message(ADMIN_ID, "Usage: /add_points user_id amount\nExample: /add_points 12345678 1000")

@bot.message_handler(commands=['order']) def place_order(message): msg = bot.send_message(message.chat.id, "Please send your TikTok video link and the number of views you want to order (must be within your balance).\nExample:\nhttps://www.tiktok.com/@user/video/1234567890\nViews: 1000") bot.register_next_step_handler(msg, store_order)

def store_order(message): user_id = message.from_user.id if user_id not in user_data: bot.send_message(user_id, "Please send /start first.") return user_data[user_id]['orders'].append(message.text) bot.send_message(user_id, "✅ Your order has been received. It will be processed shortly.") bot.send_message(ADMIN_ID, f"New Order from {user_id}:\n{message.text}")

@bot.message_handler(commands=['my_orders']) def show_orders(message): user_id = message.from_user.id orders = user_data.get(user_id, {}).get('orders', []) if orders: reply = "📦 Your Orders:\n\n" + "\n---\n".join(orders) else: reply = "You haven't placed any orders yet. Use /order to get started." bot.send_message(user_id, reply)

@bot.message_handler(commands=['prices']) def send_prices(message): price_list = '''🔥 Our Service Price List 🔥

==================== 🎯 TikTok Service • Views: 10K = 20৳ | 1M = 1300৳ • Likes: 100 = 10৳ | 100K = 7000৳ • Followers: 1K = 430৳ | 10K = 4200৳ • Comments: 50 = 25৳ • Shares: 1K = 100৳ • Saves: 500 = 25৳

==================== 📘 Facebook Service • Views:

10K = 20৳

100K = 190৳

500K = 900৳

1M = 1700৳ • Followers:

1K = 250৳

10K = 2400৳

100K = 23500৳ • Reactions:

100 = 20৳

1K = 180৳

10K = 1700৳


==================== 📸 Instagram Service • Views:

1K = 5৳

10K = 45৳

100K = 400৳

500K = 1950৳

1M = 3800৳ • Followers (Lifetime):

1K = 500৳

10K = 1000৳ • Likes:

100 = 5৳

1K = 40৳

10K = 350৳


==================== ▶️ YouTube Service • Subscribers (Non Drop):

1K = 500৳

10K = 1000৳

100K = 10000৳ • Watch Time:

1K Hours = 4000৳

(More = Discount Available) • Likes:

1K = 150৳

10K = 1400৳ • Comments:

1 = 1৳

100 = 99৳

1000 = 990৳


==================== 🔥 Free Fire Service (Cooming Soon...) Stay tuned for Diamond Top-Up, Elite Pass, Membership & more!

==================== 💳 Payment Methods: Bkash / Nagad / Upay (Personal): 01760656083

After payment, send screenshot using /submit_payment''' bot.send_message(message.chat.id, price_list)

@bot.message_handler(commands=['help']) def help_command(message): help_text = '''🤖 Bot Command Guide 🤖

/start - Start the bot and get welcome bonus /refer - Get your referral link and count /order - Submit your video link and views to order /my_orders - Show your order history /prices - See all service prices /balance - Check your view balance /submit_payment - Submit your payment details /help - Show this help message''' bot.send_message(message.chat.id, help_text, parse_mode='Markdown')

bot.polling()
