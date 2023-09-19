import unittest

from mood_analyser import MoodAnalyser

class TestMoodAnalyser(unittest.TestCase):
    def setUp(self) -> None:
        self.analyser = MoodAnalyser()

    def test_fun_mood(self):
        self.assertEqual(self.analyser.mood_analyser('У меня веселое настроение'), 'веселое')

    def test_sad_mood(self):
        self.assertEqual(self.analyser.mood_analyser('У меня грустное настроение'), 'грустное')

    def test_happy_mood(self):
        self.assertEqual(self.analyser.mood_analyser('Я счастлив'), 'счастливое')

    def test_unknown_mood(self):
        self.assertEqual(self.analyser.mood_analyser('меня зовут Петя'), 'Я не разобрал Ваше настроение')

if __name__ == "__main__":
    unittest.main()