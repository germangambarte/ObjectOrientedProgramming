import tkinter as tk

from Color_Palette import Color_Palette


class Aplicacion(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        palette = Color_Palette()

        self.title("Geometría Grid")
        self.configure(bg=palette.get_bg())

        label_a = tk.Label(
            self, text="Label A", bg=palette.get_yellow(), fg=palette.get_fg_2()
        )
        label_b = tk.Label(
            self, text="Label B", bg=palette.get_red(), fg=palette.get_fg_2()
        )
        label_c = tk.Label(
            self, text="Label C", bg=palette.get_blue(), fg=palette.get_fg_2()
        )
        label_d = tk.Label(
            self, text="Label D", bg=palette.get_green(), fg=palette.get_fg_2()
        )
        label_e = tk.Label(
            self, text="Label E", bg=palette.get_magenta(), fg=palette.get_fg_2()
        )

        label_a.place(relwidth=0.25, relheight=0.25)
        label_b.place(x=100, anchor=tk.N, width=100, height=50)
        label_c.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.5, relheight=0.5)
        label_d.place(
            in_=label_c,
            anchor=tk.CENTER,
            # x=2,
            # y=2,
            relx=0.5,
            rely=0.5,
            relwidth=0.5,
            relheight=0.5,
        )
        label_e.place(x=200, y=200, anchor=tk.SE, relwidth=0.25, relheight=0.25)


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
