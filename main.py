
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout


from Model import *
from kivy.uix.popup import Popup,ModalView
from kivymd.uix.button import  MDTextButton
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from View import *

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
        popup_btn.bind(on_press = lambda x:insert_db_category(input_popup.text))
        popup_btn.bind(on_press=lambda x: self.save_new_category(input_popup.text))
        popup_btn.bind(on_release=view.dismiss)


    """создание текстового файла"""
    def save_new_category(self,category):
        f = open('categorys.txt','a',encoding='utf-8')
        f.write(f"{category}\n")
        f.close()

    """создание слайдера категорий"""
    def create_list_category(self):
        btn_container = self.root.ids.main_scroll
        btn1 = MDTextButton(text='Добавить новую категорию', padding=(10))
        btn1.bind(on_press=lambda x: self.popup_new_category_btn())
        btn_container.add_widget(btn1)
        for i in fetch_all():
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
        a = fletch_products_name()
        for i in a:
            btn_text = i[0]
            btn = MDTextButton(text=f'{btn_text}', padding=(10))
            btn.bind(on_press=lambda x,text = btn_text: self.popup_product_item(text))
            btn_container.add_widget(btn)


    """создание попапа продуктов"""
    def popup_product_item(self,item):
        content = MDBoxLayout(orientation='vertical', size_hint=(0.7, 0.7), )
        label = MDLabel(text=item)
        content.add_widget(label)
        price = fletch_products_price(item)
        input_popup = MDTextField(size_hint=(1, 0.8),text=f'{price}')
        content.add_widget(input_popup)
        popup_btn = MDTextButton(id="qwerty", text='Добавить цену')
        content.add_widget(popup_btn)
        view = ModalView(size_hint=(None, None), size=(200, 130))
        view.add_widget(content)
        view.open()
        category =  fletch_products_category(item)
        popup_btn.bind(on_press=lambda x: insert_db(item,input_popup.text,category))
        popup_btn.bind(on_release=view.dismiss)

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


