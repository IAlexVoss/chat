import flet as ft
from controllers.chat_controller import ChatController
from views.chat_view import ChatView
from components import ChatComponents


class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Flet Chat"

        # Create components
        self.components = ChatComponents(page)

        # Create Controller functions
        self.controller = ChatController(
            page=self.page,
            chat_list=self.components.chat_list,
            new_message=self.components.new_message,
            welcome_dlg=self.components.welcome_dlg,
            join_user_name=self.components.join_user_name
        )

        # Functions binding
        self.components.join_user_name.on_submit = self.controller.join_click
        self.components.welcome_dlg.actions[0].on_click = self.controller.join_click
        self.components.new_message.on_submit = self.controller.send_click
        
        # Filling and creating view
        chat_view = ChatView(
            chat_list=self.controller.chat_list,
            new_message=self.controller.new_message,
            on_send_click=self.controller.send_click
        )

        # add chat view on page
        self.page.add(chat_view)

        # update page
        self.page.update()