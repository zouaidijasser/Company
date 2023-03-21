# library
import sqlite3



class Database :
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS company (
            id INTEGER PRIMARY KEY,
            name text,
            age text,
            job text,
            email text,
            gender text,
            mobile text,
            address text
        );

        """
        self.cur.execute(sql)
        self.con.commit()
    def insert(self,name,age,job,email,gender,mobile,address) :
        self.cur.execute("insert into company values (Null,?,?,?,?,?,?,?)",
                        (name,age,job,email,gender,mobile,address))
        self.con.commit()
    
    def fetch(self) :
        self.cur.execute("select * from company")
        rows = self.cur.fetchall()
        return rows
    
    def remove(self,id) :
        self.cur.execute("delete from company where id =?",(id,))
        self.con.commit()

    def update(self,id,name,age,job,email,gendre,mobile,address) :
        self.cur.execute("update company set name=?,age=?,job=?,email=?,gender=?,mobile=?,address=? where id=?",
                        (name,age,job,email,gendre,mobile,address,id) )
        self.con.commit()
