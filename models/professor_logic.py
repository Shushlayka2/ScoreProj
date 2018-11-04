from sqlalchemy import insert, func
import models.db as db

class Professor_logic(db.Professor):

    def sign_up(self, name, department, email, password, confirm_password):
        if password != confirm_password:
            return False
        self = db.Professor()
        self.email = email
        self.password = password
        self.full_name = name
        session = db.Session()
        self.department = session.query(db.Department).filter(db.Department.id == department).first()
        session.add(self)
        session.commit()
        session.close()
        return True

    def sign_in(self, email, password):
        professor_id = db.engine.execute(func.user_auth(email, password)).first()[0]
        session = db.Session()
        professor = session.query(db.Professor).filter(db.Professor.id == professor_id).first()
        session.close()
        return professor

    def publish_diploma(self, thesis, description, deadline, team_work, scope):
        session = db.Session()
        diploma = db.Diploma()
        diploma.thesis = thesis
        diploma.description = description
        diploma.deadline = deadline
        diploma.team_work = team_work
        diploma.professor = self
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