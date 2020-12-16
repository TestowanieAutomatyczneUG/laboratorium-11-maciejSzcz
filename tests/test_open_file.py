# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from unittest.mock import mock_open, patch, MagicMock
from unittest import mock
from src.zad1.open_file import OpenFile


class TestOpenFile(unittest.TestCase):
    def setUp(self):
        self.temp = OpenFile()

    def test_OpenFile_read(self):
        open_test = mock_open(read_data="tutaj jest tekst")
        path = 'zadanko.txt'

        with patch('builtins.open', open_test):
            self.assertEqual("tutaj jest tekst", self.temp.read(path))

    def test_OpenFile_write(self):
        open_test = mock_open(read_data="tutaj jest tekst")
        path = 'zadanko.txt'

        with patch('builtins.open', open_test):
            self.temp.write(path, "To jest inny tekst niz wczesniej")

        open_test.assert_called_once_with(path, 'w+')

    @mock.patch('src.zad1.open_file.os')
    def test_OpenFile_delete_file_exists(self, mock_os):
        path = 'zadanko.txt'
        mock_os.path = MagicMock()
        mock_os.path.exists.return_value = True
        
        self.temp.delete(path)

        mock_os.remove.assert_called_with(path)

    @mock.patch('src.zad1.open_file.os')
    def test_OpenFile_delete_file_doesnt_exist(self, mock_os):
        path = 'zadanko.txt'
        mock_os.path = MagicMock()
        mock_os.path.exists.return_value = False

        self.assertRaises(IOError, self.temp.delete, path)



if __name__ == '__main__':
    unittest.main()
