from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from models.database import Database


class UserListItem(BoxLayout):
    def delete_user(self):
        database = Database()
        database.delete_user(self.user.id)
        self.parent.remove_widget(self)
        database.close()


class BotView(BoxLayout):
    users_list = BoxLayout()
    start_button = Button()

    def update_users_list(self):
        self.users_list.clear_widgets()
        database = Database()
        users = database.get_all_users()
        database.close()

        for user in users:
            user_item = UserListItem(user=user)
            self.users_list.add_widget(user_item)

    def display_error_message(self, message):
        error_label = Label(text=message)
        self.add_widget(error_label)
