import flet as ft

class ChatComponents:
    def __init__(self, page: ft.Page):
        self.page = page

        self.join_user_name = ft.TextField(                 # TextField for input username
            label="Enter your name to join the chat",
            autofocus=True,
        )

        self.welcome_dlg = ft.AlertDialog(                  # Welcome dlg frame, TextField component included
            open=True,
            modal=True,
            title=ft.Text("Welcome!"),
            content=ft.Column([self.join_user_name], width=300, height=70, tight=True),
            actions=[ft.Button(content=ft.Text("Join chat"))],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        self.chat_list = ft.ListView(                       # ListView - for collect chat messages
            expand=True,
            spacing=10,
            auto_scroll=True,
        )

        self.new_message = ft.TextField(                    # TextField option for writing user message
            hint_text="Write message",
            autofocus=True,
            shift_enter=True,
            min_lines=1,
            max_lines=5,
            filled=True,
            expand=True,
        )

        self.page.overlay.append(self.welcome_dlg)          # instantly add welcome dlg frame

    def reset_input(self):                                  # For reset user messgae in input TextField
        self.new_message.value = ""
        self.new_message.focus()

