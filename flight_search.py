import requests

from flight_data import FlightData
KIWI_API_KEY = "YOUR KIWI API KEY"
KIWI_ENDPOINT = "https://api.tequila.kiwi.com/v2/search?"



class FlightSearch:


    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        if not destination_city_code:
            print(f"No destination city IATA Code provided.")
            return None

        kiwi_headers = {
            "apikey": KIWI_API_KEY,
        }
        flight_params = {
                "fly_from": origin_city_code,
                "fly_to": destination_city_code,
                "date_from": from_time,
                "date_to": to_time,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "max_stopovers": 0,
                "curr": "INR",
                "one_for_city": 1

        }

        response = requests.get(KIWI_ENDPOINT, params=flight_params, headers=kiwi_headers)

        try:
            data = response.json()["data"][0]
            # pp(data)
        except IndexError:
                flight_params["max_stopovers"] = 2
                response = requests.get(KIWI_ENDPOINT, params=flight_params, headers=kiwi_headers)
                try:
                    data = response.json()["data"][0]
                except IndexError:
                    print(f"No flights found for {destination_city_code}")
                    return None
                else:
                    flight_data = FlightData(
                        price=data["price"],
                        origin_city=data["route"][0]["cityFrom"],
                        origin_airport=data["route"][0]["flyFrom"],
                        destination_city=data["route"][1]["cityTo"],
                        destination_airport=data["route"][1]["flyTo"],
                        departure_date=data["route"][0]["local_departure"].split("T")[0],
                        arrival_date=data["route"][2]["local_departure"].split("T")[0],
                        stop_over = flight_params["max_stopovers"],
                        via_city= data["route"][0]["cityTo"],
                        )
                    print(f"{flight_data.destination_city}: ₹ {flight_data.price}")

                    return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                departure_date=data["route"][0]["local_departure"].split("T")[0],
                arrival_date=data["route"][1]["local_departure"].split("T")[0],
                )


            print(f"{flight_data.destination_city}: ₹ {flight_data.price}")

            return flight_data




