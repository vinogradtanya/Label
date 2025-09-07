from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        lbl = Label(text = 'hello\nlable',
                    font_size = 70,
                    color = [0.8, 0.3, 0, 1],
                    halign = 'center',
                    #underline = True,
                    #strikethrough = True,
                    font_name = 'Arial')
        return lbl

if __name__ == '__main__':
    app = MyApp()
    app.run()