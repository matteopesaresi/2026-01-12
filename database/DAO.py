from database.DB_connect import DBConnect
from model.Constructor import Constructor


class DAO():

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()
        if conn is None:
            print(f"errore di connessione")
            return
        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT distinct year FROM seasons s  ORDER BY year"

        cursor.execute(query)

        for row in cursor:
            results.append(row["year"])

        cursor.close()
        conn.close()
        return results
    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        if conn is None:
            print(f"errore di connessione")
            return
        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM constructors"

        cursor.execute(query)

        for row in cursor:
            results.append(Constructor(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getNodes(anno1,anno2):
        conn = DBConnect.get_connection()
        if conn is None:
            print(f"errore di connessione")
            return
        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT c.constructorId JOIN results r ON c.constructorId = r.constructorId JOIN races r2 ON r.racedId = r2.raceId Where r2.year >= %s and r2.year<=%s and r.position is not null"

        cursor.execute(query,(anno1,anno2,))

        for row in cursor:
            results.append(row)

        cursor.close()
        conn.close()
        return results

