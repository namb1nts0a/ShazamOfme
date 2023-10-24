from kivy.lang import Builder
from kivymd.app import MDApp


root_kv = """
MDBoxLayout:
    orientation: "vertical"

    MDBottomNavigation:
        id: panel

        MDBottomNavigationItem:
            name: "files2"
            text: "C++"
            icon: "language-cpp"

            MDLabel:
                font_style: "Body1"
                theme_text_color: "Primary"
                text: "I programming of C++"
                halign: "center"

        MDBottomNavigationItem:
            name: "files3"
            text: "JS"
            icon: "language-javascript"

            MDLabel:
                font_style: "Body1"
                theme_text_color: "Primary"
                text: "Oh god JS again"
                halign: "center"
"""


class TestApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "KivyMD Examples - Bottom Navigation"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_string(root_kv)


if __name__ == "__main__":
    TestApp().run()