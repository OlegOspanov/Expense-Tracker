from connection_to_db import insert_category_db,fetch_all,connect_db
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from Model import insert_db,fletch_products_name,fletch_products_category
from kivy.uix.popup import Popup,ModalView
from kivymd.uix.button import  MDTextButton
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window
from functools import partial
Window.size = (250, 500)

class MainWindow(MDBoxLayout):
    pass


class MainApp(MDApp):



    """добовление в базу данных продуктов"""
    def insert_category(self,name,value,num):
        print(name,num,value)
        if name!="" and num!="":
            insert_db(name, num, value)

    """очистка остновной формы"""
    def  clear_text_forms(self,product,price):
        product.text=""
        price.text=""


    """создание попапа"""
    def popup_new_category_btn(self):
        content = MDBoxLayout(orientation='vertical',size_hint=(0.7,0.6),)
        input_popup=MDTextField(size_hint=(1,0.8))
        content.add_widget(input_popup)
        popup_btn=MDTextButton(id="qwerty",text='Сохранить')
        content.add_widget(popup_btn)
        view = ModalView(size_hint=(None, None), size=(200,100))
        view.add_widget(content)
        view.open()
        popup_btn.bind(on_press = lambda x:insert_category_db(input_popup.text))
        popup_btn.bind(on_press=lambda x: self.save_new_category(input_popup.text))
        popup_btn.bind(on_press=lambda x: connect_db())
        popup_btn.bind(on_release=view.dismiss)


    """создание текстового файла"""
    def save_new_category(self,category):
        f = open('categorys.txt','a',encoding='utf-8')
        f.write(f"{category}\n")
        f.close()

    """создание слайдера категорий"""
    def create_list_category(self):
        for i in fetch_all():
            item1 = i[1]
            btn_container = self.root.ids.main_scroll
            btn = MDTextButton(text=item1,padding=(10))
            btn.bind(on_press = lambda x :self.insert_category(self.root.ids.product.text,item1,self.root.ids.price.text))
            btn_container.add_widget(btn)

    """очищение слайдера категорий"""
    def clean_list_category(self):
        btn_container = self.root.ids.main_scroll
        btn_container.clear_widgets()

    """очищение слайдерачастых продуктов"""
    def clean_list_often_products(self):
        btn_container = self.root.ids.often_product_scroll
        btn_container.clear_widgets()



    """создание слайдера частых продуктов"""
    def often_products(self):
        btn_container = self.root.ids.often_product_scroll
        a = fletch_products_name()
        for i in a:
            btn_text = i[0]
            btn = MDTextButton(text=f'{btn_text}', padding=(10))
            btn.bind(on_press=lambda x:self.popup_product_item(btn_text))
            btn_container.add_widget(btn)


    """создание попапа продуктов"""

    def popup_product_item(self,item):
        content = MDBoxLayout(orientation='vertical', size_hint=(0.7, 0.6), )
        input_popup = MDTextField(size_hint=(1, 0.8))
        content.add_widget(input_popup)
        popup_btn = MDTextButton(id="qwerty", text='Добавить цену')
        content.add_widget(popup_btn)
        view = ModalView(size_hint=(None, None), size=(200, 100))
        view.add_widget(content)
        view.open()
        category =  fletch_products_category(item)
        text = input_popup.text
        popup_btn.bind(on_press=lambda x: insert_db(item,text,category))




    def build(self):
        self.theme_cls.theme_style = "Dark"
        return MainWindow()


if __name__ == '__main__':
    MainApp().run()


