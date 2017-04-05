import pyodbc


class SQLServerConn:
    """Conexao hardcoded com SQL Server para testes do bot"""
    #conection string example:  'DRIVER={SQL Server};SERVER=.\sqlexpress;DATABASE=Bot_Database;UID=sa;PWD=Elipse21'

    def __init__(self, query_string, connection_string):
        self.query = query_string
        self.connection_string = connection_string

    def Query(self):
        connectionstring = 'DRIVER={SQL Server};SERVER=.\sqlexpress;DATABASE=Bot_Database;UID=sa;PWD=Elipse21'
        conn = pyodbc.connect(self.connection_string)
        cursor = conn.cursor()

        row = cursor.execute(self.query).fetchall()
        print row







