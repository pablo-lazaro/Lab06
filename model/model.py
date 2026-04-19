from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getAllAnni(self):
        return DAO.getAnni()

    def getAllProdotti(self):
        return DAO.getProdotti()

    def getAllRetailer(self):
        return DAO.getRetailer()