from kivy.lang import Builder
from kivy.properties import DictProperty, StringProperty, BooleanProperty
from kivymd.uix.screen import MDScreen
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp

KV = '''
#:import NoTransition kivy.uix.screenmanager.NoTransition
#:import Window kivy.core.window.Window
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget


<ItemBackdropFrontLayer@TwoLineAvatarListItem>
    icon: "android"

    IconLeftWidget:
        icon: root.icon


<ItemBackdropBackLayer>
    adaptive_height: True
    spacing: "10dp"
    md_bg_color:
        root.theme_cls.primary_dark \
        if root.selected_item \
        else root.theme_cls.primary_color

    MDIconButton:
        icon: root.icon
        theme_text_color: "Custom"
        text_color: (1, 1, 1, .5) if not root.selected_item else (1, 1, 1, 1)

    MDLabel:
        text: root.text
        color: (1, 1, 1, .5) if not root.selected_item else (1, 1, 1, 1)


<ItemBackdropBackLayerOfSecondScreen@BoxLayout>
    size_hint_y: None
    height: "40dp"
    spacing: "25dp"
    text: ""

    MDCheckbox:
        size_hint: None, None
        size: "30dp", "30dp"
        active: False or self.active
        pos_hint: {"center_y": .5}
        selected_color: 1, 1, 1, 1

    MDLabel:
        text: root.text
        color: 1, 1, 1, .7


<ItemRoundBackdropBackLayerOfSecondScreen@BoxLayout>
    size_hint_y: None
    height: "40dp"
    spacing: "25dp"
    text: ""

    MDCheckbox:
        group: "size"
        size_hint: None, None
        size: "30dp", "30dp"
        pos_hint: {"center_y": .5}
        selected_color: 1, 1, 1, 1

    MDLabel:
        text: root.text
        color: 1, 1, 1, .7


<MyBackdropFrontLayer@ScrollView>
    backdrop: None
    backlayer: None

    MDGridLayout:
        adaptive_height: True
        cols: 1
        padding: "5dp"

        

<MyBackdropBackLayer@ScreenManager>
    transition: NoTransition()

    MDScreen:
        name: "one screen"

        ScrollView

            MDGridLayout:
                adaptive_height: True
                cols: 1
                padding: "5dp"

                ItemBackdropBackLayer:
                    icon: "theater"
                    text: "TV & Home Theaters"

                ItemBackdropBackLayer:
                    icon: "camera-plus-outline"
                    text: "Camera and Camcorders"
                ItemBackdropBackLayer:
                    icon: "speaker"
                    text: "Speakers"

                ItemBackdropBackLayer:
                    icon: "movie-outline"
                    text: "Movies"
                ItemBackdropBackLayer:
                    icon: "gamepad-variant-outline"
                    text: "Games"
                ItemBackdropBackLayer:
                    icon: "music-circle-outline"
                    text: "Music"

MDScreenManager:
    MainScreen:
    CameraScreen:

<CameraScreen>:
    name: "camera"
    MDScreen:
        BoxLayout:
            MDLabel:
                text: "Camera Screen"
                halign: "center"
                valign: "middle"

<MainScreen>:
    

    MDBackdrop:
        id: backdrop
        on_open: print("on_open")
        on_close: print("on_close")
        left_action_items: [["menu", lambda x: self.open()]]
        title: app.title
        header_text: "hello world"

        MDBackdropBackLayer:
            MyBackdropBackLayer:
                id: backlayer

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
                                source: "assets/images/1.jpg"
                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 0, 20, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"
                                MDLabel:
                                    text: "raviny telo"
                                    color: "white"

                            MDSmartTile:
                                source: "assets/images/2.jpg"
                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 0, 20, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"
                                MDLabel:
                                    text: "hey mommie i have OCB"
                                    color: "white"
                                    
                            MDSmartTile:
                                source: "assets/images/3.jpg"
                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 0, 20, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"
                                MDLabel:
                                    text: "how are you feeling today"
                                    color: "white"

                            MDSmartTile:
                                source: "assets/images/4.jpg"
                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 0, 20, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"
                                MDLabel:
                                    text: "rarany mbola maniry"
                                    color: "white"
    MDScreen:
        MDFloatingActionButtonSpeedDial:
            id: speed_dial
            data: app.data
            root_button_anim: True
            hint_animation: True
'''

class CameraScreen(MDScreen):
    pass

class MainScreen(MDScreen):
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

class Example(MDApp):
    data = DictProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Shazam of me"
        # self.theme_cls.primary_palette = "Blue"

    def build(self):
        # self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.data = {
            'Camera': [
                'camera',
                "on_press", lambda x: print("pressed camera"),
                "on_release", self.callback
            ],
            'Gallery': [
                'image-multiple',
                "on_press", lambda x: print("pressed gallery"),
                "on_release", lambda x: self.callback
            ],
        }
        # self.root = CameraScreen()
        return Builder.load_string(KV)

    def callback(self, button):
        if button.icon == "camera":
            self.root.current = "camera"  # Naviguer vers la nouvelle fenêtre
        elif button.icon == "image-multiple":
            print("galery ee")

if __name__ == "__main__":
    Example().run()
