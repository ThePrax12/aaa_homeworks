import unittest
import json
from unittest.mock import patch
from what_is_year_now import what_is_year_now


class TestWhatIsYearNow(unittest.TestCase):

    @patch("urllib.request.urlopen")
    def test_valid_ymd_format(self, mock_urlopen):
        """
        Тестирует корректную работу функции для формата даты YYYY-MM-DD.
        Ожидается, что функция вернет правильный год из строки в формате '2019-03-01T12:34:56Z'.
        """
        mock_response = {"currentDateTime": "2019-03-01T12:34:56Z"}
        mock_urlopen.return_value.__enter__.return_value.read.return_value = json.dumps(
            mock_response
        ).encode("utf-8")

        self.assertEqual(what_is_year_now(), 2019)

    @patch("urllib.request.urlopen")
    def test_valid_dmy_format(self, mock_urlopen):
        """
        Тестирует корректную работу функции для формата даты DD.MM.YYYY.
        Ожидается, что функция вернет правильный год из строки в формате '01.03.2019T12:34:56Z'.
        """
        mock_response = {"currentDateTime": "01.03.2019T12:34:56Z"}
        mock_urlopen.return_value.__enter__.return_value.read.return_value = json.dumps(
            mock_response
        ).encode("utf-8")

        self.assertEqual(what_is_year_now(), 2019)

    @patch("urllib.request.urlopen")
    def test_invalid_date_format(self, mock_urlopen):
        """
        Тестирует обработку неверного формата даты.
        Ожидается, что при получении даты в формате '2019/03/01T12:34:56Z'
        будет выброшено исключение ValueError.
        """

        mock_response = {"currentDateTime": "2019/03/01T12:34:56Z"}
        mock_urlopen.return_value.__enter__.return_value.read.return_value = json.dumps(
            mock_response
        ).encode("utf-8")

        with self.assertRaises(ValueError):
            what_is_year_now()

    @patch("urllib.request.urlopen")
    def test_missing_current_datetime_field(self, mock_urlopen):
        """
        Тестирует ситуацию, когда в ответе от API отсутствует поле 'currentDateTime'.
        Ожидается, что при отсутствии этого поля будет выброшено исключение KeyError.
        """
        mock_response = {}
        mock_urlopen.return_value.__enter__.return_value.read.return_value = json.dumps(
            mock_response
        ).encode("utf-8")

        with self.assertRaises(KeyError):
            what_is_year_now()

    @patch("urllib.request.urlopen")
    def test_network_error(self, mock_urlopen):
        """
        Тестирует обработку сетевой ошибки, когда API не доступно.
        Ожидается, что будет выброшено исключение URLError.
        """
        mock_urlopen.side_effect = Exception("Network Error")

        with self.assertRaises(Exception):
            what_is_year_now()


if __name__ == "__main__":
    unittest.main()
