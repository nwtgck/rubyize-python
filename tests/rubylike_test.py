import unittest
import rubylike

class RubylikeTest(unittest.TestCase):

  def test_list_length(self):
    """
    Test of list#length
    """
    actual = [1, 2, 3].length()
    expect = 3
    self.assertEqual(actual, expect)


  def test_list_map(self):
    """
    Test of list#map
    """
    actual = [1, 2, 3].map(lambda x: x*2).to_list()
    expect = [2, 4, 6]
    self.assertEqual(actual, expect)

  def test_list_filter(self):
    """
    Test of list#filter
    """
    actual = [1, 2, 3].filter(lambda x: x % 2 == 0).to_list()
    expect = [2]
    self.assertEqual(actual, expect)


def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(RubylikeTest))
  return suite