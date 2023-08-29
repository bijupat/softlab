#file to connect to psql database of saflab app to import data from CSV (created from export of PPENT)
import psycopg2
import pymssql
from sys import exit
from func import connect_psql, connect_mssql, create_practitioner, add_dr_name, add_telecom, add_address

def main():
    # Connect to an existing psql database
    connpsql = connect_psql()

    # Connect to an existing mssql database
    connmssql = connect_mssql()

    #Open a cursor to perform database operations
    curmssql = connmssql.cursor()
    curmssql.execute("SELECT * FROM Mstdr")
    i=0
    for dr in curmssql.fetchall():
        if i < 3 :
            qualification = dr[4] or "Not Defined"
            # Create new pratitior object by inserting it in Practitioner table and get it's practitioner_id as return value
            practitioner_id = create_practitioner(qualification, connpsql)

            # save to Name Table and link it to practitioner        
            prefix =  dr[1] or ""
            given= dr[2] or ""
            add_dr_name(prefix, given, practitioner_id, connpsql)

            # save to Telecom Table mobile number and link it to practitioner if it has value
            if dr[11]:
                value= dr[11]
                use = "M"
                add_telecom(value,use, "P",practitioner_id, connpsql)

            # save to Telecom Table office number and link it to practitioner if it has value
            if dr[9]:
                value= dr[9]
                use = "W"
                add_telecom(value,use,"P", practitioner_id, connpsql)

            # save to Telecom Table home number and link it to practitioner if it has value
            if dr[10]:
                value= dr[10]
                use = "H"
                add_telecom(value,use,"P", practitioner_id, connpsql)

            # save to Telecom Table e mail  and link it to practitioner if it has value
            if dr[13]:
                value= dr[13]
                use = "H"
                add_telecom(value,use,"E", practitioner_id, connpsql)


            # save to address Table and link it to practitioner if it has value
            if dr[5]:
                text = dr[5] 
                line = dr[6] or ""
                postalcode = dr[8]
                add_address(text, line, postalcode, practitioner_id, connpsql)
            
            
            print(prefix +" "+ given + " added")
        i =  i + 1 

    try:
        connpsql.close()
        connmssql.close()
        print('Finally, BOTH connection closed.')
    except(Exception) as error:
        print(f"cannot close one or both connection because : {error}")






if __name__ == "__main__":
    main()