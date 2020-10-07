import unittest
from hw04 import getRepo, getCommit
from unittest import mock


class Mock_TestgetInfo(unittest.TestCase):
    @mock.patch('hw04.getRepo')
    def mocktest_get_repo_01(self,mocktest_get_repo_name):
        mocktest_get_repo_name.return_value = ['Annie', 'birthday', 'hw04','ssw567', 'Student-Repository', 'Triangle567'] 
        expectresult = ['Annie', 'birthday', 'hw04','ssw567', 'Student-Repository', 'Triangle567'] 
        self.assertEqual(getRepo('dchen810'), expectresult)
        self.assertEqual(getRepo('dchen810'), expectresult)

    @mock.patch('hw04.getCommit')
    def test_get_commit_01(self,mocktest_get_commit):
        mocktest_get_commit.return_value = 2
        name = 'dchen810'
        self.assertEqual( getCommit(name, 'Annie'), 2)
        mocktest_get_commit.return_value = 1
        self.assertEqual( getCommit(name, 'birthday'), 1)
        mocktest_get_commit.return_value = 12
        self.assertEqual( getCommit(name, 'hw04'), 12)
        mocktest_get_commit.return_value = 4
        self.assertEqual( getCommit(name, 'ssw567'), 4)
        mocktest_get_commit.return_value = 7
        self.assertEqual( getCommit(name, 'Student-Repository'), 7)
        mocktest_get_commit.return_value = 4
        self.assertEqual( getCommit(name, 'Triangle567'), 4)


if __name__ == '__main__':
    unittest.main(exit = False, verbosity = 2)