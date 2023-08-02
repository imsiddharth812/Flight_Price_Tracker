# Flight_Price_Tracker
This project is a flight price alert system that uses various classes and modules to retrieve flight data, search for flights, and send notifications on Telegram Channel & Email Addresses.

To get a Telegram bot token and a channel ID, you'll need to follow these steps:

# Step 1: Create a Telegram Bot

Open the Telegram app and search for the "BotFather" bot.
Start a chat with the BotFather by clicking on the "Start" button or sending a message like "/start".
Use the "/newbot" command to create a new bot. Follow the instructions provided by the BotFather to set a name and username for your bot.
Once the bot is created, the BotFather will provide you with a unique bot token. Keep this token safe, as it will be used to authenticate your bot and send messages.

# Step 2: Create a Telegram Channel

Open the Telegram app and click on the hamburger menu (three horizontal lines) in the top left corner.
Click on "New Channel" to create a new channel.
Choose a name for your channel and set the privacy settings as per your preference (public or private).
Once the channel is created, click on the channel name to view the channel details.
The channel ID will be visible in the URL of your channel. It will look something like this: t.me/joinchat/ABC123XYZ456. The last part of the URL (ABC123XYZ456) is your channel ID.

Important Notes:

Make sure to add your bot as an administrator to the channel to allow it to send messages.
If your channel is private, you'll need to invite the bot to the channel manually.
With the bot token and channel ID in hand, you can now use the Python code provided earlier to send messages to your Telegram channel using the python-telegram-bot library.


