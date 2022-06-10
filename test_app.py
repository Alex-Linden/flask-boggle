from unittest import TestCase

from app import app, games

from pdb import set_trace

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            html = response.get_data(as_text=True)

            # set_trace()

            self.assertEqual(response.status_code, 200)
            self.assertIn('boggle homepage', html)
            #self.assertIn('<button class="word-input-btn">Go</button>', html)
            #original test before review
            # test that you're getting a template

    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:
            ...
            response = client.post("/api/new-game")
            gameboard = response.get_data(as_text=True)
            print(gameboard)
            # set_trace()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.is_json, True)
            self.assertIn("gameId", gameboard)
