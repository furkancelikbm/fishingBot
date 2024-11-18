from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import mss
import os
import pyautogui
import cv2
import numpy as np

# Telegram API token
TOKEN = "7709512017:AAEsEEPDq-DqqXSIiaEoZhV5wOAkIyUpi4g"

captcha_area = {"left": 600, "top": 230, "width": 700, "height": 645}

# Koordinatlar
koordinatlar = {
    'option1': (747, 407),
    'option2': (837, 392),
    'option3': (972, 394),
    'option4': (750, 514),
    'option5': (875, 517),
    'option6': (750, 664),
    'option7': (766,646),
    'option8': (870,630),
    'option9': (990,658)
}

async def tikla(secim):
    # Seçime göre koordinatları al
    x, y = koordinatlar[secim]
    
    # Mouse'u belirtilen koordinata hareket ettir ve tıkla
    pyautogui.click(x, y)

    # Kullanıcıya bilgi ver
    print(f"{secim} seçildi. Koordinat: ({x}, {y}) tıklandı.")  # Konsola bilgi yazdır

async def tikla_next():
    # Ekran görüntüsü alma
    with mss.mss() as sct:
        screenshot = sct.grab(captcha_area)
        screenshot_np = np.array(screenshot)

    # Ekran görüntüsünü kaydet
    cv2.imwrite("captcha_area.png", cv2.cvtColor(screenshot_np, cv2.COLOR_BGRA2BGR))

    # "next.png" resmi ile eşleştirme
    next_image = cv2.imread("next.png")
    captcha_image = cv2.imread("captcha_area.png")

    # Resmin bulunması
    result = cv2.matchTemplate(captcha_image, next_image, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8  # Eşleşme eşiği
    loc = np.where(result >= threshold)

    # Eşleşme varsa tıklama yap
    for pt in zip(*loc[::-1]):  # Koordinatları al
        click_x = pt[0] + captcha_area["left"] + (next_image.shape[1] // 2)  # Resmin ortasına tıklamak için
        click_y = pt[1] + captcha_area["top"] + (next_image.shape[0] // 2)
        pyautogui.click(click_x, click_y)
        print(f"'next.png' tıklandı. Koordinat: ({click_x}, {click_y})")
        break  # İlk eşleşmede tıklama yap ve döngüden çık

    # Geçici dosyaları sil
    os.remove("captcha_area.png")

async def tikla_new():
    # Ekran görüntüsü alma
    with mss.mss() as sct:
        screenshot = sct.grab(captcha_area)
        screenshot_np = np.array(screenshot)

    # Ekran görüntüsünü kaydet
    cv2.imwrite("captcha_area.png", cv2.cvtColor(screenshot_np, cv2.COLOR_BGRA2BGR))

    # "new.png" resmi ile eşleştirme
    new_image = cv2.imread("new.png")
    captcha_image = cv2.imread("captcha_area.png")

    # Resmin bulunması
    result = cv2.matchTemplate(captcha_image, new_image, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8  # Eşleşme eşiği
    loc = np.where(result >= threshold)

    # Eşleşme varsa tıklama yap
    for pt in zip(*loc[::-1]):  # Koordinatları al
        click_x = pt[0] + captcha_area["left"] + (new_image.shape[1] // 2)  # Resmin ortasına tıklamak için
        click_y = pt[1] + captcha_area["top"] + (new_image.shape[0] // 2)
        pyautogui.click(click_x, click_y)
        print(f"'new.png' tıklandı. Koordinat: ({click_x}, {click_y})")
        break  # İlk eşleşmede tıklama yap ve döngüden çık

    # Geçici dosyaları sil
    os.remove("captcha_area.png")

async def tikla_verify():
    # Ekran görüntüsü alma
    with mss.mss() as sct:
        screenshot = sct.grab(captcha_area)
        screenshot_np = np.array(screenshot)

    # Ekran görüntüsünü kaydet
    cv2.imwrite("captcha_area.png", cv2.cvtColor(screenshot_np, cv2.COLOR_BGRA2BGR))

    # "verify.png" resmi ile eşleştirme
    verify_image = cv2.imread("verify.png")
    captcha_image = cv2.imread("captcha_area.png")

    # Resmin bulunması
    result = cv2.matchTemplate(captcha_image, verify_image, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8  # Eşleşme eşiği
    loc = np.where(result >= threshold)

    # Eşleşme varsa tıklama yap
    for pt in zip(*loc[::-1]):  # Koordinatları al
        click_x = pt[0] + captcha_area["left"] + (verify_image.shape[1] // 2)  # Resmin ortasına tıklamak için
        click_y = pt[1] + captcha_area["top"] + (verify_image.shape[0] // 2)
        pyautogui.click(click_x, click_y)
        print(f"'verify.png' tıklandı. Koordinat: ({click_x}, {click_y})")
        break  # İlk eşleşmede tıklama yap ve döngüden çık

    # Geçici dosyaları sil
    os.remove("captcha_area.png")


# Komut işlevleri
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def fotocek(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Ekran görüntüsü alma
    with mss.mss() as sct:
        screenshot = sct.shot(output='screenshot.png')  # 'screenshot.png' olarak kaydeder

    # Ekran görüntüsünü gönderme
    with open('screenshot.png', 'rb') as file:
        await update.message.reply_photo(photo=file)

    # Geçici dosyayı sil
    os.remove('screenshot.png')

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
    [InlineKeyboardButton("1", callback_data='option1'),
     InlineKeyboardButton("2", callback_data='option2'),
     InlineKeyboardButton("3", callback_data='option3')],
     [InlineKeyboardButton("4", callback_data='option4'),
    InlineKeyboardButton("5", callback_data='option5'),
     InlineKeyboardButton("6", callback_data='option6')],
     [InlineKeyboardButton("7", callback_data='option7'),
     InlineKeyboardButton("8", callback_data='option8'),
    InlineKeyboardButton("9", callback_data='option9')],
     [InlineKeyboardButton("Next", callback_data='optionNext'),
     InlineKeyboardButton("Verify", callback_data='optionVerify'),
     InlineKeyboardButton("New", callback_data='optionNew')]
]


    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Lütfen bir seçenek belirleyin:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    if query.data == 'optionNext':
        await tikla_next()
    elif query.data == 'optionVerify':
        await tikla_verify()
    elif query.data == 'optionNew':
        await tikla_new()
    else:
        await tikla(query.data)

    # Seçenekler tıklandıktan sonra aynı menüyü tekrar göster
    keyboard = [
        [InlineKeyboardButton("1", callback_data='option1'),
         InlineKeyboardButton("2", callback_data='option2'),
         InlineKeyboardButton("3", callback_data='option3')],
        [InlineKeyboardButton("4", callback_data='option4'),
         InlineKeyboardButton("5", callback_data='option5'),
         InlineKeyboardButton("6", callback_data='option6')],
        [InlineKeyboardButton("7", callback_data='option7'),
         InlineKeyboardButton("8", callback_data='option8'),
         InlineKeyboardButton("9", callback_data='option9')],
        [InlineKeyboardButton("Next", callback_data='optionNext'),
         InlineKeyboardButton("Verify", callback_data='optionVerify'),
         InlineKeyboardButton("New", callback_data='optionNew')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_reply_markup(reply_markup=reply_markup)

# Telegram botunu başlatma
app = ApplicationBuilder().token(TOKEN).build()

# Komut işleyicileri ekleme
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("fotocek", fotocek))
app.add_handler(CommandHandler("menu", menu))  # Menü komutu ekleniyor
app.add_handler(CallbackQueryHandler(button))  # Buton komut işleyicisi ekleniyor

# Telegram botunu çalıştırma
app.run_polling()
