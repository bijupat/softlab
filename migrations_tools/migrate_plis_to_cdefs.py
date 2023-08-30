#file to connect to psql database of saflab app to import data from CSV (created from export of PPENT)
#import psycopg2
#import csv
#from sys import argv
#import pymssql
#import sys
import datetime
from func import connect_psql, connect_mssql



def main():
    # Connect to an existing psql database
    connpsql = connect_psql()
    #Open a cursor to perform database operations
    #curpsql = connpsql.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Connect to an existing mssql database
    connmssql = connect_mssql()

    #Open a cursor to perform database operations in msql
    curmssql = connmssql.cursor()

    #Open a cursor to perform database operations in psql
    curpsql = connpsql.cursor()

    #SELCT pricelist items from table for picelist of mahi mstplkey = 50
    curmssql.execute("SELECT * FROM Mstplitems WHERE mstplkey = %s", 50)
    for pli in curmssql.fetchall():
        if pli["Rate"] > 0 :
            title = pli['Item'] #item 
            value = pli["Rate"] #rate
            print_in_receipt = pli["PrintInRecp"] #printinrecp
            alias = pli["ShortName"] #shortname
            created = datetime.datetime.now() # add present time date to avoid not null contrain on created column
            status = 'active'
            experimental = False
            is_profile = False
            SQL = "INSERT INTO labsys_ChargeItemDefinition (title, value, print_in_receipt, alias, created, status, experimental, is_profile) VALUES ( %s, %s , %s, %s, %s, %s, %s, %s)" # Note: no quotes
            data = (title, value, print_in_receipt, alias , created, status, experimental, is_profile)
            curpsql.execute(SQL, data) # Note: no % operator
            connpsql.commit()
            print (f'{title} added successfully')

    """    
    curmssql.execute("SELECT top(100) * FROM Mstpl")
    for pl in curmssql.fetchall():
        print(pl)
    """

if __name__ == "__main__":
    main()



    """
    print(f'mstitemkey = {pli[0]}')
    print(f'mstplkey = {pli[1]}')
    print(f'item = {pli[2]}')
    print(f'rate = {pli[3]}')
    print(f'collection = {pli[4]}')
    print(f'printinrecp = {pli[5]}')
    print(f'shortname = {pli[6]}')
    print(f'itemcode = {pli[7]}')
    print(f'category = {pli[8]}')
    print(f'outsourced = {pli[9]}')
    print(f'repofreq = {pli[10]}')
    print(f'repocolltime = {pli[11]}')
    print(f'outsrcto = {pli[12]}')
    print(f'tubecolors = {pli[13]}')
    print('**********************')
    
    if pli[1] == 33:
        title = pli[2] #item 
        value = pli[3] #rate
        print_in_receipt = pli[5] #printinrecp
        alias = pli[6] #shortname
        created = datetime.datetime.now() # add present time date to avoid not null contrain on created column
        status = 'active'
        experimental = False
        is_profile = False
        Note = f"Note for chargeitem {title}"
        SQL = "INSERT INTO labsys_ChargeItemDefinition (title, value, print_in_receipt, alias, created, status, experimental, is_profile) VALUES ( %s, %s , %s, %s, %s, %s, %s, %s)" # Note: no quotes
        data = (title, value, print_in_receipt, alias , created, status, experimental, is_profile)
        cur.execute(SQL, data) # Note: no % operator
        conn.commit()
        print (f'{i}: {title} added successfully')
        i = i + 1
    """


