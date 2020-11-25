from libs.fenetre.classe import Window
from libs.brique.classe import Brick
from tkinter import *

if __name__ == "__main__":
    def startProgram(method="GUI"):
        if method == "GUI":
            fenetre = Window()
            fenetre.window.mainloop()
        elif method == "console":
            Brick.display_console(self="")



    # Ecrire "console" comme paramètre pour lancer en mode console.
    startProgram("console")
