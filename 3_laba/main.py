from tkinter import messagebox, Tk
from gui import TicTacToeGUI


def main():
    try:
        root = Tk()
        app = TicTacToeGUI(root)
        root.protocol("WM_DELETE_WINDOW", app.exit_game)
        root.mainloop()

    except Exception as e:
        print(f"Ошибка при запуске приложения: {e}")
        messagebox.showerror("Не удалось запустить приложение")


if __name__ == "__main__":
    main()
