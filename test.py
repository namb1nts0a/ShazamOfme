# Fichier Python (main.py)
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2

KV = '''
BoxLayout:
    orientation: "vertical"
    Image:
        id: camera_image
'''

class TestApp(MDApp):
    def build(self):
        self.root = Builder.load_string(KV)
        self.image = self.root.ids.camera_image
        
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.load_video, 1.0/30.0)
        return self.root

    def load_video(self, *args):
        ret, frame = self.capture.read()
        self.image_frame = frame
        cv2.putText(self.image_frame, "text ici", (60, 60), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 1)
        
        buffer = cv2.flip(frame, 0).tobytes()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture

if __name__ == "__main__":
    TestApp().run()
