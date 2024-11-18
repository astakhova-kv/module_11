import HumanMoveTest
import unittest

class RunnerTest(unittest.TestCase):


    def test_walk(self):
        r1 = HumanMoveTest.Runner('Name1')
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance,50)

    def test_run(self):
        r2 = HumanMoveTest.Runner('Name2')
        for i in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)

    def test_challenge(self):
        r3 = HumanMoveTest.Runner('Name3')
        r4 = HumanMoveTest.Runner('Name4')
        for i in range(10):
            r4.walk()
        for i in range(10):
            r3.run()
        self.assertNotEqual(r3.distance, r4.distance)

if __name__ == '__main__':
    unittest.main()