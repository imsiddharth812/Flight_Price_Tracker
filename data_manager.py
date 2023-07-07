import requests
import gspread  # Import the gspread module for accessing Google Sheets
from google.oauth2.service_account import Credentials  # Import Credentials from google.oauth2.service_account for authentication
from pprint import pprint as pp  # Import pprint from pprint module for pretty-printing



KIWI_API_KEY = "LOSX3FlKp4Nz6yRBdfUGPxH8Hg9-AqpT"
KIWI_LOCATION_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"

KIWI_HEADERS = {
    "apikey": KIWI_API_KEY,
}
SCOPES = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                  "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        # Define the necessary scopes for accessing Google Sheets and Drive

CREDS = Credentials.from_service_account_file("sheet_credentials.json", scopes=SCOPES)
# Create credentials by loading the service account file and specifying the desired scopes

CLIENT = gspread.authorize(CREDS)
# Authorize the client using the obtained credentials


class DataManager:  #This class is responsible for talking to the Google Sheet.
    def __init__(self):

        self.spreadsheet = CLIENT.open("Flight Deals")
        self.destination_worksheet = self.spreadsheet.get_worksheet(0)
        self.users_worksheet = self.spreadsheet.get_worksheet(1)
        self.destination_data = {}

        # Open the Google Sheets spreadsheet titled "Flight Deals" and select the first sheet

    def get_destination_data(self):
        self.destination_data = self.destination_worksheet.get_all_records()
        return self.destination_data
        # Retrieve all records (rows) from the selected sheet and store them in the destination_data variable


    """ Write iata code from kiwi API to sheet """
    def update_destination_iata_codes(self):
        for destination in self.get_destination_data():
            destination_city = destination["City"].title()
            if destination["IATA Code"] == "":
                locations = {
                    "location_types": "airport",
                    "term": destination_city,
                    "limit": 1,
                }

                response_iata = requests.get(KIWI_LOCATION_ENDPOINT, headers=KIWI_HEADERS, params=locations)
                try:
                    data = response_iata.json()["locations"][0]
                    # pp(data)  # Pretty-print the retrieved data
                    city_code = data["code"]
                    print(f"New IATA code {city_code} added.")

                    if city_code:
                        cell = self.destination_worksheet.find(destination_city)
                        self.destination_worksheet.update_cell(cell.row, cell.col + 1, city_code)
                except IndexError:
                    print(f"No IATA code found for {destination_city}")
                    # return None

    def users_data(self):
        users_data = self.users_worksheet.get_all_records()
        return users_data

    def update_user_data(self):
        users_list = []
        user_first_name = input("What is your first name?\n")
        users_list.append(user_first_name)
        user_last_name = input("What is your last name?\n")
        users_list.append(user_last_name)
        user_email = input("What is your email address?\n")
        users_list.append(user_email)
        user_confirm_email = input("Type your email again\n")
        if user_confirm_email != user_email:
            print("Email and Confirm Email addresses are different.")
        else:
            self.users_worksheet.append_row(users_list)



                    

