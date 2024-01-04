from models.user import User

class BotController:
    def __init__(self):
        self.users = []

    def add_user(self, name, chat_id):
        user = User(name, chat_id)
        self.users.append(user)
        return user

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
