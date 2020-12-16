import unittest

from unittest.mock import mock_open, patch, MagicMock
from unittest import mock
from src.zad3.friendships_storage import FriendshipsStorage
from src.zad3.friendships import Friendships


class TestFriendshipsStorage(unittest.TestCase):
    def test_friendships_storage_add_raises_typeError_with_not_friendships(self):
        friendships_storage = FriendshipsStorage()
        friendships_storage.add = MagicMock(side_effect=TypeError)

        self.assertRaises(TypeError, friendships_storage.add, "Andrzej")
        friendships_storage.add.assert_called_with("Andrzej")
        
    def test_friendships_storage_add_note_success(self):
        friendships = Friendships()
        friendships.make_friends("anmdrej", "marek")
        friendships_storage = FriendshipsStorage()
        friendships_storage.add = MagicMock(return_value="Added Friendships succesfully")

        friendships_storage.add(friendships)
        friendships_storage.add.assert_called_once_with(friendships)


    def test_friendships_storage_clear(self):
        friendships_storage = FriendshipsStorage()
        friendships_storage.clear = MagicMock(return_value="Cleared all Friendships")

        self.assertEqual(friendships_storage.clear(), "Cleared all Friendships")
        friendships_storage.clear.assert_any_call()


    def test_friendships_storage_get_friends_of(self):
        friendships_storage = FriendshipsStorage()
        friendships_storage.get_friends_of = MagicMock(return_value=["Michał", "Adrian"])

        self.assertEqual(friendships_storage.get_friends_of("Andrzej"), ["Michał", "Adrian"])
        friendships_storage.get_friends_of.assert_called_with("Andrzej")


    def test_friendships_storage_get_friends_of_non_existent(self):
        friendships_storage = FriendshipsStorage()
        friendships_storage.get_friends_of = MagicMock(side_effect=ValueError)

        self.assertRaises(ValueError, friendships_storage.get_friends_of, "Andrzej")


if __name__ == '__main__':
    unittest.main()
