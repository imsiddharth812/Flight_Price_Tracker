KIWI_ENDPOINT = "https://api.tequila.kiwi.com/v2/search?"
KIWI_API_KEY = "YOU KIWI API KEY"


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, departure_date, arrival_date,stop_over=0, via_city=""):
        self.price = price
        self.origin_airport = origin_airport
        self.origin_city = origin_city
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.stop_over = stop_over
        self.via_city = via_city
        # self.booking_token = booking_token

