''' Дизайн главного окна(работает только кнопка закрытия) '''
import arcade
import arcade.gui

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Top-Down Shooter"

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.DARK_TAN)

        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()

        start_button_style = {
            "normal": arcade.gui.UIFlatButton.UIStyle(
                font_size=20,
                font_name=("Impact", "Arial Black", "Arial"),
                font_color=arcade.color.BLACK,
                bg=arcade.color.DARK_RED,
                border=arcade.color.BROWN,
                border_width=4
            ),
            "hover": arcade.gui.UIFlatButton.UIStyle(
                font_size=20,
                font_name=("Impact", "Arial Black", "Arial"),
                font_color=arcade.color.BLACK,
                bg=arcade.color.RED_DEVIL,
                border=arcade.color.DARK_RED,
                border_width=4
            ),
            "press": arcade.gui.UIFlatButton.UIStyle(
                font_size=18,
                font_name=("Impact", "Arial Black", "Arial"),
                font_color=arcade.color.LIGHT_GRAY,
                bg=arcade.color.BLACK,
                border=arcade.color.DARK_RED,
                border_width=4
            )
        }

        button_style = {
            "normal": arcade.gui.UIFlatButton.UIStyle(
                font_size=16,
                font_name=("Courier New", "monospace"),
                font_color=arcade.color.LIGHT_GRAY,
                bg=arcade.color.BROWN,
                border=arcade.color.DARK_RED,
                border_width=2
            ),
            "hover": arcade.gui.UIFlatButton.UIStyle(
                font_size=17,
                font_name=("Courier New", "monospace"),
                font_color=arcade.color.BLACK,
                bg=arcade.color.DARK_RED,
                border=arcade.color.RED,
                border_width=2
            ),
            "press": arcade.gui.UIFlatButton.UIStyle(
                font_size=15,
                font_name=("Courier New", "monospace"),
                font_color=arcade.color.BLACK,
                bg=arcade.color.DARK_RED,
                border=arcade.color.BLACK,
                border_width=2
            )
        }

        start_button = arcade.gui.UIFlatButton(
            text="НАЧАТЬ ИГРУ",
            width=400,
            height=50,
            style=start_button_style
        )

        wins_button = arcade.gui.UIFlatButton(
            text="РЕКОРДЫ",
            width=195,
            height=50,
            style=button_style
        )

        settings_button = arcade.gui.UIFlatButton(
            text="НАСТРОЙКИ",
            width=195,
            height=50,
            style=button_style
        )

        exit_button = arcade.gui.UIFlatButton(
            text="ВЫХОД",
            width=100,
            height=50,
            style=button_style
        )

        start_button.on_click = self.start_game
        self.uimanager.add(start_button)
        wins_button.on_click = self.wins_view
        self.uimanager.add(wins_button)
        settings_button.on_click = self.settings_window
        self.uimanager.add(settings_button)
        exit_button.on_click = self.exit_action
        self.uimanager.add(exit_button)

        start_button.left = (self.width - start_button.width) // 2
        start_button.top = (self.height - start_button.height) // 2

        wins_button.left = (self.width // 2) - 200
        wins_button.top = (self.height // 2) - (start_button.height * 2)

        settings_button.left = (self.width // 2) + 5
        settings_button.top = (self.height // 2) - (start_button.height * 2)

        exit_button.left = self.width - 10 - exit_button.width
        exit_button.top = self.height - 10

    def start_game(self, event):
        pass

    def wins_view(self, event):
        pass

    def settings_window(self, event):
        pass

    def exit_action(self, event):
        arcade.close_window()

    def on_draw(self):
        self.clear()
        self.uimanager.draw()

def on_update(self, delta_time):
    pass


if __name__ == "__main__":
    app = GameWindow()
    arcade.run()
