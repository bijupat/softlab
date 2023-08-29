#file to connect to psql database of saflab app to import data from CSV (created from export of PPENT)
#import psycopg2
#import psycopg2.extras
#import csv
#import pymssql
#from pymssql.cursors import DictCursor
#import datetime
from func import connect_psql, connect_mssql, create_practitioner,  add_telecom, add_address, find_or_add_patient, find_of_add_refdoc, find_or_add_obdef


def main():
    # Connect to an existing psql database
    connpsql = connect_psql()
    #Open a cursor to perform database operations
    #curpsql = connpsql.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Connect to an existing mssql database
    connmssql = connect_mssql()

    #Open a cursor to perform database operations
    curmssql = connmssql.cursor()
    curmssql.execute("SELECT top(1) * FROM Tbllab ORDER BY dor DESC")
    for pt in curmssql.fetchall():
        #print(pt)
        curmssql.execute("SELECT * FROM Mstdr WHERE mstdrkey = %s", pt["RefDr"])
        ref_dr_dic = curmssql.fetchone()
        #print(ref_dr_dic)

        #print(dr)
        print(f'{pt["DOR"]} :{pt["SampNo"]} : {pt["LabRefNo"]} : {pt["PatName"]} {pt["Age"]} {pt["AgeUnit"]}/{pt["Sex"]}: {pt["Phone"]} :  ')
        # find patient from existing PSQL(softlab) data if already added and add if not already added
        patientid = find_or_add_patient(pt["FName"], pt["MName"], pt["LName"],  pt["Sex"], pt["Age"], pt["DOR"], pt["Phone"], pt["Email"], connpsql)
        print(patientid)
        # find refdoc from existing PSQL(softlab) data if already added and add if not already added
        practitioner_id = find_of_add_refdoc(ref_dr_dic, connpsql)
        print(practitioner_id)
        curmssql.execute("SELECT * FROM Tblinv WHERE labkey = %s", pt["LabKey"])
        for inv in curmssql.fetchall():
            #print(inv)
            invkey = inv["InvKey"]
            print(f"     chargeitem : {inv['Item']}")
            """                
            curmssql.execute("SELECT * FROM Tblrepo WHERE labkey = %s", pt["LabKey"])            
            for report in curmssql.fetchall():
                repokey = report[0]
                print(f"reports :{report[6]}")
                print("****")
            """                
            curmssql.execute("SELECT top(1) * FROM Tbltests WHERE invkey = %s", invkey)
            for test in curmssql.fetchall():
                find_or_add_obdef(test, connpsql)
                """
                #print(test)
                if test["InvKey"]:
                    print(f'                Observtion:{test["Test"]} result : {test["Result"]} ({test["Normals"]}), {test["nLow"]}- {test["nHigh"]}')
                """

        print("***************************************************************************************************")

    try:
        connpsql.close()
        connmssql.close()
        print('Finally, BOTH connection closed.')
    except(Exception) as error:
        print(f"cannot close one or both connection because : {error}")

if __name__ == "__main__":
    main()