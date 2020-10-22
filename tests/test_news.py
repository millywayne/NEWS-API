import unittest
from app.models import News

class   NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.latest_news = News("Disjointed Covid-19 Apps Across U.S. Raise Questions About Tech's Role - The Wall Street Journal","The lack of a national plan on contact tracing has resulted in a state-by-state patchwork of differing technological tools","https://www.wsj.com/articles/disjointed-covid-19-apps-across-u-s-raise-questions-about-techs-role-11603272613","https://images.wsj.net/im-247417/social")

    def test_instance(self):
        self.assertTrue(isinstance(self.latest_news,News))