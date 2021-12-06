from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.datatables import MDDataTable

from kivy.metrics import dp

import pandas as pd

kv = """
Screen:
    in_class: text
    MDLabel:
        text: 'Basic Authentication App'
        font_style: 'H2'
        pos_hint: {'center_x': 0.6, 'center_y': 0.8}
    MDTextField:
        id: text
        hint_text: 'Enter you password'
        helper_text: 'Forgot your password?'
        helper_text_mode: "on_focus" 
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint_x: None
        width: 300
        icon_right: "account-search"
        required: True
        
    MDRectangleFlatButton:
        text: 'Submit'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press:
            app.submit()
            
    MDLabel:
        text: ''
        id: show
        pos_hint: {'center_x': 0.6, 'center_y': 0.2}
"""

class Dictionary():

    dictionary = pd.read_csv('Aword.csv')

    def loadDictionary():
        pass

    def valid_word_update(letters):

        working_words = []

        for i in range(len(Dictionary.dictionary['Word'])):
        
            if ((Dictionary.dictionary['Word'][i][len(Dictionary.dictionary['Word'][i])-2]) == letters[2].lower()):   #this is working
                for j in range(1, len(Dictionary.dictionary['Word'][i])-2):
                    if ((Dictionary.dictionary['Word'][i][j]) == letters[1].lower()):
                        if(Dictionary.dictionary['Word'][i][0].lower() == letters[0].lower()): #this is just to double check since there can be wrong words in the .csv files
                            working_words.append(Dictionary.dictionary['Word'][i])
                            break
        
        return working_words
    

class Main(MDApp):
    in_class = ObjectProperty(None)

    def build(self):
        return Builder.load_string(kv)

    def submit(self):
        letters = self.root.in_class.text

        label = self.root.ids.show
        label.text = "".join(Dictionary.valid_word_update(letters))    #better way to do this

if __name__ == '__main__':
    Main().run()