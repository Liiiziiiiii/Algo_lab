import unittest

from src.main import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_isReachable_all_connected(self):
        pipelines = [['A', 'B'], ['B', 'C'], ['C', 'D']]
        cities = ['A', 'B', 'C', 'D']
        gas = ['GasStorage1', 'GasStorage2']
        result = self.graph.isReachable(pipelines, cities, gas)
        self.assertEqual(result, False)

    def test_isReachable_some_unreachable(self):
        pipelines = [['A', 'B'], ['B', 'C']]
        cities = ['A', 'B', 'C', 'D']
        gas = ['GasStorage1', 'GasStorage2']
        result = self.graph.isReachable(pipelines, cities, gas)
        expected = {'GasStorage1': ['D'], 'GasStorage2': ['D']}
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()
