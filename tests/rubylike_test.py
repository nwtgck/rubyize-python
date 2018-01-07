import unittest
import rubyize

class RubyizeTest(unittest.TestCase):

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
    actual = [1, 2, 3].map(lambda x: x*2)
    expect = [2, 4, 6]
    self.assertEqual(actual, expect)

  def test_list_filter(self):
    """
    Test of list#filter
    """
    actual = [1, 2, 3].filter(lambda x: x % 2 == 0)
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
    Test of list#take
    """
    actual = [1, 2, 3].take(2)
    expect = [1, 2]
    self.assertEqual(actual, expect)

  def test_list_drop(self):
    """
    Test of list#drop
    """
    actual = [1, 2, 3].drop(2)
    expect = [3]
    self.assertEqual(actual, expect)

  def test_list_group_by(self):
    """
    Test of list#group_by
    """
    actual = [1, 2, 3, 4, 5, 6].group_by(lambda e: e % 2 == 0)
    expect = {True: [2, 4, 6], False: [1, 3, 5]}
    self.assertEqual(actual, expect)

  def test_list_compact(self):
      """
      Test of list#compact
      """
      actual = [1, 2, None, 4, None, 6].compact()
      expect = [1, 2, 4, 6]
      self.assertEqual(actual, expect)

  def test_list_to_iter(self):
      """
      Test of list#to_iter
      """
      itr = [1, 2, 3, 4, 5].to_iter()
      for actual, expect in zip(itr, [1, 2, 3, 4, 5]):
        self.assertEqual(actual, expect)

  def test_list_flat_map(self):
    """
        Test of list#flat_map
        """
    actual = [1, 2, 3].flat_map(lambda e: [e] * 2)
    expect = [1, 1, 2, 2, 3, 3]
    self.assertEqual(actual, expect)

  def test_list_each_cons(self):
    """
        Test of list#flat_each_cons
        """
    actual = [1, 2, 3, 4, 5].each_cons(3)
    expect = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    self.assertEqual(actual, expect)

    actual = [1, 2, 3, 4, 5].each_cons(6)
    expect = []
    self.assertEqual(actual, expect)


  def test_list_each_slice(self):
    """
        Test of list#flat_each_slice
        """
    actual = [1, 2, 3, 4, 5].each_slice(2)
    expect = [[1, 2], [3, 4], [5]]
    self.assertEqual(actual, expect)

    actual = [1, 2, 3, 4, 5, 6].each_slice(2)
    expect = [[1, 2], [3, 4], [5, 6]]
    self.assertEqual(actual, expect)

    actual = [1].each_slice(2)
    expect = [[1]]
    self.assertEqual(actual, expect)

    actual = [].each_slice(2)
    expect = []
    self.assertEqual(actual, expect)



  def test_map_map(self):
    """
    Test of map#map
    """
    mapped = map(lambda e: e, [1, 2, 3]).map(lambda x: x * 2)
    for actual, expect in zip(mapped, [2, 4, 6]):
      self.assertEqual(actual, expect)


  # TODO: Test other classes not only <class 'list'>

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(RubyizeTest))
  return suite