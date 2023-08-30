#file to connect to psql database of saflab app to import data from CSV (created from export of PPENT)
import psycopg2
#import csv
from sys import argv
import pymssql
import sys


try:
    # Connect to an existing database
    conn = psycopg2.connect(host="122.179.129.85", database="labsys", user="postgres", password="your_password")
    connmssql = pymssql.connect(server= '192.168.102.150', user = 'SA', password = 'LETMEIN', database = 'MEDI201819NEW')

    if conn is not None or connmssql is not None:
        #Open a cursor to perform database operations


        """
         cur2 = conn.cursor()
        cur2.execute("SELECT * FROM labsys_ObservationDefinition" )
        for odef in cur2.fetchall():
            for o in odef:
                print (o, " ", end="") 
            print()  
            print("--------------------------------------")
         
        print("************all specemen listed**********"   )
        """

       


        """
        with open(argv[1]) as file:
            csvdata = csv.DictReader(file)
            for row in csvdata:
                print(row)
                #cur.execute("INSERT INTO pricelist (testid, test, lprice, SmpType ) VALUES(?,?,?,?)", row["No"], row["Test"], row["lprice"], row["Sample"])
        """

        
        curmssql = connmssql.cursor()
        cur = conn.cursor()

        curmssql.execute("SELECT * FROM Msttests")
        i=0

        for t in curmssql.fetchall():
            if i > 98:
                Test = t[1]
                Default_value = t[3]
                Options = t[4]
                Unit = t[7]
                Alias_sms = t[12]
                tat = t[14]
                Formula = t[15]
                Vrule = t[16]
                Vmsg = t[17]
                Vrulemust = t[18]

                SQL = "INSERT INTO labsys_ObservationDefinition (Test, Default_value, Options, Unit, Alias_sms, Tat, Formula, Vrule, Vmsg, Vrulemust) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" # Note: no quotes
                data = (Test, Default_value, Options, Unit, Alias_sms, tat, Formula, Vrule, Vmsg, Vrulemust )
                cur.execute(SQL, data) # Note: no % operator
                conn.commit()
                print (f'{Test} added successfully as {data}')
            i = i + 1
  

        
        """
        with open(argv[1]) as file:
            csvdata = csv.DictReader(file)
            for row in csvdata:
                print(row)  
        """  
    else:
        print('Connection not established to either  PostgreSQL or Mssql.')
         
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
 
finally:
    if conn is not None:
        #Close communication with the database
        conn.close()
        print('Finally, connection closed.')







"""
labsys_observationdef

0 : 7 | ID
1 :  B12 | Test
2 : Vitamin B12 | Alias
3 :  CLIA | Method
4 : mg/dl | Unit
5 :  loinc code for b12 |Loinc code:
6 : L | Category
7 :  Note for  b12 | Note
8 : 2 | Specimen
9 :  b12 sms | Alias sms
10 :  formula for b12 | Formula

11 : False | Is calculated:

12 :  options for b12 | OPTIONS
13 : None | Tat
14 :  v msg for b12 | Vmsg
15 : v rule for b12 | Vrule

16 :  True | Vrulemust

17 : None | department
18 :  b12 default  | Default value:



testdb_Msttests::

id : 18 | msttestkey
1 :  FBS | test
2 : fbs | testid
3 :   | result(defalut)
4 :  | options
5 :   | analyzer
6 :  | anatest
7 :  mg/dL | unit
8 : BIOCHEM | dept
9 :  None | location
10 :  True | printincard
11 : 70-110 | normals 
12 :  FBS | test4sms
13 : True | visible2all
14 :  30 | tatinmm
15 :  | formula
16 :  [fbs]<120 | vrule
17 : Is FBS Abnormal ? | vmsg
18 :  False | vrulemust
19 :   | 
20 :  |
"""