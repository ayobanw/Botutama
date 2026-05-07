import telebot
import threading
from flask import Flask
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- ENGINE RENDER (WAJIB UNTUK LIVE 24 JAM) ---
app = Flask('')
@app.route('/')
def home(): return "Bot is alive!"
def run(): app.run(host='0.0.0.0', port=10000)

# --- CONFIG BOT ANW STORE ---
TOKEN = "8300282726:AAEeRUjkbOyDWMfUgwFs-hHrY5AP_Hu16T0"
bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")

CHANNEL_ID = -1002447953683  
CHANNEL_LINK = "https://t.me/+3x10prkLlfl2ODll"
ADMIN_LINK = "https://t.me/ayobanw"
TOOL_LINK = "https://anwstore.my.id"
IMAGE_URL = "https://files.catbox.moe/b39056.jpg" 

def main_menu():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("🛠 Tool", url=TOOL_LINK),
        InlineKeyboardButton("💎 CODE KERETA", callback_data="kereta_menu"),
        InlineKeyboardButton("⚒️ CUSTOM SPOILER & BESI", callback_data="custom_menu"),
        InlineKeyboardButton("💼 Admin", url=ADMIN_LINK),
        InlineKeyboardButton("📹 VIDEO ACC", url=CHANNEL_LINK)
    )
    return kb

def is_subscribed(user_id):
    try:
        status = bot.get_chat_member(CHANNEL_ID, user_id).status
        return status in ['member', 'administrator', 'creator']
    except:
        return False

@bot.message_handler(commands=['start'])
def start(msg):
    if is_subscribed(msg.from_user.id):
        bot.send_photo(msg.chat.id, IMAGE_URL, caption="🏠 *Menu Utama ANW STORE*", reply_markup=main_menu())
    else:
        kb = InlineKeyboardMarkup()
        kb.add(InlineKeyboardButton("✅ JOIN GROUP DULU", url=CHANNEL_LINK))
        kb.add(InlineKeyboardButton("🔄 SAYA DAH JOIN", callback_data="check_status"))
        bot.send_message(msg.chat.id, "❌ *Kena join group dulu baru boleh guna bot ni!*", reply_markup=kb)

@bot.callback_query_handler(func=lambda c: c.data == "check_status")
def check_status(call):
    if is_subscribed(call.from_user.id):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id, IMAGE_URL, caption="🏠 *Menu Utama ANW STORE*", reply_markup=main_menu())
    else:
        bot.answer_callback_query(call.id, "⚠️ Awak belum join lagi!", show_alert=True)

# --- LIST KERETA (IKUT FORMAT SEBARIS KE BAWAH) ---
@bot.callback_query_handler(func=lambda c: c.data == "kereta_menu")
def kereta_menu(call):
    text = (
        "🏎️ *LIST CODE KERETA*\n\n"
        "202 Pagani Zonda\n"
        "204 Mercedes Van\n"
        "205 Porsche RWB\n"
        "206 Alfa Romeo Giulia\n"
        "207 Porsche Le Mans\n"
        "208 Ford Bronco\n"
        "209 Lexus IS300 2009\n"
        "210 Corvette C5\n"
        "211 Audi RS7\n"
        "212 6x6 Mercedes G63\n"
        "213 Nissan R33\n"
        "214 Toyota Chaser MK2\n"
        "215 Chevy Tahoe\n"
        "216 McLaren Senna\n"
        "217 BMW X7\n"
        "218 Toyota Crown\n"
        "219 VW Passat\n"
        "220 Fairlady Z\n"
        "221 Old NSX\n"
        "222 Porsche 918\n"
        "223 DMC Delorean\n"
        "224 Subaru Raptor Eye\n"
        "225 Honda DelSol\n"
        "226 Fiat Van\n"
        "227 AMG One\n"
        "228 Audi RS2\n"
        "229 Ferrari F40\n"
        "230 Land Rover\n"
        "231 Toyota LC250 Old\n"
        "232 Kia Stinger\n"
        "233 BMW i7\n"
        "234 Newer Aston Martin\n"
        "235 Newer Mustang\n"
        "236 RV\n"
        "237 Semi Truck\n"
        "238 New BMW M5\n"
        "239 New Escalade\n"
        "240 Ford Focus\n"
        "241 LaFerrari\n"
        "242 New Camaro\n"
        "243 Jeep Gladiator\n"
        "244 New Land Rover\n"
        "245 Toyota GR Yaris\n"
        "248 New Russian Car\n"
        "249 New Maybach\n"
        "250 Porsche Carrera GT\n"
        "253 FORD TURCKS NEW\n"
        "257 BMW M2 NEW\n"
        "259 FORTUNER NEW"
    )
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("⬅ Kembali", callback_data="back_menu"))
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=kb)
