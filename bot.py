from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = "8588990746:AAFCt4JworJTze32h4ZqChBsGiOsVbPeTuQ"
CHANNEL_ID = "-1003531372779"

async def forward_to_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    if msg.text:
        await context.bot.send_message(chat_id=CHANNEL_ID, text=msg.text)
    elif msg.photo:
        await context.bot.send_photo(chat_id=CHANNEL_ID, photo=msg.photo[-1].file_id, caption=msg.caption)
    elif msg.video:
        await context.bot.send_video(chat_id=CHANNEL_ID, video=msg.video.file_id, caption=msg.caption)
    elif msg.sticker:
        await context.bot.send_sticker(chat_id=CHANNEL_ID, sticker=msg.sticker.file_id)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward_to_channel))
app.run_polling()
