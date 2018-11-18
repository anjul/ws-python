import sqlite3
from sqlite3 import Error

import matplotlib.pyplot as plt
import numpy as np


var_sqlitedbFilePath = "/Users/anjul/eclipse/workspace/ws-python/Histogram/db/db_BankAdditional.db"

# Defining database connection and supplying local sqlite db file path
def createConnection(var_dbFilePath):
    try:
        conn = sqlite3.connect(var_dbFilePath)
        print(sqlite3.version)
        listAllTables(conn)
    except Error as err:
        print(err)
    finally:
        conn.close()
        
# method to display all tables available in existing db
def listAllTables(conn):
    cursor = conn.cursor()
    cursor.execute("select name from sqlite_master where type='table';")
    print(cursor.fetchall())

    computeHistogramAllAgesWithUnivDeg(cursor)
    
        
        
#Method to compute & plot histogram for all ages with university degree holder from dataset        
def computeHistogramAllAgesWithUnivDeg(cursor):
    cursor.execute("select age from tbl_bankadditional where education='university.degree';")
    listAge = cursor.fetchall()
    arrayAge = np.asarray_chkfinite(listAge)
    print(arrayAge)
    
    bins = 3
    _label="Age of all people with Univ Degree"
    plt.hist(arrayAge, bins, histtype='bar', align='mid', color='g', edgecolor='black', label=_label)
    plt.title("Histogram of age of all people with university degree")
    plt.legend()
    #plt.show()
    plt.savefig('1.png')
    plt.clf()
    computeHistogramAllAgesWithUnivDegWithY(cursor)
    
    
    
#Method to compute & plot histogram for all ages with university degree with label y='yes' holder from dataset        
def computeHistogramAllAgesWithUnivDegWithY(cursor):
    cursor.execute("select age from tbl_bankadditional where education='university.degree' and y='yes';")
    listAge = cursor.fetchall()
    arrayAge = np.asarray_chkfinite(listAge)
    #print(myArray)
    
    bins = 5
    _label="Age of all people with Univ Degree with y='yes'"
    plt.hist(arrayAge, bins, histtype='bar', align='mid', color='b', edgecolor='black', label=_label)
    plt.title("Histogram of age of all people with university degree with label y='yes'")
    plt.legend()
    #plt.show()
    plt.savefig('2.png')
    plt.clf()
    computeHistogramAllAgesWithUnivDegWithN(cursor)


#Method to compute & plot histogram for all ages with university degree with label n='no' holder from dataset        
def computeHistogramAllAgesWithUnivDegWithN(cursor):
    cursor.execute("select age from tbl_bankadditional where education='university.degree' and y='yes';")
    listAge = cursor.fetchall()
    arrayAge = np.asarray_chkfinite(listAge)
    #print(myArray)
    
    bins = 5
    _label="Age of all people with Univ Degree with n='no'"
    plt.hist(arrayAge, bins, histtype='bar', align='mid', color='c', edgecolor='black', label=_label)
    plt.title("Histogram of age of all people with university degree with label n='no'")
    plt.legend()
    #plt.show()
    plt.savefig('3.png')
        
if __name__ == "__main__":
    createConnection(var_sqlitedbFilePath)