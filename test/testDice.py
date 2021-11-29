import unittest
from io import StringIO

from hamcrest import *
from unittest.mock import patch
from Dice import Dice


class TestDice(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def testLancer(self, reponse):
        with patch('builtins.input', reponse="o"):
            dice = Dice().lancer()
            self.assertTrue(1 <= dice <= 6)
