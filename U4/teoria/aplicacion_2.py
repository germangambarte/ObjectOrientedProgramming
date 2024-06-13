import tkinter as tk

from Color_Palette import Color_Palette


class Aplicacion(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        palette = Color_Palette()

        self.title("Geometría Pack")
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

        opts = {"ipadx": 10, "ipady": 10, "fill": tk.BOTH, "expand": True}

        label_a.pack(side=tk.TOP, **opts)
        label_b.pack(side=tk.TOP, **opts)
        label_c.pack(side=tk.LEFT, **opts)
        label_e.pack(side=tk.LEFT, **opts)
        label_d.pack(side=tk.LEFT, **opts)


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
