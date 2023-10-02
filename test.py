from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.imagelist import MDSmartTile
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

root_kv = """
<MySmartTileWithLabel@SmartTileWithLabel>:
    font_style: "Subhead"


MDBackdrop:
    left_action_items: [["menu", lambda x: x]]
    md_bg_color: app.theme_cls.primary_color
    header_text: "My App"

    MDBackdropFrontLayer:

        ScreenManager:
            id: manager
            MDScreen:
                name: "one"

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
                            stars_color: "#478945"
                            source: "1234.JPG"
                            MDIconButton:
                                icon: "heart-outline"
                                theme_icon_color: "Custom"
                                icon_color: 1, 0, 0, 1
                                pos_hint: {"center_y": .5}
                                on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"
                        MDSmartTile:
                            stars: 3
                            source: "1234.JPG"
                            MDLabel:
                                text:"hello "
                                
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
