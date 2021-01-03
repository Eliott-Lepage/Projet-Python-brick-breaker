import unittest
import mvp

class GuiTestCase(unittest.TestCase):
    def test_level(self):
        self.assertEqual(mvp.display_console("test123"), "File not found !")

