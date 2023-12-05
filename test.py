import unittest

from main import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.t = Trie()

    def test_insert_and_search(self):
        words_to_insert = ["apple", "banana", "cherry", "dog", "cat"]
        for word in words_to_insert:
            self.t.insert(word)

        self.assertTrue(self.t.search("apple"))
        self.assertTrue(self.t.search("banana"))
        self.assertTrue(self.t.search("cherry"))
        self.assertTrue(self.t.search("dog"))
        self.assertTrue(self.t.search("cat"))

    def test_search_non_existent_keys(self):
        self.assertFalse(self.t.search("grape"))
        self.assertFalse(self.t.search("elephant"))
        self.assertFalse(self.t.search("xylophone"))

    def test_search_prefix(self):
        self.assertFalse(self.t.searchPrefix("ap"))
        self.assertFalse(self.t.searchPrefix("ban"))
        self.assertFalse(self.t.searchPrefix("che"))
        self.assertFalse(self.t.searchPrefix("do"))
        self.assertFalse(self.t.searchPrefix("ca"))
        self.assertFalse(self.t.searchPrefix("xy"))

    def test_case_insensitive_keys(self):
        t_case_insensitive = Trie()
        words_case_insensitive = ["Apple", "Banana", "Cherry", "Dog", "Cat"]
        for word in words_case_insensitive:
            t_case_insensitive.insert(word.lower())

        self.assertTrue(t_case_insensitive.search("apple"))
        self.assertTrue(t_case_insensitive.search("Banana"))
        self.assertTrue(t_case_insensitive.search("ChErRy"))
        self.assertTrue(t_case_insensitive.search("dog"))
        self.assertTrue(t_case_insensitive.search("CAT"))


if __name__ == '__main__':
    unittest.main()
