from kivy.uix.popup import ModalView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDTextButton,MDIconButton
from kivy.uix.scrollview import ScrollView

from Model import UpdateScroll



class PopUps():

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






