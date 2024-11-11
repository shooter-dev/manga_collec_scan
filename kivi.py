from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.lang import Builder

kv = '''
<HeaderNews>:
    orientation: 'horizontal'
    padding: 0
    spacing: 0
    size_hint: None, None
    size: 714, 51
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1
        Line:
            width: 2
            rectangle: self.x, self.y, self.width, self.height
            dash_offset: 10

    Label:
        id: name_page_label
        text: "Nouveautés"
        font_size: '18sp'
        bold: True
        size_hint_x: None
        width: 400  # Ajuster selon les besoins
        halign: 'left'
        valign: 'middle'

    Spinner:
        id: publisher_combo_box
        text: 'Editeurs'
        values: ['Editeurs', 'Akata', 'Ankama', 'Asuka', 'Auto-Edition', 'Black Blox', 'Bookmark', 'Clair de Lune', 'Crunchyroll/Kazé', 'Delcourt/Tonkam']
        size_hint: None, None
        size: 223, 28
        font_size: '17sp'
        background_normal: ''  # Ajouter une image ou un fond si besoin
        background_color: 1, 1, 1, 1
        on_text: app.on_spinner_select(self.text)

        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [4]
'''

class HeaderNews(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        Builder.load_string(kv)
        return HeaderNews()

    def on_spinner_select(self, selected_text):
        print(f"Éditeur sélectionné: {selected_text}")

if __name__ == '__main__':
    MyApp().run()
