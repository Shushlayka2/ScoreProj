from datetime import datetime
import models.db as db
from models.diploma_logic import Diploma_logic as Diploma_wrapper
from models.professor_logic import Professor_logic as Professor_wrapper
from flask import Flask
import sched, time

# Checker service
def check_state():
    session = db.Session()
    diplomas = session.query(db.Diploma).all()
    for diploma in diplomas:
        criterias = session.query(db.Criterion).all()
        if diploma.publish_time.day < datetime.now().day + 1 or len(criterias) >= 3:
            diploma_wrapper = Diploma_wrapper(diploma)
            diploma_wrapper.release()
    session.close()
    s.enter(86400, 1, check_state)

s = sched.scheduler(time.time, time.sleep)
s.enter(86400, 1, check_state)
s.run()

# # Server
# app = Flask(__name__)

# @app.route("/")
# def test():
#     return 'Test'

# app.run()

# professor = Professor_wrapper()
# professor.sign_in("test_email@gmail.com", "test_password")
# professor.publish_diploma("test_thesis", "test_description", datetime.now(), True, "testing")
# professor.sign_up("Test name", 1, "test_email@gmail.com", "test_password", "test_password")
# professor.estimate_diploma(5, 5, 5, 5, 2)