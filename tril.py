import telebot
import requests
from telegram import Bot

# Create a new instance of the TeleBot class
bot = telebot.TeleBot('5983174648:AAEbMKWsCeAOF0IK2Cs_nUDWPPPLm1zlbEs')

@bot.message_handler(commands=['download'])
def handle_download(message):
    """
    Handler function for the '/download' command.

    This function is triggered when the user sends the '/download' command to the Telegram bot.

    Parameters:
    - message: telebot.types.Message
        The message object that contains the details of the user's command.

    Returns:
    - None

    Side Effects:
    - Downloads the file specified by the user and sends it back to the user.

    """

    # Get the file URL from the user's command
    file_url = message.text.split(' ')[1]

    try:
        # Download the file from the specified URL
        response = requests.get(file_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Send the file back to the user
            bot.send_document(message.chat.id, response.content)
        else:
            # Send an error message if the request was not successful
            bot.send_message(message.chat.id, "Error: Unable to download the file.")
    except Exception as e:
        # Send an error message if an exception occurred during the download process
        bot.send_message(message.chat.id, f"Error: {str(e)}")

# Start the bot
bot.polling()
print("Bot started.")