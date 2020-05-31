from sqlalchemy import orm, connectors 
from psycopg2 import connect

# BASE ORM
class ORM:

    def query(self, q: str):
       orm.session.Session.query(q)

    def connection(self):
        try:
            session_pg = connect('dbname=test user=postgres password=verySecure')
        except:
            session_mysql = NotImplemented
        finally:
            session_sql = connectors.Connector()

# EXAMPLE
# ORM().query('''SELECT *''')