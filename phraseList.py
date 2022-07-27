
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem
import sqlite3
from dataclass import Traduction, Phrase

class PhraseList(MDList):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gen_contextItems()

    def context_callback(self, text):
        self.clear()
        self.gen_listItem(text)
       
        
    def retour_callback(self):
        self.clear()
        self.gen_contextItems()

    def clear(self):
        self.clear_widgets()
    
    def gen_contextItems(self):
        avail_context = ['Salutation','Restaurant_bar','Remerciement','Presentation','Direction','time','Numbers']
        for cont in avail_context:
            list_item = ButtonContext(
                text = cont
            )
            self.add_widget(list_item)
    
    def gen_listItem(self, context):
        phrase_list = self.get_context_lang_phrase_list(context, 'French')

        retourButton = ReturnButton(
                text = 'retour'
            )
        self.add_widget(retourButton)

        for phrase in phrase_list:
            traduction = phrase.get_trad('English')
            phrase_button = ButtonPhrase(
                text = phrase.content,
                secondary_text = phrase.get_trad('English').content
            )
            if traduction.phrase_id :
                del traduction
        
            self.add_widget(phrase_button)
        retourButton = ReturnButton(
            text = 'retour'
        )
        self.add_widget(retourButton)
            
            
        

    def get_context_lang_phrase_list(self, context, lang):
        phrase_list = []
        for phrase in Phrase :
            if (phrase.context == context) & (phrase.lang == lang):
                phrase_list.append(phrase)
            
        return phrase_list


class ButtonContext(OneLineListItem):
    pass
class ReturnButton(OneLineListItem):
    pass

class ButtonPhrase(TwoLineListItem):
    def callback(self):
        print(f'{self.text}')