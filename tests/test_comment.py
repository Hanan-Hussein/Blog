import unittest
from app.models import Comments



class TestComment(unittest.TestCase):
    """
    The test for the comment class

    Args:
        unittest : The unittest
    """
    def setUp(self):
        """
        This is the set up that runs before the test
        """
        self.new_comment= Comments("Good work"

        )
        
    def test_user_source_(self):
        """
        Test if the instance created by article class
        """
        self.assertTrue(isinstance(self.new_comment,Comments))
        
if __name__ == '__main__':
    unittest.main()