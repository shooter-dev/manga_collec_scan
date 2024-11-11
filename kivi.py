import os
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Hello, Framebuffer!")

def main():
    os.environ["KIVY_METRICS_DENSITY"] = "2"  # Ajuste la densité pour l'écran
    os.environ["KIVY_BCM_DISPMANX"] = "1"  # Active le support Raspberry Pi sans X11
    os.environ["KIVY_GL_BACKEND"] = "gl"  # Utilise OpenGL, adapté au framebuffer
    os.environ["DISPLAY"] = ":0"

    MyApp().run()

if __name__ == '__main__':
    main()