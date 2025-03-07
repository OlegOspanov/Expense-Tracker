from kivy.uix.popup import ModalView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDTextButton,MDIconButton
from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextField

from Model import UpdateScroll, Insert_db, SelectProductsItem, SelectDB


class PopUps:

    """создание попапа категорий"""
    def popup_new_category_btn(self):
        content = MDBoxLayout(orientation='vertical', size_hint=(0.7, 0.6), )
        input_popup = MDTextField(size_hint=(1, 0.8))
        content.add_widget(input_popup)
        popup_btn = MDTextButton(id="qwerty", text='Сохранить')
        content.add_widget(popup_btn)
        view = ModalView(size_hint=(None, None), size=(200, 100))
        view.add_widget(content)
        view.open()
        popup_btn.bind(on_press=lambda x: Insert_db.insert_db_category(input_popup.text))
        #popup_btn.bind(on_press=lambda x: self.save_new_category(input_popup.text))
        popup_btn.bind(on_release=view.dismiss)

    """создание попапа итоговых сумм"""
    def create_popup(self,category):
        view = ModalView(size_hint=(None, None), size=(230, 450))
        view.open()
        content = MDBoxLayout(orientation='vertical')
        btn = MDIconButton(icon_color=(.60,.60,.60,1),icon="exit-to-app")
        btn.bind(on_press=view.dismiss)
        scroll_area = ScrollView()
        products = UpdateScroll.get_product(self,category)
        for i in products:
            price = UpdateScroll.get_sum_price(self,i)
            btn1 = MDTextButton(padding=(10), text=f'{i}   {price}')
            content.add_widget(btn1)
        content.add_widget(btn)
        content.add_widget(scroll_area)
        view.add_widget(content)


    """создание попапа продуктов"""
    def popup_product_item(self,item):
        content = MDBoxLayout(orientation='vertical', size_hint=(0.7, 0.7), )
        label = MDLabel(text=item)
        content.add_widget(label)
        price = SelectProductsItem.fetch_products_price(item)
        input_popup = MDTextField(size_hint=(1, 0.8), text=f'{price}')
        content.add_widget(input_popup)
        popup_btn = MDTextButton(id="qwerty", text='Добавить цену')
        content.add_widget(popup_btn)
        view = ModalView(size_hint=(None, None), size=(200, 130))
        view.add_widget(content)
        view.open()
        category = SelectDB.fetch_products_category(self, item)
        popup_btn.bind(on_press=lambda x: Insert_db.insert_db(item, input_popup.text, category))
        popup_btn.bind(on_release=view.dismiss)





