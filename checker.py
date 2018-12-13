from datetime import datetime
from threading import Thread
import sched, time
import models.db as db
from configuration_manager import Configuration_Manager
from models.diploma_logic import Diploma_logic as Diploma_wrapper

s = sched.scheduler(time.time, time.sleep)

class Checker(Thread):
    def run(self):
        s.enter(Configuration_Manager.get_checking_interval(), 1, check_state)
        s.run()

def check_state():
    session = db.Session()
    diplomas = session.query(db.Diploma).all()
    for diploma in diplomas:
        criterias = session.query(db.Criterion).all()
        if diploma.publish_time.day + Configuration_Manager.get_unreleased_time() < datetime.now().day or len(criterias) >= Configuration_Manager.get_experts_count():
            diploma_wrapper = Diploma_wrapper(diploma)
            diploma = diploma_wrapper.release()
            session.commit()
    session.close()
    s.enter(Configuration_Manager.get_checking_interval(), 1, check_state)