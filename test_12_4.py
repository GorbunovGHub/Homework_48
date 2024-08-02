import unittest
import rt_with_exceptions
import logging


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            object_runner = rt_with_exceptions.Runner('Alex', -50)
            for i in range(10):
                object_runner.walk()
            self.assertEqual(object_runner.distance, 50)
            logging.info(f'"test_walk" выполнен успешно {object_runner}')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            object_runner = rt_with_exceptions.Runner(404, 50)
            for i in range(10):
                object_runner.run()
            self.assertEqual(object_runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
            return 0

    def test_challenge(self):
        object_runner_1 = rt_with_exceptions.Runner('Paul')
        object_runner_2 = rt_with_exceptions.Runner('Dominik')
        for i in range(10):
            object_runner_1.walk()
            object_runner_2.run()
        self.assertNotEqual(object_runner_1.distance, object_runner_2.distance)


logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests.log', encoding='UTF-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")
