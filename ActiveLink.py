from kivy.app import App
from kivy.uix.label import Label
import webbrowser

class MyApp(App):
    def build(self):
        lbl = Label(text="Для перехода по ссылке нажмите [ref=][i][u]сюда[/u][/i][/ref]",
                    font_size=30,
                    color=[0.8, 0.3, 0, 1],
                    markup=True)

        lbl.bind(on_ref_press=self.link)
        return lbl

    def link(self, instance, value):
        webbrowser.open("https://translate.yandex.ru/?lang=en-ru&text=-")

if __name__ == "__main__":
    MyApp().run()