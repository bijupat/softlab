#file to connect to psql database of saflab app to import data from CSV (created from export of PPENT)
#import psycopg2
import psycopg2.extras
#import csv
#import pymssql
#import datetime
from func import connect_psql, connect_mssql, create_practitioner, add_name, add_telecom, add_address, find_or_add_patient


def main():
    # Connect to an existing psql database
    connpsql = connect_psql()
    #Open a cursor to perform database operations
    curpsql = connpsql.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Connect to an existing mssql database
    connmssql = connect_mssql()

    #Open a cursor to perform database operations
    with connmssql.cursor(as_dict=True) as curmssql:
        curmssql.execute("SELECT * FROM Tbllab LIMIT 5 ORDER BY dor DESC")
        tbllabs = curmssql.fetchall()
    for pt in tbllabs:
        curmssql.execute("SELECT drname FROM Mstdr WHERE mstdrkey = %s", refdr)
        dr = curmssql.fetchone()[0]
        print(dor)
        # find patient from existing PSQL(softlab) data if already added
        print("patid ", find_or_add_patient(pt[fname], pt[mname], pt[lname],  pt[sex], pt[age], pt[dor], pt[phone], pt[email], pt[connpsql]))
        
        with connmssql.cursor(as_dict=True) as curmssql:
            curmssql.execute("SELECT * FROM Tblinv WHERE labkey = %s", pt["labkey"])
            invs = curmssql.fetchall()
        for inv in invs:
            invkey = inv["invkey"]
            print(f"     chargeitem : {inv['invkey']}")
            with connmssql.cursor(as_dict=True) as curmssql:
                curmssql.execute("SELECT * FROM Tbltests WHERE invkey = %s", invkey)
                tests = curmssql.fetchall()                
            for test in tests:
            if test[5]:
                print(f'                Observtion:{test["testid"]} result : {test["result"]} ({test["normals"]}), {test["nlow"]}- {test["nhigh"]}')


        print()

    
        
    try:
        connpsql.close()
        connmssql.close()
        print('Finally, BOTH connection closed.')
    except(Exception) as error:
        print(f"cannot close one or both connection because : {error}")





if __name__ == "__main__":
    main()



