import flet as ft
from app import App


def main(page: ft.Page):
    
    app = App(page)             # app build and run

if __name__ == "__main__":
    ft.run(main, no_cdn=True)   # run the script