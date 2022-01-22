import unittest
import sity
class Test(unittest.TestCase):
    def test (self):
        format=sity.siti('МСК','РОССИЯ')
        self.assertEqual(format,'мскросси')
unittest.main()