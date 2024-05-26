from wordDB.db_connection import connect_to_database
class BaseCRUD:
    def __init__(self, table_name, required_fields):
        self.table_name = table_name
        self.required_fields = required_fields
        self.conn = connect_to_database()
        self.cursor = self.conn.cursor(dictionary=True)

    def create(self, **kwargs):
        for field in self.required_fields:
            if field not in kwargs:
                raise ValueError(f"Missing required field: {field}")
        keys = ', '.join(kwargs.keys())
        values = ', '.join(['%s'] * len(kwargs))
        sql = f"INSERT INTO {self.table_name} ({keys}) VALUES ({values})"
        self.cursor.execute(sql, tuple(kwargs.values()))
        self.conn.commit()
        return self.cursor.lastrowid

    def read(self, record_id):
        sql = f"SELECT * FROM {self.table_name} WHERE id = %s"
        self.cursor.execute(sql, (record_id,))
        return self.cursor.fetchone()

    def update(self, record_id, **kwargs):
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        sql = f"UPDATE {self.table_name} SET {set_clause} WHERE id = %s"
        self.cursor.execute(sql, tuple(kwargs.values()) + (record_id,))
        self.conn.commit()
        return self.cursor.rowcount

    def delete(self, record_id):
        sql = f"DELETE FROM {self.table_name} WHERE id = %s"
        self.cursor.execute(sql, (record_id,))
        self.conn.commit()
        return self.cursor.rowcount

    def __del__(self):
        self.cursor.close()
        self.conn.close()


class User(BaseCRUD):
    def __init__(self):
        super().__init__('users')


class Word(BaseCRUD):
    def __init__(self):
        super().__init__('word')
