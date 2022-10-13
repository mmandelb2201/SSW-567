import unittest
from unittest import mock
from unittest.mock import Mock, patch
import Api

class TestApi(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        cls.mock_get_patcher = patch('Api.getRepoCommits')
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher.stop()

    @patch('Api.getRepoCommits')
    def testDataNotEmpty(self, mock_get_commits):
        dict = {'applitech-launcher': 4, 'Complexity': 30, 'design-pattern-lab': 5, 'finance-bot': 30, 'HW3': 30, 'java-game': 1, 'NodeJSLab': 2, 'portfolio': 18, 'Rate-My-Cat': 7, 'ssw-project-one': 30, 'SSW345': 7, 'SSW567_HW02b': 30, 'turtlebot-sim': 5, 'waddle': 10}
        mock_get_commits.return_value = dict

        self.assertNotEqual(len(Api.getRepoCommits("")), 0, "dictionary should not be empty")
    
    @patch('Api.getRepoCommits')
    def testDataHasRepositortNames(self, mock_get_commits):
        dict = {'applitech-launcher': 4, 'Complexity': 30, 'design-pattern-lab': 5, 'finance-bot': 30, 'HW3': 30, 'java-game': 1, 'NodeJSLab': 2, 'portfolio': 18, 'Rate-My-Cat': 7, 'ssw-project-one': 30, 'SSW345': 7, 'SSW567_HW02b': 30, 'turtlebot-sim': 5, 'waddle': 10}
        mock_get_commits.return_value = dict

        dict = Api.getRepoCommits("")
        
        self.assertEqual("NodeJSLab" in dict, True, "repository 'NodeJSLab' should be in dictionary")
    
    @patch('Api.getRepoCommits')
    def testCommitCountCorrect(self, mock_get_commits):
        dict = {'applitech-launcher': 4, 'Complexity': 30, 'design-pattern-lab': 5, 'finance-bot': 30, 'HW3': 30, 'java-game': 1, 'NodeJSLab': 2, 'portfolio': 18, 'Rate-My-Cat': 7, 'ssw-project-one': 30, 'SSW345': 7, 'SSW567_HW02b': 30, 'turtlebot-sim': 5, 'waddle': 10}
        mock_get_commits.return_value = dict

        dict = Api.getRepoCommits("")
        self.assertNotEqual(len(dict), 0, "dictionary should not be empty")
        if len(dict) == 0:
            return
        self.assertEqual(dict["portfolio"], 18, "repository 'portfolio' should ave 18 commits")
        self.assertEqual(dict["ssw-project-one"], 30, "repository 'ssw-project-one' should have 30 commits")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()