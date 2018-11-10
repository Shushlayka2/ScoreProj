from datetime import datetime
from threading import Thread
import sched, time
import models.db as db
from models.diploma_logic import Diploma_logic as Diploma_wrapper

s = sched.scheduler(time.time, time.sleep)

class Checker(Thread):
    def run(self):
        s.enter(86400, 1, check_state)
        s.run()

def check_state():
    session = db.Session()
    diplomas = session.query(db.Diploma).all()
    for diploma in diplomas:
        criterias = session.query(db.Criterion).all()
        if diploma.publish_time.day + 3 < datetime.now().day or len(criterias) >= 6:
            diploma_wrapper = Diploma_wrapper(diploma)
            diploma_wrapper.release()
    session.close()
    s.enter(86400, 1, check_state)