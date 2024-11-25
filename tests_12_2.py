from HMT_2 import Runner, Tournament
import unittest
class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)
    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)
    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        TournamentTest.all_results['usain_and_nick'] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")
    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results['andrey_and_nick'] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")
    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results['usain_andrey_and_nick'] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")
if __name__ == '__main__':
    unittest.main()