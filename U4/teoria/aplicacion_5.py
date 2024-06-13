from tkinter import *
from tkinter import ttk

from Color_Palette import Color_Palette


class Aplicacion:
    ventanas_abiertas = 0
    pos = 0
    __ventana_principal: Tk
    __dialogo: Toplevel

    def __init__(self) -> None:
        palette = Color_Palette()
        self.__ventana_principal = Tk()
        self.__ventana_principal.configure(bg=palette.get_bg())
        self.__ventana_principal.geometry("300x200")
        self.__ventana_principal.resizable(width=False, height=False)
        self.__ventana_principal.title("Abrir Dialogs")

        boton_abrir_dialog = ttk.Button(
            self.__ventana_principal,
            text="Abrir Dialogo",
            command=self.abrir_dialogo_transitorio,
        )
        boton_abrir_dialog.place(anchor=CENTER, rely=0.5, relx=0.5)
        self.__ventana_principal.mainloop()

    def abrir_dialogo(self):
        self.__dialogo = Toplevel()

        Aplicacion.ventanas_abiertas += 1
        Aplicacion.pos += 50

        self.__dialogo.geometry(f"200x100+{Aplicacion.pos}+{Aplicacion.pos}")
        self.__dialogo.resizable(width=False, height=False)

        self.__dialogo.title(
            f"{Aplicacion.ventanas_abiertas}: {self.__dialogo.winfo_id()}"
        )

        boton_cerrar_dialog = ttk.Button(
            self.__dialogo, text="Cerrar Dialogo", command=self.__dialogo.destroy
        )

        boton_cerrar_dialog.place(anchor=CENTER, rely=0.5, relx=0.5)
        self.__ventana_principal.wait_window(self.__dialogo)

    def abrir_dialogo_transitorio(self):
        self.__dialogo = Toplevel()

        Aplicacion.ventanas_abiertas += 1
        Aplicacion.pos += 50

        self.__dialogo.geometry(f"200x100+{Aplicacion.pos}+{Aplicacion.pos}")
        self.__dialogo.resizable(width=False, height=False)

        self.__dialogo.title(
            f"{Aplicacion.ventanas_abiertas}: {self.__dialogo.winfo_id()}"
        )

        boton_cerrar_dialog = ttk.Button(
            self.__dialogo, text="Cerrar Dialogo", command=self.__dialogo.destroy
        )

        boton_cerrar_dialog.place(anchor=CENTER, rely=0.5, relx=0.5)
        self.__ventana_principal.transient(master=self.__ventana_principal)
        self.__dialogo.grab_set()
        self.__ventana_principal.wait_window(self.__dialogo)


if __name__ == "__main__":
    app = Aplicacion()
