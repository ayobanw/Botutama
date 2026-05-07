from flask import Flask
import threading

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

# Jalan dalam thread supaya tak kacau bot Telegram
threading.Thread(target=run).start()


import telebot
#from telebot import apihelper

# Letak ni sebelum baris bot = telebot.TeleBot(TOKEN)
#apihelper.proxy = {'https': 'http://proxy.server:3128'}

# ================= CONFIG =================
TOKEN = "8300282726:AAEeRUjkb0yDWMfUgwFs-hHrY5AP_Hu16T0"
GROUP_USERNAME = "@GroupBotAnw"
GROUP_ID = -1003526954874

ADMIN_LINK = "https://t.me/ayobanw"
TOOL_LINK = "https://anwstore.my.id"
CHANNEL_ACC_CPM = "https://t.me/+3xl0prkLlfI2ODll"

bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")

# ================= JOIN BUTTON =================
def join_keyboard():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("📢 Join Group AnwBot", url="https://t.me/GroupBotAnw"),
        InlineKeyboardButton("✅ I've Joined", callback_data="check_join")
    )
    return kb

# ================= MAIN MENU =================
def main_menu():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("🛠 Tool", url=TOOL_LINK),
        InlineKeyboardButton("💎 CODE KERETA", callback_data="harga_menu"),
        InlineKeyboardButton("🛠️ CUSTOM SPOILER & BESI", callback_data="custom_menu"),
        InlineKeyboardButton("�‍💼 Admin", url=ADMIN_LINK),
        InlineKeyboardButton("📹 VIDEO ACC", url=CHANNEL_ACC_CPM),
        InlineKeyboardButton("🔑 API KEY (PM Admin)", url=ADMIN_LINK)
    )
    return kb

# ================= START =================
@bot.message_handler(commands=['start'])
def start(msg):
    photo = open("anwbot.jpg", "rb")

    bot.send_photo(
        msg.chat.id,
        photo,
        caption="📢 *Join Group Required*\n\n"
                "Untuk guna bot ini, sila join group rasmi kami dahulu.\n\n"
                "Selepas join, tekan *Ive Joined* 👇\n\n"
                "Untuk tengok menu",
        reply_markup=join_keyboard()
    )

# ================= CHECK JOIN =================
@bot.callback_query_handler(func=lambda c: c.data == "check_join")
def check_join(call):
    try:
        member = bot.get_chat_member(GROUP_USERNAME, call.from_user.id)
        if member.status != 'left':
            bot.answer_callback_query(call.id, "✅ Verified!")
            bot.send_message(
                call.message.chat.id,
                "🎉 *Verified!*\n\nSila pilih menu di bawah 👇",
                reply_markup=main_menu()
            )
        else:
            bot.answer_callback_query(call.id, "❌ Sila join group dulu.", show_alert=True)
    except:
        bot.answer_callback_query(call.id, "❌ Sila join group dulu.", show_alert=True)

# ================= HARGA =================
@bot.callback_query_handler(func=lambda c: c.data == "harga_menu")
def harga_menu(call):
    text = (
        "🚗 *CODE KERETA CPM1 V4.9.8* 🚗\n\n"
        "1 BMW 135I\n"
        "2 VW Scirocco\n"
        "3 BMW M5 2015\n"
        "4 OLD G-Wagon\n"
        "5 Chevy Camaro\n"
        "6 Subaru BRZ\n"
        "7 Lexus LFA\n"
        "8 Infiniti G36\n"
        "9 Subie Stinkeye\n"
        "10 Ferrari F12\n"
        "11 R34 Skyline\n"
        "12 Evo 10\n"
        "13 EK9\n"
        "14 GTR R35\n"
        "15 Audi RS4\n"
        "17 Merc C63\n"
        "18 Lambo Huracan\n"
        "19 Merc AMG GTR\n"
        "20 Audi TT\n"
        "21 Jeep Wrangler\n"
        "22 BMW M6\n"
        "23 Hyundai Veloster\n"
        "24 Porsche Panamera\n"
        "25 Bugatti Veyron\n"
        "28 Porsche Cayenne\n"
        "29 Honda FN2\n"
        "30 BMW M5 99's\n"
        "31 BMW M5 05's\n"
        "32 Koenigsegg Agera\n"
        "35 Mustang Shelby GT500\n"
        "37 Ford Transit\n"
        "39 Dodge Charger 70's\n"
        "40 Corvette C7\n"
        "41 McLaren P1\n"
        "42 Aventador\n"
        "43 Lexus IS300\n"
        "44 Lambo Veneno\n"
        "45 BMW M5 97's\n"
        "47 S2000\n"
        "48 RX8\n"
        "49 Supra MK4\n"
        "51 Old Ferrari\n"
        "53 Hakosuka GTR\n"
        "54 BMW M5 80's\n"
        "55 Hummer H1\n"
        "56 BMW M3 E93\n"
        "57 Cadillac CTS-V\n"
        "58 Ferrari 458\n"
        "59 Smart Fortwo\n"
        "60 Escalade\n"
        "61 Mercedes E Series\n"
        "62 Dodge Charger\n"
        "65 Gallardo\n"
        "66 Chrysler 300C\n"
        "70 Scania Truck\n"
        "74 Peugeot 308\n"
        "76 BMW Z4\n"
        "77 Mini Cooper\n"
        "81 Subaru Hawkeye\n"
        "82 Evo 8\n"
        "85 Ford Ranger\n"
        "86 BMW X5\n"
        "87 Mercedes C Series\n"
        "88 Iconic BMW M3\n"
        "89 Hudson Hornet\n"
        "99 LADA\n"
        "100 Russian Car\n"
        "101 Ford Trailer\n"
        "102 Russian Car\n"
        "103 BMW M4 F82\n"
        "104 BMW M5 F90\n"
        "105 Dodge Challenger\n"
        "106 Old Mercedes E Series\n"
        "107 Audi R8 V10 Old\n"
        "108 Audi Quattro\n"
        "109 Porsche 911 991\n"
        "110 Range Rover SVR\n"
        "111 New NSX\n"
        "112 Mercedes E/C Class\n"
        "113 Golf R MK7\n"
        "114 Mercedes E/S Class\n"
        "115 Audi R8 V10 Plus New\n"
        "116 Mustang 5.0\n"
        "117 Audi S7\n"
        "118 BMW X6\n"
        "119 Hummer Military\n"
        "120 Toyota Camry\n"
        "121 Toyota LC200\n"
        "123 Mercedes GLE\n"
        "124 Rolls Royce Wraith\n"
        "125 Lambo Urus\n"
        "126 GMC Sierra\n"
        "127 BMW M2\n"
        "128 Nissan S15\n"
        "129 RX7\n"
        "130 Ford GT\n"
        "131 Nissan 240SX\n"
        "132 Russian Car\n"
        "133 Myvi Perodua M600\n"
        "134 Toyota Chaser\n"
        "135 Audi RS6\n"
        "136 Mercedes Class\n"
        "137 Honda FD2\n"
        "138 BMW i8\n"
        "139 Crown Victoria\n"
        "140 Toyota AE86\n"
        "141 Dodge Viper\n"
        "142 Mercedes C63\n"
        "143 Mercedes G63 New\n"
        "145 Nissan 350Z\n"
        "146 Russian Car\n"
        "147 Honda FK8\n"
        "148 Fastback Mustang\n"
        "149 Oldies Car\n"
        "150 Supra MK5\n"
        "151 Toyota Velfire\n"
        "152 Russian Car\n"
        "153 BMW M4 G82\n"
        "154 Toyota Hilux\n"
        "155 Old F1\n"
        "156 R32 GTR\n"
        "157 Golf R MK5/4\n"
        "158 Mazda MX5\n"
        "159 Lambo SVJ\n"
        "160 Old Dodge Challenger\n"
        "161 Jeep Cherokee\n"
        "162 McLaren 720S\n"
        "163 Mercedes Convertible\n"
        "164 Dune Buggy\n"
        "165 New F1\n"
        "166 Corvette C8\n"
        "167 Dodge Ram\n"
        "168 Bentley Continental\n"
        "169 Ford Explorer\n"
        "170 Peterbilt Truck\n"
        "171 Scania Truck\n"
        "172 Rolls Royce Cullinan\n"
        "173 Mercedes Class\n"
        "175 Mercedes Class\n"
        "176 Chevy Pickup\n"
        "177 Nissan S13\n"
        "178 Bugatti Chiron SS\n"
        "179 Chevy\n"
        "180 Chevy Pickup\n"
        "181 Old Mustang\n"
        "182 Drift Truck Hoonicorn\n"
        "183 Drift Mustang\n"
        "184 Mitsubishi Eclipse\n"
        "185 Chevy Impala\n"
        "186 Astro Van\n"
        "187 Mazda Miata\n"
        "188 Porsche GT3RS\n"
        "189 Ford Raptor\n"
        "190 Peugeot\n"
        "191 Bus 1\n"
        "192 Ram TRX\n"
        "193 M3 Touring\n"
        "194 Mercedes SLR\n"
        "195 Bus 2\n"
        "196 Old Dodge Charger\n"
        "197 VW Microbus\n"
        "198 Koenigsegg Jesko\n"
        "199 Corvette C6\n"
        "200 Dodge Durango\n"
        "201 Mercedes CLK GTR\n"
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
        "259 FORTUNER NEW\n"
    )
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("⬅ Kembali", callback_data="back_menu"))

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=kb
    )

# ================= CUSTOM SPOILER & BESI =================
@bot.callback_query_handler(func=lambda c: c.data == "custom_menu")
def custom_menu(call):
    text = (
        "🛠️ *CODE CUSTOM SPOILER DAN BESI DALAM*\n\n"

        "🔩 *!! C O D E  BESI DLM !!*\n"
        "4  - Besi ampaian/Bmw x6\n"
        "5  - Bar depan\n"
        "6  - roofbox/skybox\n"
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
        "16  - spoiler merc Amg\n"
        "19  - spoiler r35\n"
        "41  - spoiler 350z\n"
        "49  - spoiler brz\n"
        "65  - spoiler rx7\n"
        "69  - spoiler nsx\n"
        "77  - spoiler rx8\n"
        "93  - spoiler Itik\n"
        "95  - spoiler ducktail infinity\n"
        "96  - spoiler wing infinity\n"
        "106 - spoiler wing ek9\n"
        "135 - spoiler audi r8v8\n"
        "148 - spoiler ferrari\n"
        "155 - spoiler wing bmw\n"
        "168 - spoiler Evo\n"
        "170 - spoiler Lambo\n"
    )

    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("⬅ Kembali", callback_data="back_menu"))

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=kb
    )

# ================= BACK MENU =================
@bot.callback_query_handler(func=lambda c: c.data == "back_menu")
def back_menu(call):
    bot.edit_message_text(
        "🏠 *Menu Utama*",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=main_menu()
    )

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
def welcome(msg):
    bot.send_message(msg.chat.id, WELCOME_TEXT, reply_markup=bottom_buttons())

# ================= RUN =================
print("\033[1;31m🤖 Bot berjalan (AnwBotGroup)....\033[0m")
bot.infinity_polling()
