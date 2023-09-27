import random


from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, ConversationHandler
TOKEN = "6489496109:AAElLoYXaj9W96iouUYhp9nC0xEwMMCOVKo"


famous_people = {
    "Abdulla Qodiriy": "Abdulla Qodiriy (asosiy taxalluslari: Qodiriy, Julqunboy) (1894.4.10-Toshkent-1938.10.4)  XX a. yangi ozbek adabiyotining ulkan namoyandasi, ozbek romanchiligining asoschisi; 20-yillardagi muhim ijtimoiy-madaniy jarayonlarning faol ishtirokchisi. Bogbon oilasida tugilgan. Otasi Qodirbobo (1820—1924) xon, beklar qolida sarbozlik qilgan, rus bosqini paytida (1865) Toshkent mudofaasida qatnashgan. Otasi boshidan otgan sarguzashtlar Abdulla Qodiriyning qator asarlari, xususan tarixiy romanlarining yuzaga kelishida muhim rol oynagan. Abdulla Qodiriy musulmon maktabida (1904.06), rus-tuzem maktabida (1908.12), Abulqosim shayx madrasasida (1916.17) talim oldi; Moskvadagi adabiyot kursida (1925.26) oqidi. Yoshligidanoq qadimgi Sharq madaniyati va adabiyoti ruhida tarbiya topgan; arab, fors va rus tillarini organgan. Jahon adabiyotini ixlos bilan mutolaa qilgan.",
    "Amur Temur": "Amir Temur, Temur, Temurbek (toliq ismi Amir Temur ibn Amir Taragay ibn Amir Barqul) (1336-yil, 9-aprel — 1405-yil, 18-fevral) — orta asrning yirik davlat arbobi, buyuk turkiy sarkardasi, kuchli, markazlashgan davlat asoschisi, ilm-fan va madaniyat homiysi.",
    "Mirzo Ulug'bek": "Mirzo (keyinchalik Sulton) Muhammad ibn Shohrux ibn Temur Ulugbek Koragon — Temuriylar davlatining hukmdori, buyuk ozbek astronomi (yulduzshunos) va matematigi. U otasi Shohrux Mirzo davrida Mavarounnahr hokimi va otasi vafot etgach butun Temuriylar imperiyasi sultoni(1447—1449) boldi. Ulugbek  trigonometriya va sferik geometriya kabi astronomiya bilan bogliq matematika sohasidagi ishlari, shuningdek, sanat va intellektual faoliyatga umumiy qiziqishlari bilan ajralib turardi.   U besh tilda: turkiy, arab ,  fors ,  mogul va oz miqdorda  xitoy tillarini bilgan deb taxmin qilinadi .  Uning hukmronligi davrida (avval hokim, keyin togridan-togri) uning etibori va homiyligi tufayli  temuriylar uygonish davrining  madaniy choqqisiga erishdi . Samarqand hokimligi, otasi Shohrux Mirzo tomonidan Ulugbekga berilgan."
}
def start(update, context):
    keyboard = []
    for person_name in famous_people:
        keyboard.append([InlineKeyboardButton(person_name, callback_data=person_name)])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Xush Kelibsiz O'zbek Adiblariga.", reply_markup=reply_markup)

def button_click(update, context):
    query = update.callback_query
    person_name = query.data
    
    if person_name in famous_people:
        person_info = famous_people[person_name]
        query.message.reply_text(f"{person_name}: {person_info}")
    else:
        query.message.reply_text("Person not found.")

def main():
    updater = Updater(TOKEN)

    
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CallbackQueryHandler(button_click))
    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()