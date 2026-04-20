from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getAllAnni(self):
        return DAO.getAnni()

    def getAllBrand(self):
        return DAO.getBrand()

    def getAllRetailer(self):
        return DAO.getRetailer()

    def getTopVendite(self, anno, brand, retailer_code):
        return DAO.getTopVendite(anno, brand, retailer_code)

    def getStatistiche(self, anno, brand, retailer_code):
        return DAO.getStatisticheVendite(anno, brand, retailer_code)