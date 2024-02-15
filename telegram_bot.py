from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import qr_code_generator

TOKEN = 'YOUR TOKEN HERE'


def send_img(update, context):
    message = update.message.text

    path = qr_code_generator.generateQRCode("exam", message)
    context.bot.send_document(chat_id=update.effective_chat.id, document=open(path, 'rb'))


def start(update, context):
    user_name = update.message.from_user.first_name
    welcome_message = f"Welcome, {user_name}! This bot is a QR code generator. "
    welcome_message += "Just send a link, and it will create a QR code for you."
    context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, send_img))

    updater.start_polling()
    updater.idle()
