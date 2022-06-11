from re import U
from unittest import TestCase

from app import app, games

from boggle import BoggleGame


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
            # print(gameboard)
            # set_trace()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.is_json, True)
            self.assertIn("gameId", gameboard)

    def test_api_score_word(self):
        """Test scoring a word"""

        with self.client as client:
            response = client.post("/api/new-game")
            gameboard = response.get_json()
            gameId = gameboard["gameId"]
            game = games[gameId]

            game.board[0] = ['C', 'A', 'T', 'X', 'X']
            game.board[1] = ['C', 'T', 'X', 'X', 'X']
            game.board[2] = ['X', 'X', 'X', 'X', 'X']
            game.board[3] = ['X', 'X', 'X', 'X', 'X']
            game.board[4] = ['X', 'X', 'X', 'X', 'X']

            resp = client.post('/api/score-word',
                json={'gameId': gameId, 'word': 'CAT'})
            json_response = resp.get_json()

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.is_json, True)
            self.assertEqual({'result': "ok"}, json_response)

            resp_not_word = client.post('/api/score-word',
                json={'gameId': gameId, 'word': 'XYZ'})
            json_response_not_word = resp_not_word.get_json()

            self.assertEqual({'result': "not-word"}, json_response_not_word)

            resp_not_board = client.post('/api/score-word',
                json={'gameId': gameId, 'word': 'QUILL'})
            json_response_not_board = resp_not_board.get_json()

            self.assertEqual({'result': "not-on-board"}, json_response_not_board)

            # not valid
            # not on board
            # okay

