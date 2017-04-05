import unittest
from watson_developer_cloud import ConversationV1
from license_query.sql_query import SQLServerConn


class TestSQLServerConnection(unittest.TestCase):

    def testSQLServerConnection(self):
        Conn = SQLServerConn(query_string='SELECT * FROM licenca_table',connection_string='DRIVER={SQL Server};SERVER=.\sqlexpress;DATABASE=Bot_Database;UID=sa;PWD=Elipse21')
        Conn.Query()


class TestWatsonConnection(unittest.TestCase):

    def testwatson(self):

        conversation = ConversationV1(
            username='48668bda-7cdc-4e2c-b98b-61d8498fd93b',
            password='QzdhAsFJLly6',
            version='2016-09-20')

        # replace with your own workspace_id
        workspace_id = '97f9058e-9f52-4d7c-8bba-bb45d485c071'

        response = conversation.message(workspace_id=workspace_id, message_input={
            'text': 'oi'})
        print response





if __name__ == '__main__':
    unittest.main()
