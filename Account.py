from FileManager import FileManager
from HistoryMessages import HistoryMessages

class Account:
    def __init__(self, balance = 0):
        self.balance = balance
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"
        

    def write_to_history(self, hist_dict):
        self.file_manager.add_to_json(hist_dict, self.hist_file_path)

    def deposit(self, amount):
        try:
            amount = int(amount)
            if amount > 0:
                self.balance += amount
                history_message = HistoryMessages.deposit("success", amount, self.balance)
            else:
                print("Invalid amount for deposit!")
                history_message = HistoryMessages.deposit("failure", amount, self.balance)

        except ValueError:
            print("Invalid amount for deposit!" )
            return

        self.write_to_history(history_message)


    def debit(self, amount):
        try:
            amount = int(amount)
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                history_message = HistoryMessages.debit("success", amount, self.balance)
            else:
                history_message = HistoryMessages.debit("failure", amount, self.balance)
                print("Invalid amount for debit!")
        except ValueError:
            print("Invalid amount for debit!")
            return

        self.write_to_history(history_message)


    def get_balance(self):
        return self.balance

    def dict_to_string(self, dict):
        if dict["operation_type"] != "exchange":
            return f"type: {dict["operation_type"]} status: {dict["status"]} amount: {dict["amount_of_deposit"]} balance: {dict["total_balance"]}"
        else:
            return f"type: {dict["operation_type"]} status: {dict["status"]} pre exchange amount: {dict["pre_exchange_amount"]} exchange amount: {dict["exchange_amount"]} currency from: {dict["currency_from"]} currency to: {dict["currency_to"]}"
        

    def get_history(self):
        history = self.file_manager.read_json(self.hist_file_path)
        history_str = ""
        for entry in history:
            history_str += self.dict_to_string(entry) + "\n"
        return history_str