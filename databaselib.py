import sqlite3
import datetime

def connectDB(dbname):
    conn = None 
    try:
        conn = sqlite3.connect(dbname)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    else:
        return conn    

car_table = '''CREATE TABLE IF NOT EXISTS car_table (
                    placa text PRIMARY KEY UNIQUE NOT NULL,
                    localidade text,
                    date text,
                    time text
               );'''

def createTable(dbname):
    conn = connectDB(dbname)
    if conn:
        try:
            db_cursor = conn.cursor()
            db_cursor.execute(car_table)
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

def insertData(placa, localidade,conn, cur):
    
    sqlInsert = '''INSERT INTO car_table(placa, localidade, date, time)
                    VALUES(?, ?, ?, ?)'''
    date = datetime.datetime.now()
    hour = str(date.hour)+':'+str(date.minute)+':'+str(date.second)

    placaDados = (str(placa), str(localidade), str(datetime.date.today()), hour)
    try:
        cur.execute(sqlInsert, placaDados)
    except sqlite3.Error as e:
        print(e)
    else:
        conn.commit()
        conn.close()
        return cur.lastrowid

def stringTratment(placa, localidade, dbname):
    conn = connectDB(dbname)
    cur = conn.cursor()

    if placa.find("-") != -1:
        novaplaca = placa.replace("-","")
        insertId = insertData(novaplaca, localidade, conn, cur)

def deletCar_table(dbname):
    conn = connectDB(dbname)
    cur = conn.cursor()

    sqlDelete = '''DELETE FROM car_table WHERE placa = ABC1235;'''
    cur.execute(sqlDelete)

    conn.close()
    
