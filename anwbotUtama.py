from flask import Flask
import threading
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ================= SERVER UNTUK RENDER =================
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

# ================= CONFIG BOT =================
TOKEN = "8300282726:AAEeRUjkbOyDWMfUgwFs-hHrY5AP_Hu16T0"
bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")

ADMIN_LINK = "https://t.me/ayobanw"
TOOL_LINK = "https://anwstore.my.id"
CHANNEL_ACC_CPM = "https://t.me/+3x10prkLlfl2ODll"

# ================= KEYBOARD MENU =================
def main_menu():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("🛠 Tool", url=TOOL_LINK),
        InlineKeyboardButton("💎 CODE KERETA", callback_data="kereta_menu"),
        InlineKeyboardButton("⚒️ CUSTOM SPOILER & BESI", callback_data="custom_menu"),
        InlineKeyboardButton("💼 Admin", url=ADMIN_LINK),
        InlineKeyboardButton("📹 VIDEO ACC", url=CHANNEL_ACC_CPM),
        InlineKeyboardButton("🔑 API KEY (PM Admin)", url=ADMIN_LINK)
    )
    return kb

# ================= START COMMAND =================
@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, "🏠 *Menu Utama ANW STORE*", reply_markup=main_menu())

# ================= CODE KERETA MENU =================
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

# ================= CUSTOM SPOILER & BESI =================
@bot.callback_query_handler(func=lambda c: c.data == "custom_menu")
def custom_menu_handler(call):
    text = (
        "🛠️ *CODE CUSTOM SPOILER DAN BESI DALAM*\n\n"
        "🔩 *!! C O D E BESI DLM !!*\n"
        "4 - Besi ampaian/Bmw x6\n"
        "5 - Bar depan\n"
        "6 - roofbox/skybox\n"
        "10 - Lampu roof\n"
        "12 - besi rack lata\n"
        "13 - host lata\n"
        "14 - roof RR\n"
        "15 - besi blakang ford rangers\n"
        "20 - besi rack hakosuka\n"
        "32 - tire blakang jeep\n"
        "33 - besi atas jeep\n"
        "34 - besi blakang jeep\n"
        "39 - besi dalam dodge\n"
        "45 - besi atas hammer\n"
        "46/47 - besi blakang hilux\n"
        "48 - besi atas hilux\n"
        "50/52 - besi bar atas hilux\n"
        "56 - sportlight jeep\n"
        "59/60 - rack ford rangers\n"
        "61/62 - besi blakang hilux\n"
        "63 - besi blakang hilux papan\n"
        "69 - besi rack atas myvi\n"
        "75 - besi chavrolet\n\n"
        "📍 *CODE SPOILER PILIHAN*\n"
        "16 - spoiler merc Amg\n"
        "19 - spoiler r35\n"
        "41 - spoiler 350z\n"
        "49 - spoiler brz\n"
        "65 - spoiler rx7\n"
        "69 - spoiler nsx\n"
        "77 - spoiler rx8\n"
        "93 - spoiler Itik\n"
        "95 - spoiler ducktail infinity\n"
        "96 - spoiler wing infinity\n"
        "106 - spoiler wing ek9\n"
        "135 - spoiler audi r8v8\n"
        "148 - spoiler ferrari\n"
        "155 - spoiler wing bmw\n"
        "168 - spoiler Evo\n"
        "170 - spoiler Lambo"
    )
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("⬅ Kembali", callback_data="back_menu"))
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=kb)

# ================= BACK MENU =================
@bot.callback_query_handler(func=lambda c: c.data == "back_menu")
def back_menu_handler(call):
    bot.edit_message_text("🏠 *Menu Utama*", call.message.chat.id, call.message.message_id, reply_markup=main_menu())

# ================= GROUP BUTTON =================
def bottom_buttons():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("📞 ADMIN", url=ADMIN_LINK),
        InlineKeyboardButton("🛠 LINK TOOL", url=TOOL_LINK),
        InlineKeyboardButton("📹 VIDEO ACC CPM", url=CHANNEL_ACC_CPM)
    )
    return kb

WELCOME_TEXT = """
━━━━━━━━━━━━━━━━━━━━
👋 *SELAMAT DATANG KE GROUP*
➜ COIN
➜ MONEY
➜ ACHIEVEMENT
➜ MENU REMOVE BUMPER
➜ MENU CROAM VELG & BODY
➜ MENU PRANK
➜ MENU RACE BALAP
➜ MENU RACE LIARAN
➜ MENU UNLOCK
➜ COSTUM ROOF
➜ COSTUM ENGINE
➜ COSTUM CEMBER & UFO
━━━━━━━━━━━━━━━━━━━━
*PERHATIAN*
━━━━━━━━━━━━━━━━━━━━
➜ YANG NAK *BELI ACC*
TENGOK LINK DIBAWAH.
➜ TOOLS CPM WEBSITE:-
https://anwstore.my.id
➜ LIST CODE KERETA DAN CODE
  SPOILER - BESI DALAM:-
@AyobcicakBot
"""

# ================= WELCOME JOIN =================
@bot.message_handler(content_types=['new_chat_members'])
def welcome_member(msg):
    bot.send_message(msg.chat.id, WELCOME_TEXT, reply_markup=bottom_buttons())

# ================= RUN =================
if __name__ == "__main__":
    print("\033[1;31m🤖 Bot berjalan (AnwBotGroup)....\033[0m")
    # Jalankan Flask dalam thread supaya tak kacau polling bot
    threading.Thread(target=run).start()
    # Jalankan bot
    bot.infinity_polling()
