from tkinter import messagebox, Menu, Tk
from constants import RULES_TEXT, ABOUT_TEXT


class GameMenu:
    def __init__(self, root: Tk, game):
        self.root = root
        self.game = game
        self.create_menu()

    def create_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        game_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Игра", menu=game_menu)
        game_menu.add_command(
            label="Новая игра", command=self.game.new_game, accelerator="Ctrl+n"
        )
        game_menu.add_separator()
        game_menu.add_command(label="Настройки", command=self.game.show_settings)
        game_menu.add_separator()
        game_menu.add_command(
            label="Выход", command=self.game.exit_game, accelerator="Ctrl+q"
        )

        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Справка", menu=help_menu)
        help_menu.add_command(label="Правила игры", command=self.show_rules)
        help_menu.add_command(label="О программе", command=self.show_about)

        self.root.bind_all("<Control-n>", lambda i: self.game.new_game())
        self.root.bind_all("<Control-q>", lambda i: self.root.quit())

    def show_rules(self):
        messagebox.showinfo("Правила игры", RULES_TEXT)

    def show_about(self):
        messagebox.showinfo("О программе", ABOUT_TEXT)
