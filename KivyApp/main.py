import threading

import websocket
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from websocket import create_connection


class MainPage(BoxLayout):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = (30, 0)
        self.spacing = 25

        # Entry for Name
        self.name_entry = TextInput(hint_text='Name...', multiline=False, height=25, text='')
        self.add_widget(self.name_entry)

        # Editor for Messages
        self.messages_editor = TextInput(hint_text='Enter your message', multiline=True, height=500, text='')
        self.add_widget(self.messages_editor)

        # Grid for Message and Send Button
        grid_layout = BoxLayout(orientation='horizontal', spacing=10)

        # Entry for Message
        self.message_entry = TextInput(hint_text='Message...', multiline=False, height=25, text='')
        grid_layout.add_widget(self.message_entry)

        # Button for Send
        send_button = Button(text='Send', on_press=self.btn_send_clicked, size_hint_x=None, height=25, width=100)
        grid_layout.add_widget(send_button)

        self.add_widget(grid_layout)

        def on_message(wsapp, message):
            print(message)
            self.messages_editor.text += message + '\n'


        def on_ping(wsapp, message):
            pass


        def on_pong(wsapp, message):
            pass



        self.ws = websocket.WebSocketApp("ws://localhost:8000/ws", on_message=on_message, on_ping=on_ping, on_pong=on_pong)
        self.ws.run_forever(ping_interval=60, ping_timeout=10, ping_payload="This is an optional ping payload")
        self.ws.close()
        """ws_thread = threading.Thread(target = self.ws.run_forever)
        ws_thread.start()"""

    def btn_send_clicked(self, instance):
        self.ws.send(self.message_entry.text)
        self.message_entry.text = ""


class MyApp(App):
    def build(self):
        return MainPage()

if __name__ == "__main__":
    MyApp().run()


