import flet as ft
from models import Message

@ft.control
class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.message = message                                                  # Message model
        self.vertical_alignment = ft.CrossAxisAlignment.START
        self.controls = [
            ft.CircleAvatar(                                                    # Circle avatar
                content=ft.Text(self.get_initials(self.message.user)),
                color=ft.Colors.WHITE,
                bgcolor=self.get_avatar_color(self.message.user),
            ),
            ft.Column(                                                          # Column component
                tight=True,
                spacing=5,
                controls=[
                    ft.Text(self.message.user, weight=ft.FontWeight.BOLD),
                    ft.Text(self.message.text, selectable=True),
                ],
            ),
        ]

    def get_initials(self, user_name: str) -> str:                              # slef util function for get initials from username
        if user_name:
            return user_name[:1].capitalize()
        else:
            return "Unknown"
        
    def get_avatar_color(self, user_name: str):                                 # self util function for set user color
        colors_lookup = [
            ft.Colors.AMBER,
            ft.Colors.BLUE,
            ft.Colors.BROWN,
            ft.Colors.CYAN,
            ft.Colors.GREEN,
            ft.Colors.INDIGO,
            ft.Colors.LIME,
            ft.Colors.ORANGE,
            ft.Colors.PINK,
            ft.Colors.PURPLE,
            ft.Colors.RED,
            ft.Colors.TEAL,
            ft.Colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]