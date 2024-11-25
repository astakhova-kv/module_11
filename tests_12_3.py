import unittest
import logging
from HMT_2 import Runner, Tournament


logging.basicConfig(level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s: %(message)s')


def check_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        else:
            return test_func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @check_frozen
    def test_walk(self):
        try:
            runner = Runner("Alice", -5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)

    @check_frozen
    def test_run(self):
        try:
            runner = Runner(123, 10)  # Некорректное имя
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @check_frozen
    def test_first_tournament(self):
        runner1 = Runner("Alice", 10)
        runner2 = Runner("Bob", 5)
        tournament = Tournament(50, runner1, runner2)
        results = tournament.start()
        self.assertEqual(results[1], runner1)
        self.assertEqual(results[2], runner2)

    @check_frozen
    def test_second_tournament(self):
        runner1 = Runner("Alice", 10)
        runner2 = Runner("Bob", 5)
        runner3 = Runner("Charlie", 8)
        tournament = Tournament(80, runner1, runner2, runner3)
        results = tournament.start()
        self.assertEqual(results[1], runner1)

    @check_frozen
    def test_third_tournament(self):
        runner = Runner("Solo", 10)
        tournament = Tournament(100, runner)
        results = tournament.start()
        self.assertEqual(results[1], runner)