import json as js

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.list import (ImageLeftWidget, MDList, OneLineIconListItem,
                             OneLineListItem, TwoLineListItem)

import phraseList
from context_manager import SQLite
from dataclass import Phrase, Traduction
from importer import Importer

DATAFILE = r"./data/datasqlite3.db"
FLAG_PATH = '/Users/malorycouvet/programmation/Projects/TripPhrase_Kivy_V2/content/country_icon'

sql_create_phrase_table = """CREATE TABLE IF NOT EXISTS phrase (
                                    lang TEXT NOT NULL,
                                    content TEXT NOT NULL,
                                    context TEXT NOT NULL,
                                    trad_id INTEGER NOT NULL
                                    )"""

sql_create_traduction_table = """CREATE TABLE IF NOT EXISTS traduction (
                                    trad_count INTEGER NOT NULL,
                                    trad_list TEXT
                                    
                                )"""

sql_get_last_trad_id = "SELECT * FROM traduction ORDER BY column DESC LIMIT 1;"

with SQLite(file_name=DATAFILE) as cur:
    cur.execute(sql_create_phrase_table)
    cur.execute(sql_create_traduction_table)
   
class CountryList(MDList):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gen_listItem()


    def gen_listItem(self):
        import os
        for file in os.listdir(FLAG_PATH):
            if file.endswith('.png'):
                country = file.replace('.png','')
                list_item = ButtonLang(
                    text = country
                    )
                image = ImageLeftWidget(source = f'{FLAG_PATH}/{country}.png')
                list_item.add_widget(image)
                self.add_widget(list_item)


class ButtonLang(OneLineIconListItem):
    def callback(self):
        print(f'{self.text}')


class HomeScreen(MDBoxLayout):
    def callback(self, txt):
        print(txt)
    



class MainApp(MDApp):


    def Build(self):
        return HomeScreen()

    def on_start(self):
        self.load_database()
        

    def load_database(self):
        """ Load and instanciate all Dataclass object from database collection"""
        
        #call the method DBall from dataclass to load data from database
        Phrase.DBall()
        Traduction.DBall()
        
    
    def callback(self):
        print(self.txt)

if __name__ == '__main__':
    
    MainApp().run()

   

