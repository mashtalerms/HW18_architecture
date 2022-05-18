from dao.model.directorModel import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, did):
        return self.session.query(Director).get(did)
