import unittest
import os
import sys
from unittest.mock import patch, MagicMock
from io import StringIO
from api import UserInterface
from api_classes import NewsAPI, Repository, UnitOfWork, History

class TestNewsAPI(unittest.TestCase):
    def setUp(self):
        self.api = NewsAPI("test_key")

    @patch('api_classes.requests.get')
    def test_get_top_headlines(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"articles": []}
        mock_get.return_value = mock_response

        result = self.api.get_top_headlines()
        self.assertEqual(result, {"articles": []})

    @patch('api_classes.requests.get')
    def test_search_news(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"articles": []}
        mock_get.return_value = mock_response

        result = self.api.search_news("test")
        self.assertEqual(result, {"articles": []})

    @patch('api_classes.requests.get')
    def test_make_request_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        with self.assertRaises(Exception):
            self.api._make_request("http://test.com")

class TestRepository(unittest.TestCase):
    def test_add_and_get_all(self):
        repo = Repository()
        repo.add("item1")
        repo.add("item2")
        self.assertEqual(repo.get_all(), ["item1", "item2"])

class TestUnitOfWork(unittest.TestCase):
    def test_commit(self):
        uow = UnitOfWork()
        uow.commit()  # Цей метод нічого не робить, тому просто перевіряємо, що він не викликає помилок

class TestHistory(unittest.TestCase):
    def test_add_query_and_display(self):
        history = History()
        history.add_query("test query", 5)
        
        with patch('builtins.print') as mock_print:
            history.display()
            mock_print.assert_called()

class TestAPIUserInterface(unittest.TestCase):
    def test_init(self):
        api = MagicMock()
        ui = APIUserInterface(api)
        self.assertIsInstance(ui.uow, UnitOfWork)
        self.assertIsInstance(ui.history, History)

class TestUserInterface(unittest.TestCase):
    def setUp(self):
        self.api = MagicMock()
        self.ui = UserInterface(self.api)

    @patch('builtins.print')
    def test_display_articles(self, mock_print):
        articles = [
            {"title": "Test Title", "description": "Test Description"}
        ]
        self.ui.display_articles(articles)
        mock_print.assert_called()

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_save_to_file_json(self, mock_open):
        data = [{"title": "Test", "description": "Test Desc"}]
        self.ui.save_to_file(data, "test.json", "json")
        mock_open.assert_called_with("test.json", "w")

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_save_to_file_csv(self, mock_open):
        data = [{"title": "Test", "description": "Test Desc"}]
        self.ui.save_to_file(data, "test.csv", "csv")
        mock_open.assert_called_with("test.csv", "w", newline='')

    @patch('builtins.input', return_value="test")
    def test_search_news(self, mock_input):
        self.api.search_news.return_value = {"articles": []}
        with patch.object(self.ui, 'display_articles') as mock_display:
            self.ui.search_news()
            mock_display.assert_called_with([])

    @patch('builtins.input', return_value="ua")
    def test_get_top_headlines(self, mock_input):
        self.api.get_top_headlines.return_value = {"articles": []}
        with patch.object(self.ui, 'display_articles') as mock_display:
            self.ui.get_top_headlines()
            mock_display.assert_called_with([])

    @patch('builtins.input', return_value="1")
    def test_change_title_color(self, mock_input):
        self.ui.change_title_color()
        self.assertEqual(self.ui.title_color, "\033[31m")

    @patch('builtins.input', side_effect=["1", "6"])
    def test_run(self, mock_input):
        with patch.object(self.ui, 'search_news') as mock_search:
            self.ui.run()
            mock_search.assert_called_once()

if __name__ == '__main__':
    unittest.main()