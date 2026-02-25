import flet as ft

class ChatView(ft.Container):
    def __init__(self, chat_list: ft.ListView, new_message: ft.TextField, on_send_click):
        super().__init__()
        self.expand = True

        chat_container = ft.Container(
            content=chat_list,
            border=ft.Border.all(1, ft.Colors.OUTLINE),
            border_radius=5,
            padding=10,
            expand=True,
        )

        input_row = ft.Row(
            controls=[
                new_message,
                ft.IconButton(
                    icon=ft.Icons.SEND_ROUNDED,
                    tooltip="Send message",
                    on_click=on_send_click,
                ),
            ]
        )

        self.content = ft.Column(
            controls=[
                chat_container,
                input_row,
            ],
            expand=True,
        )