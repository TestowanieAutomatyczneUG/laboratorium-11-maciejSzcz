from unittest import TestCase, main

from src.zad3.friendships import Friendships


class TestFriendships(TestCase):
    def setUp(self):
        self.temp = Friendships()

    def test_friendships_make_friends(self):
        self.temp.make_friends("friend1", "friend2")
        self.assertEqual(self.temp.value, {"friend1": ["friend2"], "friend2": ["friend1"]})

    def test_friendships_make_friends_raises_with_int(self):
        self.assertRaises(TypeError, self.temp.make_friends, "friend1", 2)

    def test_friendships_add_friend(self):
        self.temp.add_friend("friend1", "friend2")
        self.assertEqual(self.temp.value, {"friend1": ["friend2"]})

    def test_friendships_get_friends_list(self):
        self.temp.make_friends("friend1", "friend2")
        self.temp.make_friends("friend1", "friend3")
        self.assertEqual(self.temp.get_friends_list("friend1"), ["friend2", "friend3"])

    def test_friendships_get_friends_list_raises_with_nonexistent_friend(self):
        self.assertRaises(ValueError, self.temp.get_friends_list, "friend2")

    def test_friendships_get_friends_list_raises_with_int(self):
        self.assertRaises(TypeError, self.temp.get_friends_list, 4)

    def test_friendships_are_friends_true(self):
        self.temp.make_friends("friend1", "friend2")
        self.assertEqual(self.temp.are_friends("friend1", "friend2"), True)

    def test_friendships_are_friends_false(self):
        self.temp.make_friends("friend1", "friend2")
        self.assertEqual(self.temp.are_friends("friend3", "friend2"), False)

    def test_friendships_are_friends_raises_exception_with_int(self):
        self.assertRaises(TypeError, self.temp.are_friends, 1, 43)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
