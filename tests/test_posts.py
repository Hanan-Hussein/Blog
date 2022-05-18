import unittest
from app.models import Posts


class test_posts(unittest.TestCase):
    """
    The test for the post class

    Args:
        unittest : The unittest
    """
    def setUp(self):
        """
        This is the set up that runs before the test
        """
        self.new_posts = Posts("Cleanser","A proper face cleanser is important for your skin life","You should consider proper face cleaning","Fashion")
        
    def test_User_model_(self):
        """
        Test if the instance created by 
        """
        self.assertTrue(isinstance(self.new_posts,Posts))
        
if __name__ == '__main__':
    unittest.main()