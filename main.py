from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.widget import Widget

from DAO import skill_dao

class SkillDiaryApp(App):
    def build(self):
        return SkillDiaryLayout()

class CategoryDropDown(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Selecione uma categoria'
        self.bind(on_release=self.show_dropdown)

        self.dropdown = DropDown()
        
        # Adicionar a opção padrão "Selecione uma categoria"
        default_btn = Button(text='Selecione uma categoria', size_hint_y=None, height=30, disabled=True)
        self.dropdown.add_widget(default_btn)
        
        for category in ['cat1', 'cat2']:
            btn = Button(text=category, size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn: self.select(btn.text))
            self.dropdown.add_widget(btn)

    def show_dropdown(self, widget):
        self.dropdown.open(widget)

    def select(self, category):
        self.text = category
        self.dropdown.dismiss()

class SkillDiaryLayout(BoxLayout):
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.prepare_data()
        
        self.skill_input = TextInput(hint_text='Nome da Habilidade', size_hint=(1, 0.1))
        self.add_widget(self.skill_input)
        
        # self.category_input = TextInput(hint_text='Categoria', size_hint=(1, 0.1))
        # self.add_widget(self.category_input)
        
        self.category_dropdown = CategoryDropDown(size_hint=(1, 0.1))
        self.add_widget(self.category_dropdown)
        
        self.add_widget(Widget(size_hint=(1, 0.1)))
        
        button_container = BoxLayout(size_hint=(1, 0.1))
        
        # Adicionar espaço no lado esquerdo do botão
        button_container.add_widget(Widget(size_hint=(0.25, 1)))
        
        self.add_button = Button(text='Adicionar Habilidade', size_hint=(0.5, 1))
        self.add_button.bind(on_press=self.add_skill)
        button_container.add_widget(self.add_button)
        
        # Adicionar espaço no lado direito do botão
        button_container.add_widget(Widget(size_hint=(0.25, 1)))
        
        self.add_widget(button_container)
        
        self.skills_label = Label(text='Habilidades:', size_hint=(1, 0.1))
        self.add_widget(self.skills_label)
        
        self.skills_box = BoxLayout(orientation='vertical', size_hint=(1, 0.6))
        self.add_widget(self.skills_box)
        
        self.update_skills_list()
        
    def prepare_data(self):
        skill_dao.create_skills_table()
        
    def add_skill(self, instance):
        name = self.skill_input.text
        category = self.category_dropdown.text
        if name and category:
            skill_dao.add_skill(name, category)
            self.skill_input.text = ''
            self.category_dropdown.select('Selecione uma categoria')
            self.update_skills_list()

    def update_skills_list(self):
        self.skills_box.clear_widgets()
        skills = skill_dao.get_skills()
        for skill in skills:
            skill_label = Label(text=f"{skill[1]} ({skill[2]})", size_hint=(1, None))
            self.skills_box.add_widget(skill_label)
            
if __name__ == '__main__':
    SkillDiaryApp().run()
