import unittest

from main import peak_length


class TestFunc(unittest.TestCase):
    def test_empty_array(self):
        arr = [1, 1, 1]
        result = peak_length(arr)
        self.assertIsNone(result)

    def test_single_peak(self):
        arr = [1, 7, 2]
        result = peak_length(arr)
        self.assertEqual(result, 3)

    def test_multiple_peaks(self):
        arr = [1, 3, 5, 4, 2, 8, 3, 7, 9, 5]
        result = peak_length(arr)
        self.assertEqual(result, 6)

    def test_uneven_peaks(self):
        arr = [3, 4, 6, 4, 1, 2, 3, 4, 5, 3]
        result = peak_length(arr)
        self.assertEqual(result, 6)

    def test_no_peaks(self):
        arr = [1, 2, 3, 4, 5]
        result = peak_length(arr)
        self.assertIsNone(result)

    def test_2_element(self):
        arr = [1, 2]
        result = peak_length(arr)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
