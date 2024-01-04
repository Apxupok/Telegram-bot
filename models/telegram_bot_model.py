from models.user import User
from models.statistics import Statistics
from models.database import Database

class TelegramBotModel:
    def __init__(self):
        self.stats = Statistics()
        self.database = Database()

    def start(self):
        pass

    def authorize_user(self, user):
        pass

    def create_random_selection(self):
        pass

    def get_statistics(self):
        pass

    def delete_user(self, user_id):
        pass

    def update_view(self):
        pass
