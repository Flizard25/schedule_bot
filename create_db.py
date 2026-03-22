import sqlite3
from config import DATABASE

class DB_Manager:
    def __init__(self, database):
        self.database = database
        self.create_tables()
        
    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS schedule (
                            monday TEXT,
                            tuesday TEXT,
                            wednesday TEXT,
                            thursday TEXT,
                            friday TEXT
                        )''') 
            conn.commit()

    def __executemany(self, sql, data):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.executemany(sql, data)
            conn.commit()
    
    def __select_data(self, sql, data = tuple()):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            return cur.fetchall()
        
    def get_monday_schedule(self):
        sql = "SELECT monday FROM schedule"
        return self.__select_data(sql)       

    def get_tuesday_schedule(self):
        sql = "SELECT tuesday FROM schedule"
        return self.__select_data(sql)
        
    def get_wednesday_schedule(self):
        sql = "SELECT wednesday FROM schedule"
        return self.__select_data(sql)
        
    def get_thursday_schedule(self):
        sql = "SELECT thursday FROM schedule"
        return self.__select_data(sql)
         
    def get_friday_schedule(self):
        sql = "SELECT friday FROM schedule"
        return self.__select_data(sql)
    
if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    print(manager.get_monday_schedule())