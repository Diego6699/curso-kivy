import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
class Tarefas(BoxLayout):
    def __init__(self,tarefas,**kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))

    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.add_widget(Tarefa(text = texto))
class Tarefa(BoxLayout):
    def __init__(self,text = '',**kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text
class QuizApp(App):
    def build(self):
        return

if __name__ == "__init__":
    QuizApp.run()