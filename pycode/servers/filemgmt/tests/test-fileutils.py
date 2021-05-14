import unittest
import os

class FileUtility(unittest.TestCase):
    def test_passwd(self):
        result = os.path.isfile('/etc/passwd')
        self.assertEqual(result, True)

    def test_gshadow(self):
        result = os.path.isfile('/etc/gshadow')
        self.assertEqual(result, True)

    def test_group(self):
        result = os.path.isfile('/etc/group')
        self.assertEqual(result, True)

    def test_shadow(self):
        result = os.path.isfile('/etc/shadow')
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
