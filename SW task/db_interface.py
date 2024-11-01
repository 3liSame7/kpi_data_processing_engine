import sqlite3

class DatabaseInterface:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS messages (
            asset_id TEXT,
            attribute_id TEXT,
            timestamp TEXT,
            value TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def store_message(self, message):
        query = """
        INSERT INTO messages (asset_id, attribute_id, timestamp, value)
        VALUES (?, ?, ?, ?)
        """
        self.conn.execute(query, (message['asset_id'], message['attribute_id'], message['timestamp'], message['value']))
        self.conn.commit()

    def close(self):
        self.conn.close()
