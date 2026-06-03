from database.DAO import DAO


class Model:
    def __init__(self):
        self._anni = DAO.getAllYears()

