import unittest

import spider_poker as sp


class PokerSpider(unittest.TestCase):
    def test_random_position(self):
        print sp.random_position()

    def test_load_resource(self):
        dir_path = "data\\pukeImage"
        self.poker_resource = sp.PokerSource(dir_path)
        ret = self.poker_resource.load_resource()
        self.assertEqual(True, ret)
        print self.poker_resource.path_list


if __name__ == '__main__':
    unittest.main()
