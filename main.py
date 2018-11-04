import datetime
from models.professor_logic import Professor_logic as Professor

professor = Professor()
professor.sign_in("test_email@gmail.com", "test_password")
# professor.sign_up("Test name", 1, "test_email@gmail.com", "test_password", "test_password")
# professor.publish_diploma("test_tesis", "test_description", datetime.datetime.now(), True, 1)