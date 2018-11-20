import sqlite3
from sqlite3 import Error

import numpy as np
from decimal import Decimal
from PyObjCTools.Conversion import decimal

var_sqlitedbFilePath = "/Users/anjul/eclipse/workspace/ws-python/Histogram/db/db_BankAdditional.db"

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


""""
select tbl_bankadditional.job as Job,( select round( (select count(marital) from tbl_bankadditional where marital='"+marital+"' and job='"+job+"') / (count(job)*0.01),2) from tbl_bankadditional where job='"+job+"') as Married,"+
                    "(select round((select count(marital) from tbl_bankadditional where marital='"+single+"' and job='"+admin+"') / (count(job)*0.01),2) from tbl_bankadditional where job like "%admin.%") as Single,"+
                    "(select round((select count(marital) from tbl_bankadditional where marital='"+divorced+"' and job='"+admin+"') / (count(job)*0.01),2) from tbl_bankadditional where job like "%admin.%") as Divorced,"+
                    "(select round((select count(marital) from tbl_bankadditional where marital='"+unknown+"' and job='"+admin+"') / (count(job)*0.01),2) from tbl_bankadditional where job like "%admin.%") as Unknown"+
                    "from tbl_bankadditional where job='"job+"' group by job;"
"""


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
    
    
    query = "create temp table tblStats(Job text,Married text, Single text, Divorced text);"
    cursor.execute(query)
    
    
    for job in arr_distinctJob:
        
        list_jobandmaritalpercentage = []
        
        for marital in arr_distinctmarital:
            #query = "select tbl_bankadditional.job as Job,(select round( (select count(marital) from tbl_bankadditional where marital='"+marital+"' and job='"+job+"') / (count(job)*0.01),2) from tbl_bankadditional where job='"+job+"') as'"+marital+"' from tbl_bankadditional where job='"+job+"' group by job;"
            query = "select count(marital) from tbl_bankadditional where marital='"+marital+"' and job='"+job+"';"
            cursor.execute(query)
            val_maritalandjob = cursor.fetchall()
            
            query = "select count(job) from tbl_bankadditional where job='"+job+"';"
            cursor.execute(query)
            val_jobcount = cursor.fetchall()
            
            val_percentage = (val_maritalandjob / val_jobcount)*100
            val_percentage = round(val_percentage,2)
            
            list_jobandmaritalpercentage.insert(val_percentage)
            
            #cursor.execute(query)
            #print(cursor.fetchall())
        
        
    
    #cursor.execute("select name from sqlite_master where type='table';")
    #print(cursor.fetchall())


if __name__ == "__main__":
    createConnection(var_sqlitedbFilePath)