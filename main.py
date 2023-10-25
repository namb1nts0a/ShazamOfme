from kivy.properties import StringProperty, BooleanProperty, DictProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2

from faceRecognition import FaceRecognition


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
        self.icon = "assets/images/icon.ico"
        self.fr = FaceRecognition()
        
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

    def load_video(self, *args):
        ret, frame = self.capture.read()
        self.image_frame = frame
        self.fr.run_recognation(frame)

        buffer = cv2.flip(frame, 0).tobytes()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture

    def callback(self, button):
        camera_screen = self.root.get_screen('camera')
        if camera_screen:
            camera_image = camera_screen.ids.camera_image
            if button.icon == "camera":
                self.root.current = "camera"
                self.image = camera_image
                self.capture = cv2.VideoCapture(0)
                Clock.schedule_interval(self.load_video, 1.0/60.0)
        elif button.icon == "image-multiple":
            print("galery ee")

    def click(self):
        self.root.current = "main_backdrop"
        self.image = None
        Clock.unschedule(self.load_video)
        self.capture.release()
        self.capture = None


if __name__ == "__main__":
    MainApp().run()