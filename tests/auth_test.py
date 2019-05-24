import os
import unittest
import models.db as db
from datetime import datetime
from models.professor_logic import Professor_logic as Professor_wrapper

class TestCommon(unittest.TestCase):

    def setUp(self):
        file = open(os.path.dirname(__file__) + '/prepare_for_test.pgsql', "r")
        text = ""
        for line in file:
            text = text + line
        db.engine.execute(text)

    def test_signup(self): 
        professor = Professor_wrapper()
        professor.sign_up("Test name", 1, "test_email@gmail.com", "test_password", "test_password")
        session = db.Session()
        profesor_list = session.query(db.Professor).all()
        self.assertTrue(len(profesor_list) == 1)
    
    def test_signin(self): 
        professor = Professor_wrapper()
        professor.sign_up("Test name", 1, "test_email@gmail.com", "test_password", "test_password")
        professor.professor = None #sign out emulation
        professor.sign_in("test_email@gmail.com", "test_password")
        self.assertTrue(professor.professor != None)

    def test_publish(self):
        professor = Professor_wrapper()
        professor.sign_up("Test name", 1, "test_email@gmail.com", "test_password", "test_password")
        professor.publish_diploma("test_thesis", "test_description", datetime.now(), True, "testing")
        session = db.Session()
        profesor_list = session.query(db.Diploma).all()
        self.assertTrue(len(profesor_list) == 1)

    def test_estimate(self):
        professor = Professor_wrapper()
        professor.sign_up("Test name", 1, "test_email@gmail.com", "test_password", "test_password")
        professor.publish_diploma("test_thesis", "test_description", datetime.now(), True, "testing")
        professor.professor.is_expert = True
        professor.estimate_diploma(4, 5, 3, 5, 1)
        session = db.Session()
        profesor_list = session.query(db.Criterion).all()
        self.assertTrue(len(profesor_list) == 1)

if __name__ == '__main__':
    unittest.main()