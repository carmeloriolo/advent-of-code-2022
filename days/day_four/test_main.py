from unittest import TestCase

from days.day_four.main import fully_contained


class Test(TestCase):
    def test_fully_contained(self):
        self.assertFalse(fully_contained([2, 4], [6, 8]))
        self.assertFalse(fully_contained([2, 3], [4, 5]))
        self.assertFalse(fully_contained([5, 7], [7, 9]))
        self.assertTrue(fully_contained([2, 8], [3, 7]))
        self.assertTrue(fully_contained([6, 6], [4, 6]))
        self.assertFalse(fully_contained([2, 6], [4, 8]))
