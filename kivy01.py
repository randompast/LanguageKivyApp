from kivymd.uix.behaviors import HoverBehavior
import io
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.tooltip import MDTooltip

KV = '''
MDScreen:
'''

es = ''
en = ''

class HoverItem(MDBoxLayout, ThemableBehavior, HoverBehavior):
    '''Custom item implementing hover behavior.'''

    def print_properties(instance):
        props = dir(instance)
        for p in props:
            print(p, instance.getattribute(p))

    def on_enter(self, *args):
        print(self.ids)
        self.clear_widgets()
        es = self.ids.es
        en = self.ids.en
        self.add_widget(
            MDLabel(text=en)
        )
        '''The method will be called when the mouse cursor
        is within the borders of the current widget.'''

    def on_leave(self, *args):
        self.clear_widgets()
        es = self.ids.es
        en = self.ids.en
        self.add_widget(
            MDLabel(text=es)
        )
        '''The method will be called when the mouse cursor goes beyond
        the borders of the current widget.'''

class TooltipLabel(MDLabel, MDTooltip):
    pass

class Main(MDApp):
    def get_file(self, fn):
        with open(fn, "r", encoding="utf-8") as f:
            return f.readlines()

    def add_label(self, screen, label):
        screen.add_widget(label)

    def build(self):
        en_text = self.get_file('Books.en-es.en')
        es_text = self.get_file('Books.en-es.es')
        screen = Builder.load_string(KV)
        box = MDBoxLayout(orientation="horizontal")
        screen.add_widget(box)
        # Names of standard color themes.
        es_data = es_text[1].split(' ')
        en_data = en_text[1].split(' ')
        print(es_data)
        for i,w in enumerate(es_data):
            id = {'es':w,'en':en_data[i]}
            hover_item = HoverItem(
                ids=id
            )
            label = MDLabel(
                text=w,
            )
            hover_item.add_widget(label)
            self.add_label(box, hover_item)
        return screen


Main().run()
