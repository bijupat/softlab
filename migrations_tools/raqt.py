import pymssql
import psycopg2
from sys import exit
import datetime

try:
    conn = pymssql.connect(server= '192.168.102.150', user = 'SA', password = 'LETMEIN', database = 'RAQT2021_22',as_dict=True,)
except(Exception) as error:
    print("cannot connect with MSSQL WITH error as below:")
    exit(error)

cur = conn.cursor()
#cur.execute("SELECT top(10) * FROM Tbllab WHERE RefDr = 1 ORDER BY dor DESC")
# RefDr  = 1 indicate self
cur.execute("SELECT * FROM Tbllab WHERE RefDr = 1 ORDER  BY dor DESC")

for pt in cur.fetchall():
    labkey= pt["LabKey"]
    dor= pt["DOR"]
    prefix= pt["Prefix"]
    labno= pt["LabNo"]
    suffix= pt["Suffix"]
    patid= pt["PatID"]
    fname= pt["FName"]
    mname = pt["MName"]
    lname= pt["LName"]
    patname= pt["PatName"]
    sex= pt["Sex"]
    if pt["Age"]:
        age= round(pt["Age"])
    else:
        age =pt["Age"]
    ageunit= pt["AgeUnit"]
    acckey= pt["AccKey"]
    plkey= pt["PLKey"]
    sfkey= pt["SFKey"]
    addr= pt["Addr"]
    place= pt["Place"]
    sendby= pt["SendBy"]
    urgent= pt["Urgent"]
    disc= pt["Disc"]
    discby= pt["DiscBy"]
    discnote= pt["DiscNote"]
    notes= pt["Notes"]
    opr= pt["OPR"]
    refid= pt["RefID"]
    phone= pt["Phone"]
    refdr= pt["RefDr"]
    refdr2= pt["RefDr2"]
    foc= pt["FOC"]
    periodic= pt["Periodic"]
    comm= pt["Comm"]
    mobile4sms= pt["Mobile4SMS"]
    smsresults= pt["SMSResults"]
    email= pt["Email"]
    deductamt= pt["DeductAmt"]
    companion= pt["Companion"]
    rel2pat= pt["Rel2Pat"]
    billno= pt["BillNo"]
    billprinted= pt["BillPrinted"]
    sampno= pt["SampNo"]
    labrefno= pt["LabRefNo"]
    incent2name= pt["Incent2Name"]
    incent2per= pt["Incent2Per"]
    key4graph= pt["Key4Graph"]
    pattitle= pt["PatTitle"]
    extopdno= pt["ExtOPDNo"]
    extipdno= pt["ExtIPDNo"]
    extreqno= pt["ExtReqNo"]
    extbillno= pt["ExtBillNo"]
    extpatcatg= pt["ExtPatCatg"]
    extsmpcoldt= pt["ExtSmpColDt"]
    extother= pt["ExtOther"]
    salesrep= pt["SalesRep"]
    reporeadysmssent= pt["RepoReadySMSSent"]
    testresultsmssent= pt["TestResultSMSSent"]
    whatsapp = f'wa.me/91{phone}'
    if foc:
        payment = "FOC"
    else:
        if disc:
            payment = "Discount"
        else:
            payment = "Fully Paid"     

    if phone:
        cur.execute("SELECT * FROM Mstdr WHERE mstdrkey = %s", refdr)
        ref_dr_dict = cur.fetchone()
        investigations = ""

        cur.execute("SELECT * FROM Tblinv WHERE labkey = %s", labkey)
        for inv in cur.fetchall():
            investigations = investigations + ": " + inv['Item']



        

        print(f"{dor},{sampno},{patname},{age} {ageunit},{sex},{phone}, {whatsapp},{payment} {discnote}, {ref_dr_dict['DrName']}, {investigations}, {addr}, {notes}")

