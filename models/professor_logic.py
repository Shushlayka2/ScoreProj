from sqlalchemy import insert, func
from datetime import datetime
import models.db as db

class Professor_logic:

    def __init__(self):
        self.professor = None

    def sign_up(self, name, department, email, password, confirm_password):
        if password != confirm_password:
            return False
        self.professor = db.Professor()
        self.professor.email = email
        self.professor.password = password
        self.professor.full_name = name
        session = db.Session()
        self.professor.department = session.query(db.Department).filter(db.Department.id == department).first()
        session.add(self.professor)
        session.commit()
        session.close()
        return True

    def sign_in(self, email, password):
        professor_id = db.engine.execute(func.user_auth(email, password)).first()[0]
        session = db.Session()
        self.professor = session.query(db.Professor).filter(db.Professor.id == professor_id).first()
        session.close()
        if (self.professor != None):
            return True
        else:
            return False

    def publish_diploma(self, thesis, description, deadline, team_work, scope):
        session = db.Session()
        diploma = db.Diploma()
        diploma.thesis = thesis
        diploma.description = description
        diploma.deadline = deadline
        diploma.team_work = team_work
        diploma.professor = self.professor
        diploma.publish_time = datetime.now()
        if type(scope) is str:
            scope_ent = db.Scope()
            scope_ent.name = scope
            session.add(scope_ent)
            session.commit()
            diploma.scope = scope_ent
        elif type(scope) is int:
            diploma.scope = session.query(db.Scope).filter(db.Scope.id == scope).first()
        session.add(diploma)
        session.commit()
        session.close()

    def estimate_diploma(self, thesis, relevance, interest, feasibility, diploma):
        if self.professor.is_expert == False:
            return
        criteria = db.Criterion()
        criteria.thesis_ev = thesis
        criteria.relevance_ev = relevance
        criteria.interest_ev = interest
        criteria.feasibility_ev = feasibility
        session = db.Session()
        criteria.diploma = session.query(db.Diploma).filter(db.Diploma.id == diploma).first()
        criteria.expert = self.professor
        session.flush()
        session.add(criteria)
        session.commit()
        session.close()