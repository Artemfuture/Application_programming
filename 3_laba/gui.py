from tkinter import (
    messagebox,
    Frame,
    Button,
    SUNKEN,
    BOTTOM,
    Toplevel,
    Label,
    LEFT,
    RIGHT,
    X,
    Tk,
)
from constants import *
from game_logic import GameLogic
from menu import GameMenu


class TicTacToeGUI:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title(GAME_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.minsize(MIN_WIDTH, MIN_HEIGHT)
        self.root.configure(bg=BG_COLOR)
        self.game_logic = GameLogic()
        self.create_game_board()
        self.create_status_bar()
        self.menu = GameMenu(self.root, self)

    def create_game_board(self):
        board_frame = Frame(self.root, bg=BG_COLOR)
        board_frame.pack(pady=20)
        self.buttons = []
        for i in range(3):
            button_row = []
            for j in range(3):
                button = Button(
                    board_frame,
                    text="",
                    font=("Arial", 24, "bold"),
                    width=6,
                    height=3,
                    bg=BUTTON_BG,
                    fg="black",
                    command=lambda row=i, col=j: self.make_move(row, col),
                )
                button.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
                button_row.append(button)
            self.buttons.append(button_row)

        for i in range(3):
            board_frame.grid_rowconfigure(i, weight=1)
            board_frame.grid_columnconfigure(i, weight=1)

    def create_status_bar(self):
        status_frame = Frame(
            self.root, bg=STATUS_BAR_COLOR, relief=SUNKEN, borderwidth=1
        )
        status_frame.pack(fill=X, side=BOTTOM, pady=5)

        self.player_label = Label(
            status_frame,
            text="Текущий игрок: X",
            font=("Arial", 10),
            bg=STATUS_BAR_COLOR,
        )
        self.player_label.pack(side=LEFT, padx=10)
        self.score_label = Label(
            status_frame,
            text=f"Счет: {self.game_logic.get_score_text()}",
            font=("Arial", 10),
            bg=STATUS_BAR_COLOR,
        )
        self.score_label.pack(side=RIGHT, padx=10)

    def make_move(self, row, col):
        try:
            valid_move, game_state, winner = self.game_logic.make_move(row, col)
            if not valid_move:
                return
            self.buttons[row][col].config(
                text=self.game_logic.current_player,
                fg=X_COLOR if self.game_logic.current_player == "X" else O_COLOR,
            )
            self.game_logic.current_player = "O" if self.game_logic.current_player == "X" else "X"
            if game_state == "win":
                self.highlight_winner_cells()
                messagebox.showinfo("Победа!", f"Игрок {winner} победил!")
                self.update_score()
                self.new_game()
            elif game_state == "draw":
                messagebox.showinfo("Ничья!", "Игра закончилась вничью!")
                self.update_score()
                self.new_game()
            else:
                self.player_label.config(
                    text=f"Текущий игрок: {self.game_logic.current_player}"
                )

        except Exception as e:
            self.handle_error(f"Ошибка при выполнении хода: {str(e)}")

    def highlight_winner_cells(self):
        for row, col in self.game_logic.winning_cells:
            self.buttons[row][col].config(bg=WINNER_COLOR)

    def new_game(self):
        try:
            self.game_logic.reset_game()
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j].config(text="", bg=BUTTON_BG)

            self.player_label.config(text="Текущий игрок: X")

        except Exception as e:
            self.handle_error(f"Ошибка при создании новой игры: {str(e)}")

    def show_settings(self):
        try:
            settings_window = Toplevel(self.root)
            settings_window.title("Настройки")
            settings_window.geometry("300x200")
            settings_window.resizable(False, False)
            settings_window.transient(self.root)
            settings_window.grab_set()

            Label(settings_window, text="Настройки игры", font=("Arial", 14)).pack(
                pady=10
            )

            Button(
                settings_window,
                text="Сбросить счет",
                command=self.reset_score,
                width=20,
            ).pack(pady=10)

            Label(
                settings_window,
                text=f"Текущий размер окна: {self.root.winfo_width()}x{self.root.winfo_height()}",
                font=("Arial", 10),
            ).pack(pady=10)

        except Exception as e:
            self.handle_error(f"Ошибка при открытии настроек: {str(e)}")

    def reset_score(self):
        self.game_logic.reset_score()
        self.update_score()
        messagebox.showinfo("Счет сброшен", "Счет игры был сброшен.")

    def update_score(self):
        self.score_label.config(text=f"Счет: {self.game_logic.get_score_text()}")

    def exit_game(self):
        if messagebox.askyesno("Выход", "Вы уверены, что хотите выйти?"):
            self.root.quit()

    def handle_error(self, error_message):
        print(f"Ошибка: {error_message}")
        messagebox.showerror(
            "Ошибка",
            f"Произошла ошибка:\n{error_message}\n\nПопробуйте начать новую игру.",
        )
