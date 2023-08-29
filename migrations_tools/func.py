"""
This file is consist of support function for migrate.py
"""
import pymssql
import psycopg2
from sys import exit
import datetime

# Connect to an existing psql database
def connect_psql():
    try:        
        return psycopg2.connect(host="122.179.129.85", database="labsys", user="postgres", password="your_password")
        
    except(Exception) as error:
            print("cannot connect with PSQL WITH error as below:")
            exit(error)

# Connect to an existing mssql database
def connect_mssql():
    try:
        return pymssql.connect(server= '192.168.102.150', user = 'SA', password = 'LETMEIN', database = 'MEDILAB2023',as_dict=True,)
    except(Exception) as error:
            print("cannot connect with MSSQL WITH error as below:")
            exit(error)

# save to Name Table and link it to person
def add_dr_name(prefix, given, person_id, connpsql):
    use = "U"
    SQL= "INSERT INTO labsys_Name( given, prefix, practitioner_id, use) VALUES (%s, %s, %s, %s)" # Note: no quotes
    data= (given,   prefix, person_id, use )
    curpsql = connpsql.cursor()
    curpsql.execute(SQL, data) # Note: no % operator
    connpsql.commit()

def add_pt_name( given, lname,  patient_id, connpsql):
    use = "U"
    SQL= "INSERT INTO labsys_Name( given, family, patient_id, use) VALUES (%s, %s, %s, %s)" # Note: no quotes
    data= ( given, lname, patient_id, use )
    curpsql = connpsql.cursor()
    curpsql.execute(SQL, data) # Note: no % operator
    connpsql.commit()

# save to Telecom Table and link it to person
def add_telecom(value,use, system, person_id, connpsql):
    SQL= "INSERT INTO labsys_Telecom(use, value, system, practitioner_id) VALUES (%s, %s, %s, %s)" # Note: no quotes
    data= (use, value, system, person_id)
    curpsql = connpsql.cursor()
    curpsql.execute(SQL, data) # Note: no % operator
    connpsql.commit()

# save to address Table and link it to person if it has value
def add_address(text, line, postalcode, person_id, connpsql):
    SQL= "INSERT INTO labsys_Address(use, text, line,city, district,state, postalcode, country, practitioner_id) VALUES (%s,%s,%s, %s, %s, %s, %s, %s, %s)" # Note: no quotes
    data= ("W", text, line,"Ahmedabad", "Ahmedabad","Gujarat",postalcode, "India", person_id)
    curpsql = connpsql.cursor()
    curpsql.execute(SQL, data) # Note: no % operator
    connpsql.commit()

#Find or add observationdefination from TBLab (not from MST PLIS)
def find_or_add_obdef(test, connpsql):
    curpsql = connpsql.cursor()
    for key, value in test.items():
        print(key, " : ", value)
    print("____________")
    
    #print(test)
    curpsql.execute("SELECT * from labsys_ObservationDefinition WHERE test = %s", ((test["Test"],)))
    obdef = curpsql.fetchone()
    print(f"obdef {obdef}")
    if obdef:
        print("ObDef Already in Database")     
        obdefid = obdef[8]
        curpsql.close()      
        return obdefid
    else:
        print("New ObDef Added")
        SQL = "INSERT INTO labsys_ObservationDefinition(test, alias,options,  formula, vrule, vmsg,  alias_sms, is_calculated, tat,vrulemust) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s,%s) RETURNING id"
        obdef_test = test["Test"]
        alias = test["TestID"] or None
        options = test["Options"] or None
        #equipment = test["Analyzer"] or None
        formula = test["Formula"] or None
        vrule = test["VRule"] or None
        vmsg = test["VMsg"] or None
        alias_sms = test["Test4SMS"] or None
        is_calculated = test["CalcTest"] or None
        tat = test["TATinMM"] or None
        vrulemust = test["VRuleMust"] or None

        data = (obdef_test , alias, options,  formula, vrule , vmsg, alias_sms, is_calculated, tat, vrulemust)
        curpsql = connpsql.cursor()
        curpsql.execute(SQL, data) # Note: no % operator
        connpsql.commit()
        obdef_id = curpsql.fetchone()[0]
        curpsql.close()
        return obdef_id
    
def find_or_add_patient(fname, mname, lname, gender, age, dor, mobile, email, connpsql):
    given = fname.strip() + " " + mname.strip()
    curpsql = connpsql.cursor()
    #print(given)
    curpsql.execute("SELECT * from labsys_Name WHERE family = %s AND given = %s", (lname, given))
    name = curpsql.fetchone()
    #print(name)
    if name:
        print("Patient Already in Database")       
        patient_id = name[8]
        curpsql.close()      
        return patient_id
    else:
        print("New Patient Added")
        SQL = "INSERT INTO labsys_Patient(gender, birthdate, active) VALUES ( %s, %s, %s) RETURNING id"
        year = dor.year - age
        birthdate = datetime.date(int(year), 1, 1)
        data = (gender , birthdate, True)
        curpsql = connpsql.cursor()
        curpsql.execute(SQL, data) # Note: no % operator
        patient_id = curpsql.fetchone()[0]
        connpsql.commit()
        curpsql.close()
        add_pt_name( given, lname,  patient_id, connpsql)
        add_telecom(mobile,"M", "P", patient_id, connpsql)
        add_telecom(email, "H", "E", patient_id, connpsql)
        # get last saved Practitioner id for name and address and communication table ref id
        return patient_id

def find_of_add_refdoc(ref_dr_dic, connpsql):

    curpsql = connpsql.cursor()
    curpsql.execute("SELECT * from labsys_Name WHERE given = %s", (ref_dr_dic["DrName"],))
    name = curpsql.fetchone()
    if name:
        print("RefDr Already in Database ")
        #print(type(name))
        practitioner_id = name[9]
        curpsql.close()
        return practitioner_id
    else:
        print("New Ref Dr Added")
        qualification = ref_dr_dic["Degree"] or "Not Defined"
            # Create new pratitior object by inserting it in Practitioner table and get it's practitioner_id as return value
        practitioner_id = create_practitioner(qualification, connpsql)

        # save to Name Table and link it to practitioner        
        prefix =  ref_dr_dic["Title"] or ""
        given= ref_dr_dic["DrName"] or ""
        add_dr_name(prefix, given, practitioner_id, connpsql)

        # save to Telecom Table mobile number and link it to practitioner if it has value
        if ref_dr_dic["Mobile"]:
            value= ref_dr_dic["Mobile"]
            use = "M"
            add_telecom(value,use, "P",practitioner_id, connpsql)

        # save to Telecom Table office number and link it to practitioner if it has value
        if ref_dr_dic["PhHosp"]:
            value= ref_dr_dic["PhHosp"]
            use = "W"
            add_telecom(value,use,"P", practitioner_id, connpsql)

        # save to Telecom Table home number and link it to practitioner if it has value
        if ref_dr_dic["PhResi"]:
            value= ref_dr_dic["PhResi"]
            use = "H"
            add_telecom(value,use,"P", practitioner_id, connpsql)

        # save to Telecom Table e mail  and link it to practitioner if it has value
        if ref_dr_dic["Email"]:
            value= ref_dr_dic["Email"]
            use = "H"
            add_telecom(value,use,"E", practitioner_id, connpsql)


        # save to address Table and link it to practitioner if it has value
        if ref_dr_dic["Address"]:
            text = ref_dr_dic["Address"] 
            line = ref_dr_dic["Area"] or ""
            postalcode = ref_dr_dic["PIN"]
            add_address(text, line, postalcode, practitioner_id, connpsql)
        return practitioner_id 
         
# Create new pratitior object by inserting it in Practitioner table and retrun it's practitioner id usiing RETURNING KEY in sql
def create_practitioner(qualification, connpsql):
        SQL = "INSERT INTO labsys_Practitioner(qualification, active ) VALUES ( %s, %s) RETURNING id" # Note: no quotes
        data = (qualification , True)
        curpsql = connpsql.cursor()
        curpsql.execute(SQL, data) # Note: no % operator
        practitioner_id = curpsql.fetchone()[0]
        connpsql.commit()
        curpsql.close()
        # get last saved Practitioner id for name and address and communication table ref id
        return practitioner_id


"""
def insert_name(name):
    # insert a new vendor into the vendors table #
    sql = "INSERT INTO labsys_Name (name) VALUES(%s) RETURNING name_id;"
    conn = None
    vendor_id = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(host="122.179.129.85", database="labsys", user="postgres", password="your_password")
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (name,))
        # get the generated id back
        name_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return name_id

"""

