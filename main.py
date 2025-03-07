from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.popup import Popup,ModalView
from kivymd.uix.button import  MDTextButton
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window
from kivymd.uix.label import MDLabel

from View import *
from Model import *

Window.size = (250, 500)


class MainWindow(MDBoxLayout):
    pass


class MainApp(MDApp):



    """добовление в базу данных продуктов"""
    def insert_category(self,name,value,num):
        print(name,num,value)
        if name!="" and num!="":
            Insert_db.insert_db(name, num, value)

    """очистка остновной формы"""
    def  clear_text_forms(self,product,price):
        product.text=""
        price.text=""





    """создание текстового файла"""
    def save_new_category(self,category):
        f = open('categorys.txt','a',encoding='utf-8')
        f.write(f"{category}\n")
        f.close()

    """создание слайдера категорий"""
    def create_list_category(self):
        btn_container = self.root.ids.main_scroll
        btn1 = MDTextButton(text='Добавить новую категорию', padding=(10))
        btn1.bind(on_press=lambda x: PopUps.popup_new_category_btn(self))
        btn_container.add_widget(btn1)
        for i in SelectDB.fetch_all(self):
            item1 = i[1]
            btn = MDTextButton(text=item1,padding=(10))
            btn.bind(on_press = lambda x ,item=item1 :self.insert_category(self.root.ids.product.text,item,self.root.ids.price.text))
            btn.bind(on_release = lambda x:self.clear_text_forms(self.root.ids.product,self.root.ids.price))
            btn_container.add_widget(btn)



    """очищение слайдера категорий"""
    def clean_list_category(self):
        btn_container = self.root.ids.main_scroll
        btn_container.clear_widgets()

    """очищение слайдера частых продуктов"""
    def clean_list_often_products(self):
        btn_container = self.root.ids.often_product_scroll
        btn_container.clear_widgets()


    """создание слайдера частых продуктов"""
    def often_products(self):
        btn_container = self.root.ids.often_product_scroll
        a = SelectProductsItem.fetch_products_name(self)
        for i in a:
            btn_text = i[0]
            btn = MDTextButton(text=f'{btn_text}', padding=(10))
            btn.bind(on_press=lambda x,text = btn_text: PopUps.popup_product_item(self,text))
            btn_container.add_widget(btn)




    """создание списка итоговых сумм"""
    def create_list_total(self):
        total = Total.get_total(self)
        container = self.root.ids.statistic_scroll
        label1 = MDTextButton(padding=(10,0,0,0),text=f'Итого: {total}', disabled=True)
        container.add_widget(label1)
        categorys = Buttons_total.get_categorys_tuple(self)
        for i in categorys:
            modal_view = PopUps()
            price = Buttons_total.get_price_category(self,i)
            btn = MDTextButton(padding=(10),text=f'{i} {price}')
            btn.bind(on_press=lambda x, name=i : modal_view.create_popup(name))
            container.add_widget(btn)






    """очищение списка итогов"""
    def clean_list_total(self):
        container = self.root.ids.statistic_scroll
        container.clear_widgets()

    """добавление функции смены вкладок в кнопке другая категория"""
    def switch_btn(self):
        btn = self.root.ids.another_category_btn
        btn.switch_tab("Screen 2")

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        return MainWindow()


if __name__ == '__main__':
    MainApp().run()


