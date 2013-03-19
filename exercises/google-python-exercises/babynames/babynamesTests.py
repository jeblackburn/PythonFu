'''
Created on Mar 18, 2013

@author: jblackburn
'''
import unittest
import babynames


class Test(unittest.TestCase):


    def testReadNames(self):
        result = babynames.extract_names("baby1990.html")
        self.assertEqual(2001, len(result), "Should find (999 * 2) baby names plus the year, got {}".format(len(result)))
        self.assertEqual("1990", result[0], "First element should be the year")

    def testNamesAreSorted(self):
        result = babynames.extract_names("baby1992.html")
        for idx in range(2, 2001):
            self.assertTrue(result[idx - 1] < result[idx], "Not sorted in alpha order: {} >= {}".format(result[idx - 1], result[idx]))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testReadNames']
    unittest.main()