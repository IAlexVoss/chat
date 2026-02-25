import flet as ft
from models import Message
from controls import ChatMessage

class ChatController:
    def __init__(self, page: ft.Page, chat_list: ft.ListView, new_message: ft.TextField,
                 welcome_dlg: ft.AlertDialog, join_user_name: ft.TextField):
        self.page = page
        self.chat_list = chat_list
        self.new_message = new_message
        self.welcome_dlg = welcome_dlg
        self.join_user_name = join_user_name

        self.page.pubsub.subscribe(self.on_message)

    def join_click(self, e: ft.ControlEvent):
        if not self.join_user_name.value:
            self.join_user_name.error_text = "Name cannot be blank!"
            self.join_user_name.update()
        else:
            self.page.session.store.set("user_name", self.join_user_name.value)
            self.welcome_dlg.open = False
            self.new_message.prefix = ft.Text(f"{self.join_user_name.value}: ")
            self.page.pubsub.send_all(
                Message(
                    user=self.join_user_name.value,
                    text=f"{self.join_user_name.value} has joined the chat.",
                    message_type="login_message"
                )
            )
            self.page.update()

    async def send_click(self, e: ft.ControlEvent):
        if not self.new_message.value:
            return
        user_name = self.page.session.store.get("user_name")
        if not user_name:
            self.welcome_dlg.open = True
            self.page.update()
            return

        self.page.pubsub.send_all(
            Message(
                user=user_name,
                text=self.new_message.value,
                message_type="chat_message"
            )
        )
        self.new_message.value = ""
        await self.new_message.focus()
        self.page.update()

    def on_message(self, message: Message):
        if message.message_type == "chat_message":
            m = ChatMessage(message)
        elif message.message_type == "login_message":
            m = ft.Text(message.text, italic=True, color=ft.Colors.WHITE_38, size=12)
        else:
            return
        self.chat_list.controls.append(m)
        self.page.update()