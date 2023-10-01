from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.imagelist import MDSmartTile

root_kv = """
<MySmartTileWithLabel@SmartTileWithLabel>:
    font_style: "Subhead"


MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        left_action_items: [["menu", lambda x: x]]
        md_bg_color: app.theme_cls.primary_color

    ScreenManager:
        id: manager

        MDScreen:
            name: "one"

            MDRaisedButton:
                pos_hint: {"center_x": .5, "center_y": .55}
                on_release: manager.current = "two"
                text: "Open Grid"

        MDScreen:
            name: "two"

            ScrollView:
                do_scroll_x: False

                MDGridLayout:
                    cols: 2
                    row_default_height: (self.width - self.cols*self.spacing[0]) / self.cols
                    row_force_default: True
                    adaptive_height: True
                    padding: dp(4), dp(4)
                    spacing: dp(4)

                    MDSmartTile:
                        stars: 3
                        source: "1234.JPG"
                    MDSmartTile:
                        stars: 3
                        source: "1234.JPG"
                    MDSmartTile:
                        text: "Beautiful\\n[size=12]beautiful-931152_1280.jpg[/size]"
                        source: "1234.JPG"
                    MDSmartTile:
                        text: "Robin\\n[size=12]robin-944887_1280.jpg[/size]"
                        source: "1234.JPG"
                    MDSmartTile:
                        text: "Kitten\\n[size=12]kitten-1049129_1280.jpg[/size]"
                        source: "1234.JPG"
                    MDSmartTile:
                        text: "Light-Bulb\\n[size=12]light-bulb-1042480_1280.jpg[/size]"
                        source: "1234.JPG"
                    MDSmartTile:
                        text: "Tangerines\\n[size=12]tangerines-1111529_1280.jpg[/size]"
                        source: "1234.JPG"
"""


class MainApp(MDApp):
    def build(self):
        self.root = Builder.load_string(root_kv)


if __name__ == "__main__":
    MainApp().run()