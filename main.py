from flask import Flask
from threading import Thread
from checker import Checker
from models.professor_logic import Professor_logic as Professor_wrapper

checker = Checker()
checker.start()

# Server
app = Flask(__name__)

@app.route("/")
def test():
    return 'Test'

app.run()

# professor = Professor_wrapper()
# professor.sign_in("test_email@gmail.com", "test_password")
# professor.publish_diploma("test_thesis", "test_description", datetime.now(), True, "testing")
# professor.sign_up("Test name", 1, "test_email@gmail.com", "test_password", "test_password")
# professor.estimate_diploma(5, 5, 5, 5, 2)