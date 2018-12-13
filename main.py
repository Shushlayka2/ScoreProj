from datetime import datetime
from threading import Thread
from checker import Checker
from models.professor_logic import Professor_logic as Professor_wrapper

checker = Checker()
checker.start()