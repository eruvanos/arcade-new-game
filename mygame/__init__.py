import arcade
from arcade.future.splash import ArcadeSplash

from mygame import resources
from mygame.version import version


class MyGameView(arcade.View):
    def __init__(self):
        super().__init__()
        w, h = arcade.get_window().size

        self.sprites = arcade.SpriteList()
        logo = arcade.Sprite(
            resources.LOGO, center_x=w // 2, center_y=h // 3 * 2, scale=0.2
        )
        self.sprites.append(logo)

        self.text = arcade.Text(
            f"Hello, welcome to my game. Version {version}",
            w // 2,
            h // 2,
            font_size=24,
            anchor_x="center",
            anchor_y="center",
        )

    def on_draw(self):
        self.clear()
        self.text.draw()
        self.sprites.draw()


def main():
    """Setup arcade window , show SplashScreen and run the game"""
    window = arcade.Window(title="My Game")

    game_view = MyGameView()
    arcade_splash = ArcadeSplash(game_view, dark_mode=True, duration=1.5)

    window.show_view(arcade_splash)

    window.run()
