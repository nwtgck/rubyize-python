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

  def test_list_inject(self):
    """
    Test of list#inject
    """
    actual = [1, 2, 3].inject(lambda s, e: s + e)
    expect = 6
    self.assertEqual(actual, expect)
    actual = [1, 2, 3].inject(100, lambda s, e: s + e)
    expect = 106
    self.assertEqual(actual, expect)

  def test_list_take(self):
    """
    Test of list#inject
    """
    actual = [1, 2, 3].take(2)
    expect = [1, 2]
    self.assertEqual(actual, expect)

  def test_list_drop(self):
    """
    Test of list#inject
    """
    actual = [1, 2, 3].drop(2)
    expect = [3]
    self.assertEqual(actual, expect)


def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(RubylikeTest))
  return suite