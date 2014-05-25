__author__ = 'lionel'

import psycopg2


class DBError:
    def __init__(self, msg):
        """Used to push messages to the UI
        """
        self.msg = msg

    def get_msg(self):
        return self.msg


class Database(object):
    def __init__(self, name, host, port, database, user, password):
        self.name = name
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection_list = list()

    def newConnection(self):
        connection = psycopg2.connect(host=self.host,
                                      port=self.port,
                                      database=self.database,
                                      user=self.user,
                                      password=self.password)
        self.connection_list.append(connection)
        return connection

    def close(self):
        [cursor.close() for cursor in self.connection_list]
        self.conn.close()


def execute(connection, query, size=None):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
    except Exception as e:
        connection.rollback()
        return None, DBError(e.__str__()), None
    headers = [c.name for c in cursor.description]
    res = fetch(cursor, size)
    status = cursor.statusmessage
    cursor.close()
    return headers, res, status


def fetch(cursor, size=None):
    try:
        if size:
            return cursor.fetchmany(size)
        else:
            return cursor.fetchall()
    except psycopg2.ProgrammingError, err:
        return DBError(err)
