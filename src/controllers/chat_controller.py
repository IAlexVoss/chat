import flet as ft
from models import Message
from controls import ChatMessage

class ChatController:
    def __init__(self, page: ft.Page, chat_list: ft.ListView, new_message: ft.TextField,
                 welcome_dlg: ft.AlertDialog, join_user_name: ft.TextField):
        self.page = page
        self.chat_list = chat_list              # component
        self.new_message = new_message          # component
        self.welcome_dlg = welcome_dlg          # component
        self.join_user_name = join_user_name    # component

        self.page.pubsub.subscribe(self.on_message)     # subscrubing the sub

    @DeprecationWarning
    def join_click(self, e: ft.ControlEvent):                                       # On join user the chat

        # If no user name value (new user in chat)
        if not self.join_user_name.value:
            self.join_user_name.error_text = "Name cannot be blank!"                # set error message
            self.join_user_name.update()                                            # update value
        else:
            self.page.session.store.set("user_name", self.join_user_name.value)     # store user name on client, on session
            self.welcome_dlg.open = False                                           
            self.new_message.prefix = ft.Text(f"{self.join_user_name.value}: ")     # set user name on chat TextField
            self.page.pubsub.send_all(                                              # send all the users on a session
                Message(
                    user=self.join_user_name.value,
                    text=f"{self.join_user_name.value} has joined the chat.",
                    message_type="login_message"                                    # type of message
                )
            )
            self.page.update()                                                      # update field

    async def send_click(self, e: ft.ControlEvent):                         # Send message from user into the chat
        if not self.new_message.value:                                      # if no message
            return
        user_name = self.page.session.store.get("user_name")                # get user name from session
        if not user_name:                                                   # if no username
            self.welcome_dlg.open = True                                    # open welcome dlg
            self.page.update()                                              # update screen
            return

        self.page.pubsub.send_all(                                          # send message to all the users from a session
            Message(
                user=user_name,                                             # username
                text=self.new_message.value,                                # message
                message_type="chat_message"                                 # type of message
            )
        )
        self.new_message.value = ""                                         # clear new message
        await self.new_message.focus()
        self.page.update()                                                  # page update

    def on_message(self, message: Message):                                                 # Paste-function: paste message into chat
        if message.message_type == "chat_message":                                          # if chat message
            m = ChatMessage(message)                                                        # create ChatMessage component
        elif message.message_type == "login_message":                                       # if login message
            m = ft.Text(message.text, italic=True, color=ft.Colors.WHITE_38, size=12)       # create Text component for login message
        else:                                                                               
            return  
        self.chat_list.controls.append(m)                                                   # add message in ListView component
        self.page.update()                                                                  # update page