#By Cheriet Noureddine
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.network.urlrequest import UrlRequest

class gApp(App):
    def send_req(self,btn):
        URL = r"" #Your Url
        DATA = self.inp.text
        # if You Send Request With Data Kivy Will make it as POST Request
        # Else It Will Make It as Get Request
        req = UrlRequest(url=URL,req_body=DATA,on_success=self.Success,
                         on_failure=self.Failure,on_error=self.Error)
    def Error(self,a,b):
        print('Error!',a,b)
    def Failure(self):
        print('Failure')
    def Success(self,a,b):
        print('Ok!',a,b)
    def build(self):
        box = BoxLayout(orientation='vertical')
        self.inp = TextInput()
        self.btn = Button(text="send")
        self.btn.bind(on_press=self.send_req)

        box.add_widget(self.inp)
        box.add_widget(self.btn)
        return box

gApp().run()
