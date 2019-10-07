import unittest

import spider_poker as sp


class PokerSpider(unittest.TestCase):
    def test_random_position(self):
        self.assertNotEqual(sp.random_position(), sp.random_position())

    def test_load_resource(self):
        dir_path = "data\\pukeImage"
        path_list = sp.load_resource(dir_path)
        print path_list
        self.assertNotEqual(len(dir_path), 0)


if __name__ == '__main__':
    unittest.main()
