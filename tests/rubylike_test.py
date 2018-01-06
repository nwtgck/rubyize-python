import unittest
import rubylike

class RubylikeTest(unittest.TestCase):
  assert(rubylike.hello() == "hello, world")
  # TODO impl


def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(RubylikeTest))
  return suite