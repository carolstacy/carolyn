import sqlite3
conn=sqlite3.connect('Mitmidmorn.db')
print("Open Database Successfully")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (1,'CARO',17,'EMOBILIS','FEMALE')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (2,'KIMSY',18,'STATE HOUSE' ,'MALE')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (3,'ANGEL',19,'NYERI HIGH' ,'FEMALE')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (4,'SUU',12,'BROOKHOUSE', 'FEMALE')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (5,'LOCXY',20,'KABARAK HIGH' ,'MALE')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (6,'MORRIS',16,'SACHO HIGH', 'MALE')")

conn.commit()
print("Records added successfully")
conn.close()