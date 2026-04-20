from database import DB_connect
from database.DB_connect import DBConnect
from model.retailer import Retailer
from model.vendita import Vendita


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
    def getBrand():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT DISTINCT Product_brand as brand
                   FROM go_products 
                   ORDER BY Product_brand"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["brand"]
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

    @staticmethod
    def getTopVendite(anno, brand, retailer_code):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # Nota l'uso di COALESCE(%s, colonna)
        # Se il primo parametro è NULL, SQL usa il valore della colonna stessa (sempre vero)
        query = """
                SELECT s.Date, p.Product_brand, s.Retailer_code, (s.Unit_sale_price * s.Quantity) as Ricavo
                FROM go_daily_sales s
                         JOIN go_products p ON s.Product_number = p.Product_number
                WHERE (%s IS NULL OR YEAR (s.Date) = %s)
                      AND (%s IS NULL \
                   OR p.Product_brand = %s)
                  AND (%s IS NULL \
                   OR s.Retailer_code = %s)
                ORDER BY Ricavo DESC
                    LIMIT 5 \
                """


        # Passiamo ogni parametro due volte (una per il check NULL, una per l'uguaglianza)
        params = (anno, anno, brand, brand, retailer_code, retailer_code)
        cursor.execute(query, params)

        res = []
        for row in cursor:
            res.append(Vendita(
                data=row["Date"],
                brand=row["Product_brand"],
                retailer_code=row["Retailer_code"],
                ricavo=row["Ricavo"]
            ))

        cursor.close()
        cnx.close()
        return res
