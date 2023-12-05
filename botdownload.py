import logging
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler, ContextTypes

BOT_TOKEN = '6395223990:AAGebZHpIqT3GWFR3BtytuPLFKvTkYAAezA'

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def downloader(update, context):
    # Download file
    fileName = update.message.document.file_name
    new_file = await update.message.effective_attachment.get_file()
    await new_file.download_to_drive(fileName)

    # Acknowledge file received
    await update.message.reply_text(f"{fileName} saved successfully")

    # Send the file
    chat_id = update.message.chat.id
    file_id = '20221222-.pptx'
    await context.bot.send_document(chat_id=chat_id, document=file_id)
    
    
    
    
    -2

def start_function(update, context):
    update.message.reply_text("Hello there! I'm AskPython Bot.")
 
 
def help_function(update, context):
    update.message.reply_text(
        """
    Available commands:
 
    /start : Starts up the bot
    /help : Help topics
    /about : About text
    /askpython : Go to AskPython Offical Website
    /custom : Other custom commands 
 
    """
    )
 
 
def about_function(update, context):
    update.message.reply_text("I am a bot and also a Python Genie.")
 
 
def ask_python_function(update, context):
    update.message.reply_text("AskPython Website: https://www.askpython.com/")
    return
 
 
def custom_function(update, context):
    update.message.reply_text("This is a custom command.")
    context.bot.send_message(chat_id=update.effective_chat.id, text="This is a custom command.")
    return
    
    
    
    

application = ApplicationBuilder().token(BOT_TOKEN).build()

# on different commands - answer in Telegram
application.add_handler(MessageHandler(filters.ALL, downloader))

# Run the bot until the user presses Ctrl-C
application.run_polling()