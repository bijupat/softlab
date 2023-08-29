from func import connect_psql, connect_mssql
import datetime


def main():
    # Connect to an existing psql database
    connpsql = connect_psql()
    #Open a cursor to perform database operations
    curpsql = connpsql.cursor()

    # Connect to an existing mssql database
    connmssql = connect_mssql()

    #Open a cursor to perform database operations
    curmssql = connmssql.cursor()
    curmssql.execute("SELECT top(6) * FROM Mstplitems")
    #curmssql.execute("SELECT * FROM Mstplitems WHERE Item = 'Max life CAT 1'" )
    for pli in curmssql.fetchall():
        curpsql.execute("SELECT * from labsys_ChargeItemDefinition WHERE title = %s", (pli["Item"],))
        item = curpsql.fetchone()            
        if not item:
            title = pli["Item"] #item 
            value = pli["Rate"] #rate
            print_in_receipt = pli["PrintInRecp"] #printinrecp
            alias = pli["ShortName"] #shortname
            created = datetime.datetime.now() # add present time date to avoid not null contrain on created column
            status = 'active'
            experimental = False
            is_profile = False
            Note = f"Note for chargeitem {title}"
            
            SQL = "INSERT INTO labsys_ChargeItemDefinition (title, value, print_in_receipt, alias, created, status, experimental, is_profile ) VALUES ( %s, %s , %s, %s, %s, %s, %s, %s) RETURNING id" # Note: no quotes
            data = (title, value, print_in_receipt, alias , created, status, experimental, is_profile, )
            curpsql.execute(SQL, data) # Note: no % operator
            chargeitemdefid = curpsql.fetchone()[0]
            connpsql.commit()
            #add mapping to labsys_chargeitemdefinition_observations tabel  chargeitemid(one) to observationids(many)
            curmssql.execute("SELECT * FROM Mstitemrepotests WHERE mstitemkey = %s ", pli["mstItemKey"])            
            for pairs in curmssql.fetchall():
                curmssql.execute("SELECT * FROM Msttests WHERE msttestkey = %s ", pairs["mstTestKey"])
                for test in curmssql.fetchall():
                    try:
                        curpsql.execute("INSERT INTO labsys_chargeitemdefinition_observations (chargeitemdefinition_id, observationdefinition_id) VALUES (%s, %s)", (chargeitemdefid, f_or_a_odef(test,connpsql)))
                    except:
                        print(f"{title} has not added observation {test['Test']}")
            print (f'{title} added successfully')
        else:
            print (f'{pli["Item"]} already there ')


            #curmssql.execute("SELECT  * FROM Mstpl WHERE mstplkey = %s", pli["mstPLKey"])
            #for repo in curmssql.fetchall():
                #print(repo)



        """
        {'mstRepoTestKey': 1, 'mstRepoKey': 1, 'mstTestKey': 598, 'EOrder': 0, 'Formula': '', 'VRule': '', 'VMsg': ''}
        {'mstItemKey': 9728, 'mstPLKey': 29, 'Item': 'FBS/PG2BS', 'Rate': 50, 'Collection': 'FBSFL;URINE;PG2BSFL;URINE', 
            'PrintInRecp': True, 'ShortName': 'FBS/PG2BS', 'ItemCode': '', 'Category': 3, 'Outsourced': False, 'RepoFreq': '', 
            'RepoCollTime': '', 'OutSrcTo': '', 'TubeColors': '8421504,16711935,7303023,16744703,,,,'}
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
    try:
        connpsql.close()
        connmssql.close()
        print('Finally, BOTH connection closed.')
    except(Exception) as error:
        print(f"cannot close one or both connection because : {error}")
# find or add observation defination and return obdefid
def f_or_a_odef(test,connpsql):
    curpsql = connpsql.cursor()
    curpsql.execute("SELECT * from labsys_ObservationDefinition WHERE test = %s", ((test["Test"],)))
    obdef = curpsql.fetchone()
    print(f"obdef {obdef}")
    if obdef:
        print("ObDef Already in Database")     
        obdefid = obdef[0]
        curpsql.close()      
        return obdefid
    else:
        Test = test['Test']
        Default_value = test['Result']
        Options = test['Options']
        Unit = test['Unit']
        Alias_sms = test['Test4SMS']
        tat = test['TATinMM']
        Formula = test['Formula']
        Vrule = test['VRule']
        Vmsg = test['VMsg']
        Vrulemust = test['VRuleMust']
        SQL = "INSERT INTO labsys_ObservationDefinition (Test, Default_value, Options, Unit, Alias_sms, Tat, Formula, Vrule, Vmsg, Vrulemust) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id" # Note: no quotes
        data = (Test, Default_value, Options, Unit, Alias_sms, tat, Formula, Vrule, Vmsg, Vrulemust )
        curpsql.execute(SQL, data) # Note: no % operator
        obdefid = curpsql.fetchone()[0]
        connpsql.commit()
        print (f'{Test} added successfully as {data}')
        return obdefid

#{'mstTestKey': 1, , 'TestID': 'vol',  'Analyzer': '', 'AnaTest': '', 'Dept': 'GEN', 'Location': None, 'PrintInCard': True, 'Normals': '',  'Visible2All': True,  'VRule': None, 'VMsg': None, 'VRuleMust': None}

if __name__ == "__main__":
    main()