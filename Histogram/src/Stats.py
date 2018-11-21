import sqlite3
from sqlite3 import Error

import numpy as np


var_sqlitedbFilePath = "db_BankAdditional.db"

# Defining database connection and supplying local sqlite db file path
def createConnection(var_dbFilePath):
    try:
        conn = sqlite3.connect(var_dbFilePath)
        print(sqlite3.version)  
        calculateStats(conn)
    except Error as err:
        print(err)
    finally:
        conn.close()

def calculateStats(conn):
    cursor = conn.cursor()
    
    query = "select distinct(job) from tbl_bankadditional;"
    cursor.execute(query)
    arr_distinctJob = np.asarray_chkfinite(cursor.fetchall())
    #print(arr_distinctJob)
    
    query = "select distinct(marital) from tbl_bankadditional;"
    cursor.execute(query)
    arr_distinctmarital = np.asarray_chkfinite(cursor.fetchall())
    #print(arr_distinctmarital[0])
    
    
    query = "create table If not exists tblStats(Job text,Married text, Single text, Divorced text, Unknown text);"
    cursor.execute(query)
    
    
    for job in arr_distinctJob:
        
        list_jobandmaritalpercentage = []
        list_recordset = [job[0],]
                
        for marital in arr_distinctmarital:
            query = "select count(marital) from tbl_bankadditional where marital='"+marital[0]+"' and job='"+job[0]+"';"
            cursor.execute(query)
            val_maritalandjob =cursor.fetchall()
            #print(val_maritalandjob[0][0])
            
            query = "select count(job) from tbl_bankadditional where job='"+job[0]+"';"
            cursor.execute(query)
            val_jobcount = cursor.fetchall()
            #print(val_jobcount[0][0])          
            
            val_percentage = ( val_maritalandjob[0][0] / val_jobcount[0][0]) * 100
            val_percentage = round(val_percentage,2)
            #print(val_percentage)
            
            
            list_recordset.append(str(val_percentage)+" %")
            #print(list_recordset)
            
   
        tuple_recordset = tuple(list_recordset)
        #print(tuple_recordset)
        
        list_jobandmaritalpercentage.append(tuple_recordset)
        
        #print(list_jobandmaritalpercentage)
        
        query = "insert into tblStats(Job, Married , Single , Divorced , Unknown) values (?,?,?,?,?)"
        cursor.executemany(query, list_jobandmaritalpercentage)
        #cursor.execute("COMMIT")    
        
        query = "select * from tblStats;"
        cursor.execute(query)
        
        #print(cursor.fetchall())



if __name__ == "__main__":
    createConnection(var_sqlitedbFilePath)