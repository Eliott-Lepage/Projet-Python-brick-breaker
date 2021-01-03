from libs.fenetre.classe import Window
from mvp import display_console
import sys

'''Program developed on the basis of the game Brick Breaker. To run the program, the user must type this command
 in a terminal: python main.py <parameter>
- The parameter must be "console" to launch the program in MVP
- The parameter must be "GUI" to launch the program in graphical interface

Projet Python EPHEC Janvier 2021
Groupe 2TM1-2
03/01/21

@:param argv[1] is used to determine the version of the game ( MVP or GUI )
@:type string

TEST

'''

__author__ = "Mathis Dory, Eliott Lepage"
__version__ = "1.0.0"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "GUI":
            gui = Window()
            gui.window.mainloop()
        elif sys.argv[1] == "console":
            display_console()
        else:
            print("Introduisez console pour lancer en mode MVP\nIntroduisez GUI pour lancer en GUI")
    else:
        print("Le programme nécessite 1 paramètre: console ou GUI !")
