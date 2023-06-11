import cx_Oracle

from django.conf import settings

con = {
    'user': settings.ORACLE_DB_USER,
    'password': settings.ORACLE_DB_PASSWORD,
    'dsn': str(cx_Oracle.makedsn(
        host=settings.ORACLE_DB_HOST,
        port=settings.ORACLE_DB_PORT
    ))
}
def run_query(query):
    connection = cx_Oracle.connect(**con)
    c = connection.cursor()
    c.execute(query)
    try:
        data = c.fetchall()
    except: # For Insertion
        data = None
        connection.commit()
    connection.close()
    return data
