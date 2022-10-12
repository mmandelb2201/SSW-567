import unittest
from Api import getRepoCommits

class TestApi(unittest.TestCase):
    def testDataNotEmpty(self):
        self.assertNotEqual(len(getRepoCommits("mmandelb2201")), 0, "dictionary should not be empty")

    def testDataHasRepositortNames(self):
        dict = getRepoCommits("mmandelb2201")
        self.assertEqual(dict.has_key("NodeJSLab"), True, "repository 'NodeJSLab' should be in dictionary")

    def testCommitCountCorrect(self):
        dict = getRepoCommits("mmandelb2201")
        self.assertNotEqual(len(dict), 0, "dictionary should not be empty")
        if len(dict) == 0:
            return
        self.assertEqual(dict["portfolio"], 18, "repository 'portfolio' should ave 18 commits")
        self.assertEqual(dict["ssw-project-one"], 30, "repository 'ssw-project-one' should have 30 commits")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()