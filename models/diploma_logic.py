import numpy as np
import models.db as db

class Diploma_logic:

    def __init__(self, diploma):
        self.diploma = diploma

    def release(self):
        session = db.Session()
        criteria_list = session.query(db.Criterion).filter(db.Criterion.diploma_id == self.diploma.id).all()
        l = len(criteria_list)
        matrix = []
        for criteria in criteria_list: 
            estimations = []
            estimations.append(criteria.thesis_ev)
            estimations.append(criteria.relevance_ev)
            estimations.append(criteria.interest_ev)
            estimations.append(criteria.feasibility_ev)
            matrix.append(estimations)
        np_matrix = np.array(matrix)
        coef = self.calculate_coef(l, np_matrix)
        ev = self.calculate_evaluation(l, np_matrix)
        self.diploma.evaluation = ev
        self.diploma.coefficient = coef
        session.close()
        return self.diploma
        
    def calculate_evaluation(self, length, np_matrix):
        return np.sum(np_matrix.mean(axis = 0)) / length

    def calculate_coef(self, length, np_matrix):
        # Kendall coefficient of concordance (see http://blog.any-p.ru/node/349) 
        m = length
        n = 4
        t = 0.5 * (n + 1) * m
        
        s = np.sum((np_matrix.sum(axis = 0) - t) ** 2)
        w = 12 * s / (m ** 2 * (n ** 3 - n))
        return w
