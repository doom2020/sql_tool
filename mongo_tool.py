from pymongo import MongoClient




class MyMongo:
    def __init__(self, host, port, db_name=None, collection_name=None):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.collection_name = collection_name
        self.conn = None
        self.db = None
        self.collection = None
        self.connect()

    def connect(self):
        try:
            self.conn = MongoClient(self.host, self.port)
        except Exception as e:
            print(e)
        try:
            self.db = self.conn.self[self.db_name]
        except Exception as e:
            print(e)
        try:
            self.collection = self.db[self.collection_name]
        except Exception as e:
            print(e)

        return (self.conn, self.db, self.collection)