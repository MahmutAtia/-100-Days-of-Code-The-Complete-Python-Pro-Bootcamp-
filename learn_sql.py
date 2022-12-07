import sqlite3

db = sqlite3.connect("me.db")
c = db.cursor()
#c.execute("DROP TAble me")
#c.execute("CReATE TABLE me (ID INTEGER PRIMARY KEY AUTOINCREMENT , name VARCHAT(30))")

name= "mo"
c.execute("INSERT INTO me(name) VALUES(:name)", {'name': name})
db.commit()
c.execute("SELECT * FROM me")
b=c.fetchall()
print(b)