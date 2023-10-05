
from kivy.properties import StringProperty, BooleanProperty, DictProperty
from camera4kivy.preview import Preview
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior


class CameraScreen(MDScreen):
    pass


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
    data = DictProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Shazam of me"
        
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.data = {
            'Camera': [
                'camera',
                'on_press', lambda x:print("camera"),
                'on_release', lambda x: self.callback(x)
                ],

            'Gallery': [
                'image-multiple'
                ],
        }
        # self.root = MainBackdrop()

    def callback(self, button):
        camera_screen = self.root.get_screen('camera')
        if camera_screen:
            camera_preview = camera_screen.ids.camera_preview
            if button.icon == "camera":
                self.root.current = "camera"
                camera_preview.connect_camera(enable_analyze_pixels=True)
                camera_preview.select_camera('0')  # Naviguer vers la nouvelle fenêtre
        elif button.icon == "image-multiple":
            print("galery ee")


if __name__ == "__main__":
    MainApp().run()