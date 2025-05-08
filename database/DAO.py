from database.DB_connect import DBConnect
from model.airports import Airports
from model.flights import Flights


class DAO():
    @staticmethod

    def get_aereoporti():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM airports"
        cursor.execute(query)

        for row in cursor:
            result.append(Airports(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_flights(distance):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM flights WHERE DISTANCE>=%s"
        cursor.execute(query,(distance,))

        for row in cursor:
            result.append(Flights(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_voli_ab(a,b):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT *
            FROM flights
            WHERE (ORIGIN_AIRPORT_ID = %s AND DESTINATION_AIRPORT_ID = %s)
               OR (ORIGIN_AIRPORT_ID = %s AND DESTINATION_AIRPORT_ID = %s)
        """
        cursor.execute(query, (a, b, b, a))

        for row in cursor:
            result.append(Flights(**row))

        cursor.close()
        conn.close()
        return result



