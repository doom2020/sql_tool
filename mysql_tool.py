import pymysql



class MysqlHelp:
    def __init__(self, host, port, user, pwd, db=None, charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.db = db
        self.charset = charset
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.pwd, \
                                        db=self.db, charset=self.charset)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)
        return (self.conn, self.cursor)

    def operate_data(self, sql_cmd):
        try:
            self.cursor.execute(sql_cmd)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollabck()

    def query_data(self, sql_cmd):
        data_ls = None
        try:
            self.cursor.execute(sql_cmd)
            data_ls = self.cursor.fetchall()
        except Exception as e:
            print(e)
        return data_ls

    def close_connect(self):
        try:
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            print(e)
