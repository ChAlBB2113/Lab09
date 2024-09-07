from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getArrivoPartenzaMedia():
        conn = DBConnect.get_connection()
        result = {}
        cursor = conn.cursor(dictionary=True)
        query = """select ORIGIN_AIRPORT_ID as a1, DESTINATION_AIRPORT_ID as a2, avg(distance) as d
                    from extflightdelays.flights f  
                    group by a1, a2
                     """
        cursor.execute(query, ())
        for row in cursor:
            result[(row["a1"], row["a2"])] = row["d"]

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAereoporti():
        conn = DBConnect.get_connection()
        result = {}
        cursor = conn.cursor(dictionary=True)
        query = """select ID as id, airport as name
                            from extflightdelays.airports a 
                            
                             """
        cursor.execute(query, ())
        for row in cursor:
            result[row["id"]] = row["name"]

        cursor.close()
        conn.close()
        return result
