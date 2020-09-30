import unittest
from hw04 import getRepo, getCommit


class TestgetInfo(unittest.TestCase):
    def test_get_repo_01(self):
        expectresult = ['Annie', 'birthday', 'ssw567', 'Student-Repository', 'Triangle567'] 
        self.assertEqual(getRepo('dchen810'), expectresult)
        self.assertEqual(getRepo('dchen810'), expectresult)


    def test_get_commit_01(self):
        name = 'dchen810'
        self.assertEqual( getCommit(name, 'Annie'), 2)
        self.assertEqual( getCommit(name, 'birthday'), 1)
        self.assertEqual( getCommit(name, 'ssw567'), 4)
        self.assertEqual( getCommit(name, 'Student-Repository'), 7)
        self.assertEqual( getCommit(name, 'Triangle567'), 4)


if __name__ == '__main__':
    unittest.main(exit = False, verbosity = 2)
