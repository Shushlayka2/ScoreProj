from datetime import datetime
from threading import Thread
import sched, time
import models.db as db
from models.diploma_logic import Diploma_logic as Diploma_wrapper

s = sched.scheduler(time.time, time.sleep)

class Checker(Thread):
    def run(self):
        s.enter(2, 1, check_state)
        s.run()

def check_state():
    session = db.Session()
    diplomas = session.query(db.Diploma).all()
    for diploma in diplomas:
        criterias = session.query(db.Criterion).all()
        if diploma.publish_time.day < datetime.now().day + 1 or len(criterias) >= 3:
            diploma_wrapper = Diploma_wrapper(diploma)
            diploma_wrapper.release()
    session.close()
    s.enter(2, 1, check_state)