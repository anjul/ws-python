import sqlite3
from sqlite3 import Error


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
    list_distinctJob = list(cursor.fetchall())
    #print(list_distinctJob)
    
    query = "select distinct(marital) from tbl_bankadditional;"
    cursor.execute(query)
    list_distinctmarital = list(cursor.fetchall())
    #print(list_distinctmarital)
      
    #resultList = []
    print(['Job']+list_distinctmarital)
    for job in list_distinctJob:
        
        list_recordset = [job[0],]
                
        for marital in list_distinctmarital:
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
            
   
        print(list_recordset)
        #resultList.append(list_recordset)
        
    #print(resultList)



if __name__ == "__main__":
    createConnection(var_sqlitedbFilePath)