from database import DB_connect
from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT DISTINCT YEAR(Date) AS Anno
                    FROM go_daily_sales
                    ORDER BY Anno DESC"""

        cursor.execute(query)

        res = []
        for row in cursor:
            # Dovro fare l'append di un oggetto corso, quindi dovrò crearmi il DTO Corso (perche?)
            res.append(row["Anno"]
            )

        cursor.close()
        cnx.close()
        return res  # Viene restituita una lista di anni

    @staticmethod
    def getProdotti():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT DISTINCT p.Product as Prodotto
                    FROM go_products p"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["Prodotto"]
                       )

        cursor.close()
        cnx.close()
        return res  # Viene restituita una lista di prodotti

    @staticmethod
    def getRetailer():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select *
                    from go_retailers """

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Retailer(
                code = row["Retailer_code"],
                name = row["Retailer_name"],
                type = row["Type"],
                country = row["Country"],
            ))

        cursor.close()
        cnx.close()
        return res  # Viene restituita una lista di Retailer
