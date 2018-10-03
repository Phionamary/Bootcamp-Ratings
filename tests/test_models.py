"""
Module to handle tests
"""
from unittest import TestCase

from models.score_model import ScoreModel
from models.user_model import UserModel


class TestModels(TestCase):
    """
    Class with methods to handle tests
    """

    def test_register_user(self):
        self.assertTrue(UserModel().register('Arnold','arnold@gmail.com', 'LF', 'password'), 'You have registered '
                                                                                             'successfully')

    def test_add_scores(self):
        self.assertTrue(ScoreModel().add_to_score_card(2, 1, 0, 2, -1), "Successfully Added the scores")

    def test_find_user(self):
        user = UserModel().register('Arnold', 'arnold@gmail.com', 'LF', 'password')
        print(user)
        self.assertTrue(UserModel().find_user_by_id(2), None)
