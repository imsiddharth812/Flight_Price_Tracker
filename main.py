#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import datetime
import asyncio
from notification_manager import NotificationManager
from flight_search import FlightSearch
from data_manager import DataManager

ORIGIN_CITY_IATA = "AMD"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

data_manager.update_destination_iata_codes()
destination_data = data_manager.get_destination_data()
tomorrow_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
till_six_month = (datetime.date.today() + datetime.timedelta(days=1) + datetime.timedelta(days=180)). \
            strftime("%d/%m/%Y")


for destination in destination_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["IATA Code"],
        tomorrow_date,
        till_six_month
    )

    if flight is None:
        continue

    if flight.price < destination["Lowest Price"]:
        message = f"Low Price Alert! Only INR {flight.price} to fly from {flight.origin_city}-" \
                  f"{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from " \
                  f"{flight.departure_date} to {flight.arrival_date}."
        if flight.stop_over > 0:
            message += f"\n Flight has {flight.stop_over} stop over, via {flight.via_city}"

        print("sending message to telegram")
        asyncio.run(notification_manager.send_message_to_channel(message))
        print("Sending Email")
        notification_manager.send_email(message)
