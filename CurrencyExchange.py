from FileManager import FileManager
from HistoryMessages import HistoryMessages
import requests

class CurrencyExchange:
    def __init__(self, balance = 0):
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"
        

    def write_to_history(self, hist_dict):
        self.file_manager.add_to_json(hist_dict, self.hist_file_path)

    def get_exchange_rates(self):
        try:
            exch_rates = request.get("https://fake-api.apps.berlintech.ai/api/currency_exchange").json()
            return exch_rates 
        except Exception as e:
            print(f"Request Error: {e}")
            return None
    
    def exchange_currency(self, currency_from, currency_to, amount):
        try:
            amount = float(amount)
        except ValueError:
            print("Currency exchange failed!")
            history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
            self.write_to_history(history_message)
            return None

        rates = self.get_exchange_rates()

        if rates and currency_from in rates and currency_to in rates:
            conversion_rate = rates[currency_to] / rates[currency_from]
            converted_amount = amount * conversion_rate
            history_message = HistoryMessages.exchange("success", amount, converted_amount, currency_from, currency_to)
            self.write_to_history(history_message)
            return converted_amount

        else:
            print("Currency exchange failed! Invalid currency codes or unable to fetch exchange rates.")
            history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
            self.write_to_history(history_message)
            return None