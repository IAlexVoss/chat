import flet as ft
from app import App


def main(page: ft.Page):
    
    app = App(page)

if __name__ == "__main__":
    ft.run(main, no_cdn=True) 