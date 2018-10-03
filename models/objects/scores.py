"""
Module to handle data about the scores
"""


class Scores:
    def __init__(self, *args):
        self.user_id = None
        self.excellence = args[0]
        self.passion = args[1]
        self.integrity = args[2]
        self.collaboration = args[3]