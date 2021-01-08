import unittest
import mvp
import libs.brique.fonction as brick_func
from libs.balle.fonctions import set_increment_score, calcul_target


class GuiTestCase(unittest.TestCase):
    def test_level(self):
         self.assertEqual(mvp.display_console("test123"), "File not found !")

    def test_set_next_level(self):
        counter = 1
        result = brick_func.set_next_level(counter)
        self.assertEqual(result, (2, 50, 50))
        counter += 1
        result = brick_func.set_next_level(counter)
        self.assertEqual(result, (3, 50, 50))

    def test_set_score(self):
        score = 0
        self.assertEqual(set_increment_score(score), 100)

    def test_dx(self):
        dx = 50
        self.assertEqual(calcul_target(dx), -50)

