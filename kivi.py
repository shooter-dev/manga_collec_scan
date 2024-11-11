import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty
from kivy.lang import Builder

# Configurer les variables d'environnement pour le framebuffer
os.environ["KIVY_METRICS_DENSITY"] = "2"
os.environ["KIVY_BCM_DISPMANX"] = "1"
os.environ["KIVY_GL_BACKEND"] = "gl"
os.environ["DISPLAY"] = ":0"

# Interface utilisateur de la liste dans le fichier KV pour plus de clarté
kv = '''
<SelectableLabel>:
    # Style de chaque élément sélectionnable dans la liste
    canvas.before:
        Color:
            rgba: (0.1, 0.5, 0.5, 1) if self.selected else (0.1, 0.1, 0.1, 1)
        Rectangle:
            pos: self.pos
            size: self.size
    size_hint_y: None
    height: 40
    padding: [10, 10]  # Mettre à jour le remplissage avec une liste ou un tuple
    color: (1, 1, 1, 1)

<CustomRecycleView>:
    viewclass: 'SelectableLabel'
    RecycleBoxLayout:
        default_size: None, dp(40)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
'''

# Classe d'élément sélectionnable
class SelectableLabel(RecycleDataViewBehavior, Label):
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            self.selected = not self.selected
            return True
        return False

# Classe RecycleView personnalisée
class CustomRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super(CustomRecycleView, self).__init__(**kwargs)
        self.data = [{'text': f'Item {i}'} for i in range(1, 51)]  # Exemples d'éléments

# Application principale
class MyApp(App):
    def build(self):
        Builder.load_string(kv)  # Charger le KV design
        return CustomRecycleView()  # Retourner l'instance RecycleView

if __name__ == '__main__':
    MyApp().run()
