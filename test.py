## A simple unit test example. Replace by your own tests
from __future__ import print_function
from __future__ import division
import sys
import unittest
import a1ece650

class MyTest(unittest.TestCase):

    def test_1(self):
        
        #Test for checking intersection of two lines
        result = a1ece650.intersect((0, 0), (3, 3), (3, 0), (0, 3))
        self.assertEqual(result, [(1.5, 1.5)])

    def test_2(self):
        #Test for Checking out the interval
        result = a1ece650.intersect((0, 5), (5, 5), (0, 0), (6, 5))
        self.assertEqual(result, [])
    
    def test_3(self):
        #Test for Endpoint checking
        result = a1ece650.intersect((0, 5), (5, 5), (0,0), (5, 5))
        self.assertEqual(result, [(5.0, 5.0)])

    def test_4(self):
        #Test for Checking overlapping lines
        result = a1ece650.intersect((0, 0), (5, 5), (-1,-1), (6, 6))
        self.assertEqual(result, [(0,0),(5,5)])



    def test_5(self):
        # Test for valid input
        string = '"King St West" (1,2)(2,3) (5,6)'
        result = a1ece650.parse(string, '')
        self.assertEqual(result, ['king st west', [(1,2),(2,3),(5,6)]])

    def test_6(self):
        # Test for empty input with only street name
        string = '"King St West"'
        result = a1ece650.parse(string, '')
        self.assertEqual(result, ['king st west', None])



    def test_7(self):
        #Test for missing parentheses
        string = '"King St West" (1,2)(2,3) 5,6)'
        result = a1ece650.parse(string, '')
        self.assertEqual(result, False)
    
    def test_8(self):
        #Invalid Cordinates test
        string = '"King St West" (12)(2,3)(5,6)'
        result = a1ece650.parse(string, '')
        self.assertEqual(result, False)
    
    def test_9(self):
        #Invalid Cordinates test
        string = '"King St West" (1,2,3)(2,3)(5,6)'
        result = a1ece650.parse(string, '')
        self.assertEqual(result, False)

    def test_10(self):
        #Invalid Street name test
        string = '"King St-West" (1,3)(2,3)(5,6)'
        result = a1ece650.parse(string, '')
        self.assertEqual(result, False)

    def test_11(self):
        #Invalid Character in vertices test
        string = '"King St West" (1.0,3)(2,3)(5,6)'
        result = a1ece650.parse(string, '')
        self.assertEqual(result, False)

    def test_12(self):
        #missing quote test
        string = '"King St West (1,3)(2,3)(5,6)'
        result = a1ece650.parse(string, '')
        self.assertEqual(result, False)

    def test_13(self):
        #basic intersection test
        graph = a1ece650.Graph()
        graph.add_street('King', [(0,0), (4,4)])
        graph.add_street('Weber', [(0,4), (4,0)])
        graph.render_graph()
        result = set(graph.vertices.keys())
        expected = { (0,0), (4,4), (0,4), (4,0), (2,2) }
        print(graph)
        self.assertEqual(result, expected)

    def test_14(self):
        #Test for vertical overlapping intersection
        graph = a1ece650.Graph()
        graph.add_street('King', [(-1,0), (-1,5)])
        graph.add_street('Weber', [(-1,2), (-1,7)])
        graph.render_graph()
        result = set(graph.vertices.keys())
        expected = { (-1,0), (-1,5), (-1,2), (-1,7) }
        print(graph)
        self.assertEqual(result, expected)

    def test_15(self):
        #Complete overlap of intersection test
        graph = a1ece650.Graph()
        graph.add_street('King', [(-3,5), (2,0)])
        graph.add_street('Weber', [(-1,3), (1,1)])
        graph.render_graph()
        result = set(graph.vertices.keys())
        expected = { (2,0), (-1,3), (1,1), (-3,5) }
        print(graph)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()




