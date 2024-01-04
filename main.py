from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from controllers.bot_controller import BotController
from kivy.uix.screenmanager import Screen
from views.bot_view import BotView

# Загружаем пользовательский интерфейс из файла .kv
Builder.load_file('views/main_screen.kv')

class MainScreen(Screen):
    view = BotView()

    def on_pre_enter(self):
        self.update_users_list()

    def update_users_list(self):
        self.view.update_users_list()


class MyApp(App):
    def build(self):
        # Создаем экземпляр контроллера
        controller = BotController()

        # Создаем экземпляр главного экрана и передаем контроллер в виджеты
        main_screen = MainScreen()
        main_screen.controller = controller

        # Создаем экземпляр ScreenManager и добавляем главный экран
        screen_manager = ScreenManager()
        screen_manager.add_widget(main_screen)

        return screen_manager

if __name__ == '__main__':
    MyApp().run()
