from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.lang import Builder

kv = '''
<MyWidget>:
    orientation: 'vertical'
    padding: 10
    spacing: 10

    Spinner:
        id: spinner
        text: 'Select an item'
        values: ['Item 1', 'Item 2', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 3', 'Item 4']
        size_hint_y: None
        height: 40
        on_text: root.on_spinner_select(spinner.text)
        # Aligner le texte à droite
        text_autoupdate: True
        halign: 'right'

    Label:
        id: selected_label
        text: 'Selected: None'
        size_hint_y: None
        height: 40
        color: (0, 0, 0, 1)
'''

class MyWidget(BoxLayout):
    def on_spinner_select(self, selected_text):
        # Mettre à jour le label avec l'élément sélectionné
        self.ids.selected_label.text = f'Selected: {selected_text}'

class MyApp(App):
    def build(self):
        Builder.load_string(kv)
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()
