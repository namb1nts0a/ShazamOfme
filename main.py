
from kivy.properties import StringProperty, BooleanProperty

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior



class MainBackdrop(MDScreen):
    pass


class ItemBackdropBackLayer(ThemableBehavior, MDBoxLayout):
    icon = StringProperty("android")
    text = StringProperty()
    selected_item = BooleanProperty(False)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            for item in self.parent.children:
                if item.selected_item:
                    item.selected_item = False
            self.selected_item = True
        return super().on_touch_down(touch)


class MainApp(MDApp):
    data = {
            'Camera': 'camera',
            'Gallery': 'image-multiple',
        }
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Shazam of me"
        self.theme_cls.primary_palette = "Blue"
        

    def build(self):
        self.root = MainBackdrop()


if __name__ == "__main__":
    MainApp().run()