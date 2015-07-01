import unittest
from Source.Exercises import Exercises

class ExerciseTests(unittest.TestCase):
    def test_GetPrintStatement(self):
        exercises = Exercises()
        self.assertEqual("Hello World!", exercises.GetPrintStatement("Hello World!"))