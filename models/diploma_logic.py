import numpy as np
import models.db as db

class Diploma_logic:

    def __init__(self, diploma):
        self.diploma = diploma

    def release(self):
        session = db.Session()
        criteria_list = session.query(db.Criterion).filter(db.Criterion.diploma_id == self.diploma.id).all()
        # Kendall coefficient of concordance (see http://blog.any-p.ru/node/349) 
        m = len(criteria_list)
        n = 4
        t = 0.5 * (n + 1) * m
        matrix = []
        for criteria in criteria_list: 
            estimations = []
            estimations.append(criteria.thesis_ev)
            estimations.append(criteria.relevance_ev)
            estimations.append(criteria.interest_ev)
            estimations.append(criteria.feasibility_ev)
            matrix.append(estimations)
        np_matrix = np.array(matrix)
        s = np.sum((np_matrix.sum(axis = 0) - t) ** 2)
        w = 12 * s / (m ** 2 * (n ** 3 - n))
        return w
