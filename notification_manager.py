from data_manager import DataManager
import telegram
import os
import smtplib


EMAIL = os.environ.get("Email")
PASSWORD = os.environ.get("Password")


# Telegram Bot API Token
TELEGRAM_TOKEN = '6019029128:AAHAaLekpeluUeYHm6nH0Uu4a2TqIG-_qCk'

# Channel ID (including the @ symbol)
CHANNEL_ID = '@flightclubdeals'

# This class is responsible for sending notifications with the deal flight details.

class NotificationManager:

    async def send_message_to_channel(self, mes):
        bot = telegram.Bot(token=TELEGRAM_TOKEN)
        await bot.send_message(chat_id=CHANNEL_ID, text=mes)

    # telegram bot will not be able to send more than 20 messages per minute to the same group hence I have kept

    # Send an Email to person's email address mentioned in Users worksheet.
    def send_email(self, email_message):
        data_manager = DataManager()
        users_data = data_manager.users_worksheet.get_all_records()

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            for email in users_data:
                connection.sendmail(from_addr=EMAIL,
                                    to_addrs=email["Email"],
                                    msg=f"Subject:New Low Price Flight!\n\n{email_message}".encode('utf-8')
                                    )
                print("Email Sent")



