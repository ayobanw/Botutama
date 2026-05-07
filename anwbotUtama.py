import telebot
import threading
from flask import Flask
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- ENJIN RENDER (WAJIB ADA) ---
app = Flask('')
@app.route('/')
def home(): return "Bot is alive!"
def run(): app.run(host='0.0.0.0', port=8080)

# --- CONFIG ASAL AWAK ---
TOKEN = "8300282726:AAEeRUjkbOyDWMfUgwFs-hHrY5AP_Hu16T0"
bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")

# Ganti ID Group & Link Gambar ikut yang asal awak punya
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

# --- FUNGSI ASAL: WAJIB JOIN GROUP ---
def is_subscribed(user_id):
    try:
        status = bot.get_chat_member(CHANNEL_ID, user_id).status
        return status in ['member', 'administrator', 'creator']
    except:
        return False

@bot.message_handler(commands=['start'])
def start(msg):
    if is_subscribed(msg.from_user.id):
        # Kalau dah join, hantar GAMBAR + MENU
        bot.send_photo(
            msg.chat.id, 
            IMAGE_URL, 
            caption="🏠 *Menu Utama ANW STORE*", 
            reply_markup=main_menu()
        )
    else:
        # Kalau belum join, paksa join
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

# --- SEMUA LIST KERETA & BESI (IKUT ASAL 100%) ---
@bot.callback_query_handler(func=lambda c: c.data == "kereta_menu")
def kereta_menu(call):
    text = (
        "🏎️ *LIST CODE KERETA*\n\n"
        "202 Pagani Zonda\n204 Mercedes Van\n205 Porsche RWB\n206 Alfa Romeo Giulia\n"
        "207 Porsche Le Mans\n208 Ford Bronco\n209 Lexus IS300 2009\n210 Corvette C5\n"
        "211 Audi RS7\n212 6x6 Mercedes G63\n213 Nissan R33\n214 Toyota Chaser MK2\n"
        "215 Chevy Tahoe\n216 McLaren Senna\n217 BMW X7\n218 Toyota Crown\n"
        "219 VW Passat\n220 Fairlady Z\n221 Old NSX\n222 Porsche 918\n"
        "223 DMC Delorean\n224 Subaru Raptor Eye\n225 Honda DelSol\n226 Fiat Van\n"
        "227 AMG One\n228 Audi RS2\n229 Ferrari F40\n230 Land Rover\n"
        "231 Toyota LC250 Old\n232 Kia Stinger\n233 BMW i7\n234 Newer Aston Martin\n"
        "235 Newer Mustang\n236 RV\n237 Semi Truck\n238 New BMW M5\n"
        "239 New Escalade\n240 Ford Focus\n241 LaFerrari\n242 New Camaro\n"
        "243 Jeep Gladiator\n244 New Land Rover\n245 Toyota GR Yaris\n"
        "248 New Russian Car\n249 New Maybach\n250 Porsche Carrera GT\n"
        "253 FORD TURCKS NEW\n257 BMW M2 NEW\n259 FORTUNER NEW"
    )
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("⬅ Kembali", callback_data="back_menu"))
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=kb)
