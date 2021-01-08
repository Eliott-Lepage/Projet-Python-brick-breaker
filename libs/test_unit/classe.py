import unittest
import mvp
import shutil
from os import listdir
from os.path import isfile, join
import os


class GuiTestCase(unittest.TestCase):
    def test_level(self):
        self.assertEqual(mvp.display_console("test123"), "File not found !")

    def test_file(self):
        list_files = list()
        files = [f for f in listdir("data") if isfile(join("data", f))]
        for i in files:
            if i[:6] == "level_":
                list_files.append(i)

        for elem in list_files:
            shutil.copy(elem, "test_" + elem)
            try:
                with open("data/" + str("test_" + elem), "w") as file:
                    for line in file:
                        line += "pkfzep"

            except FileNotFoundError:
                print('Fichier introuvable.')
            except IOError:
                print('Erreur IO.')

            error_list = list()
            try:
                with open("data/" + str("test_" + elem), "r") as file:
                    ok = True
                    for line in file:
                        true_characters = ["1", "2", "3", "4", "5", "6", "7", "8", "-", "v"]
                        dt = line.rstrip()
                        dt_replace = dt.replace(" ", "")

                        matched_list = [characters in true_characters for characters in dt_replace]
                        if False in matched_list:
                            ok = False
                            break
                        else:
                            continue
                    error_list.append(ok)

            except FileNotFoundError:
                print('Fichier introuvable.')
            except IOError:
                print('Erreur IO.')

            # Test if the list contains the boolean False / then there is a mistake
            if False in error_list:
                result = False
            else:
                result = True

        list_files_copy = list()
        files = [f for f in listdir("data") if isfile(join("data", f))]
        for i in files:
            if i[:6] == "test_":
                list_files_copy.append(i)

        for elem in list_files:
            os.remove("data/" + elem)
        message = "A change has been made! Please restore the file (s) to their default state"
        self.assertEqual(False, result, message)