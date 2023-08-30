

class Msttests(models.Model):
    msttestkey = models.AutoField(db_column='mstTestKey', primary_key=True)  # Field name made lowercase.
    test = models.CharField(db_column='Test', max_length=100)  # Field name made lowercase.
    testid = models.CharField(db_column='TestID', unique=True, max_length=10)  # Field name made lowercase.
    result = models.CharField(db_column='Result', max_length=180)  # Field name made lowercase.
    options = models.CharField(db_column='Options', max_length=5000)  # Field name made lowercase.
    analyzer = models.CharField(db_column='Analyzer', max_length=10)  # Field name made lowercase.
    anatest = models.CharField(db_column='AnaTest', max_length=10)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20)  # Field name made lowercase.
    dept = models.ForeignKey(Mstdept, models.DO_NOTHING, db_column='Dept')  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=10, blank=True, null=True)  # Field name made lowercase.
    printincard = models.BooleanField(db_column='PrintInCard')  # Field name made lowercase.
    normals = models.CharField(db_column='Normals', max_length=100)  # Field name made lowercase.
    test4sms = models.CharField(db_column='Test4SMS', max_length=50)  # Field name made lowercase.
    visible2all = models.BooleanField(db_column='Visible2All')  # Field name made lowercase.
    tatinmm = models.SmallIntegerField(db_column='TATinMM')  # Field name made lowercase.
    formula = models.CharField(db_column='Formula', max_length=200, blank=True, null=True)  # Field name made lowercase.
    vrule = models.CharField(db_column='VRule', max_length=200, blank=True, null=True)  # Field name made lowercase.
    vmsg = models.CharField(db_column='VMsg', max_length=30, blank=True, null=True)  # Validation Message.
    vrulemust = models.BooleanField(db_column='VRuleMust', blank=True, null=True)  # Validation if must ?.

    class Meta:
        managed = False
        db_table = 'mstTests'


{'mstTestKey': 1, 'Test': 'Volume', 'TestID': 'vol', 'Result': '', 'Options': '', 'Analyzer': '', 'AnaTest': '', 'Unit': '', 'Dept': 'GEN', 'Location': None, 'PrintInCard': True, 'Normals': '', 'Test4SMS': '', 'Visible2All': True, 'TATinMM': 30, 'Formula': None, 'VRule': None, 'VMsg': None, 'VRuleMust': None}
{'mstTestKey': 2, 'Test': 'BILI  (Bile Pigment)', 'TestID': 'bp', 'Result': '', 'Options': 'N|Nil  |P|Present', 'Analyzer': '', 'AnaTest': '', 'Unit': '', 'Dept': 'CL PATH', 'Location': None, 'PrintInCard': True, 'Normals': '', 'Test4SMS': 'Urine--BP', 'Visible2All': True, 'TATinMM': 30, 'Formula': None, 'VRule': None, 'VMsg': None, 'VRuleMust': None}
{'mstTestKey': 3, 'Test': 'Crystals', 'TestID': 'crystals', 'Result': '', 'Options': 'CA|Ca Oxalate*|U|Urate*|TP|Tripple Phosphate*|A|Absent', 'Analyzer': '', 'AnaTest': '', 'Unit': '', 'Dept': 'CL PATH', 'Location': None, 'PrintInCard': False, 'Normals': '', 'Test4SMS': '', 'Visible2All': True, 'TATinMM': 0, 'Formula': None, 'VRule': None, 'VMsg': None, 'VRuleMust': None}
{'mstTestKey': 4, 'Test': 'Quantity', 'TestID': 'qty', 'Result': '', 'Options': '', 'Analyzer': '', 'AnaTest': '', 'Unit': '', 'Dept': 'CL PATH', 'Location': None, 'PrintInCard': True, 'Normals': '', 'Test4SMS': '', 'Visible2All': True, 'TATinMM': 0, 'Formula': None, 'VRule': None, 'VMsg': None, 'VRuleMust': None}
{'mstTestKey': 5, 'Test': 'Consistency', 'TestID': 'cons', 'Result': 'Semi solid', 'Options': 'A|Liquid|B|Hard|C|Semisoft|D|Soft', 'Analyzer': '', 'AnaTest': '', 'Unit': '', 'Dept': 'CL PATH', 'Location': None, 'PrintInCard': False, 'Normals': '', 'Test4SMS': '', 'Visible2All': True, 'TATinMM': 0, 'Formula': None, 'VRule': None, 'VMsg': None, 'VRuleMust': None}
{'mstTestKey': 6, 'Test': 'Mucus', 'TestID': 'mucus', 'Result': 'Absent', 'Options': 'A|Absent|P|Present*', 'Analyzer': '', 'AnaTest': '', 'Unit': '', 'Dept': 'CL PATH', 'Location': None, 'PrintInCard': True, 'Normals': '', 'Test4SMS': '', 'Visible2All': True, 'TATinMM': 0, 'Formula': None, 'VRule': None, 'VMsg': None, 'VRuleMust': None}
{'mstTestKey': 7, 'Test': 'Blood', 'TestID': 'blood', 'Result': 'Absent', 'Options': 'P|Present*|A|Absent', 'Analyzer': '', 'AnaTest': '', 'Unit': '', 'Dept': 'CL PATH', 'Location': None, 'PrintInCard': False, 'Normals': '', 'Test4SMS': '', 'Visible2All': True, 'TATinMM': 0, 'Formula': None, 'VRule': None, 'VMsg': None, 'VRuleMust': None}
{'mstTestKey': 8, 'Test': 'Parasites', 'TestID': 'parasites', 'Result': 'Absent', 'Options': 'A|Absent', 'Analyzer': '', 'AnaTest': '', 'Unit': '', 'Dept': 'CL PATH', 'Location': None, 'PrintInCard': False, 'Normals': '', 'Test4SMS': '', 'Visible2All': True, 'TATinMM': 0, 'Formula': None, 'VRule': None, 'VMsg': None, 'VRuleMust': None}
{'mstTestKey': 9, 'Test': 'Trophozoites', 'TestID': 'tropho', 'Result': 'Absent', 'Options': 'EH|E Histolytica', 'Analyzer': '', 'AnaTest': '', 'Unit': '', 'Dept': 'CL PATH', 'Location': None, 'PrintInCard': False, 'Normals': '', 'Test4SMS': '', 'Visible2All': True, 'TATinMM': 0, 'Formula': None, 'VRule': None, 'VMsg': None, 'VRuleMust': None}
{'mstTestKey': 10, 'Test': 'Ova', 'TestID': 'ova', 'Result': 'Absent', 'Options': '', 'Analyzer': '', 'AnaTest': '', 'Unit': '', 'Dept': 'CL PATH', 'Location': None, 'PrintInCard': False, 'Normals': '', 'Test4SMS': '', 'Visible2All': True, 'TATinMM': 0, 'Formula': None, 'VRule': None, 'VMsg': None, 'VRuleMust': None}

class Mstplitems(models.Model):
    mstitemkey = models.AutoField(db_column='mstItemKey', primary_key=True)  # Field name made lowercase.
    mstplkey = models.ForeignKey(Mstpl, models.DO_NOTHING, db_column='mstPLKey')  # Field name made lowercase.
    item = models.CharField(db_column='Item', max_length=60)  # Field name made lowercase.
    rate = models.SmallIntegerField(db_column='Rate')  # Field name made lowercase.
    collection = models.CharField(db_column='Collection', max_length=120)  # Field name made lowercase.
    printinrecp = models.BooleanField(db_column='PrintInRecp')  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=10)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    category = models.ForeignKey(Mstitemcategory, models.DO_NOTHING, db_column='Category')  # Field name made lowercase.
    outsourced = models.BooleanField(db_column='Outsourced')  # Field name made lowercase.
    repofreq = models.CharField(db_column='RepoFreq', max_length=80)  # Field name made lowercase.
    repocolltime = models.CharField(db_column='RepoCollTime', max_length=80)  # Field name made lowercase.
    outsrcto = models.CharField(db_column='OutSrcTo', max_length=50)  # Field name made lowercase.
    tubecolors = models.CharField(db_column='TubeColors', max_length=70)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstPLItems'
        unique_together = (('mstplkey', 'shortname'),)

{'mstItemKey': 9728, 'mstPLKey': 29, 'Item': 'FBS/PG2BS', 'Rate': 50, 'Collection': 'FBSFL;URINE;PG2BSFL;URINE', 'PrintInRecp': True, 'ShortName': 'FBS/PG2BS', 'ItemCode': '', 'Category': 3, 'Outsourced': False, 'RepoFreq': '', 'RepoCollTime': '', 'OutSrcTo': '', 'TubeColors': '8421504,16711935,7303023,16744703,,,,'}
{'mstItemKey': 9729, 'mstPLKey': 29, 'Item': 'PG2BS', 'Rate': 50, 'Collection': 'PG2BSFL;URINE', 'PrintInRecp': True, 'ShortName': 'PG2BS', 'ItemCode': '', 'Category': 3, 'Outsourced': False, 'RepoFreq': '', 'RepoCollTime': '', 'OutSrcTo': '', 'TubeColors': '8421504,16711935,,,,,,'}
{'mstItemKey': 9731, 'mstPLKey': 29, 'Item': 'HDL Cholesterol', 'Rate': 150, 'Collection': 'SERUM', 'PrintInRecp': True, 'ShortName': 'HDL', 'ItemCode': '', 'Category': 3, 'Outsourced': False, 'RepoFreq': '', 'RepoCollTime': '', 'OutSrcTo': '', 'TubeColors': '255,,,,,,,'}
{'mstItemKey': 9733, 'mstPLKey': 29, 'Item': 'Max life CAT 1', 'Rate': 125, 'Collection': 'MER', 'PrintInRecp': True, 'ShortName': 'MER.', 'ItemCode': '', 'Category': 10, 'Outsourced': True, 'RepoFreq': '', 'RepoCollTime': '', 'OutSrcTo': 'SHILPA PATEL', 'TubeColors': '65280,,,,,,,'}
{'mstItemKey': 9734, 'mstPLKey': 29, 'Item': 'MAX LIFE CAT 2', 'Rate': 170, 'Collection': 'WBEDTA;MER;ESR', 'PrintInRecp': True, 'ShortName': 'CAT 2', 'ItemCode': '', 'Category': 10, 'Outsourced': False, 'RepoFreq': '', 'RepoCollTime': '', 'OutSrcTo': '', 'TubeColors': '16711808,65280,0,,,,,'}
{'mstItemKey': 9735, 'mstPLKey': 29, 'Item': 'MAX LIFE CAT 3', 'Rate': 1060, 'Collection': 'WBEDTA;PLAIN;MER', 'PrintInRecp': True, 'ShortName': 'CAT 3', 'ItemCode': '', 'Category': 10, 'Outsourced': True, 'RepoFreq': '', 'RepoCollTime': '', 'OutSrcTo': 'SHILPA PATEL', 'TubeColors': '16711808,255,65280,,,,,'}
{'mstItemKey': 9736, 'mstPLKey': 29, 'Item': 'MAX LIFE CAT 4', 'Rate': 1190, 'Collection': 'SERUM;MER;ECG;URINE', 'PrintInRecp': True, 'ShortName': 'CAT 4', 'ItemCode': '', 'Category': 10, 'Outsourced': True, 'RepoFreq': '', 'RepoCollTime': '', 'OutSrcTo': 'SHILPA PATEL', 'TubeColors': '255,65280,65535,16711935,,,,'}
{'mstItemKey': 9737, 'mstPLKey': 29, 'Item': 'MAX LIFE CAT 5', 'Rate': 1050, 'Collection': 'WBEDTA;SERUM;URINE;MER;ECG', 'PrintInRecp': True, 'ShortName': 'CAT 5', 'ItemCode': '', 'Category': 10, 'Outsourced': False, 'RepoFreq': '', 'RepoCollTime': '', 'OutSrcTo': '', 'TubeColors': '16711808,255,16711935,65280,65535,,,'}
{'mstItemKey': 9738, 'mstPLKey': 29, 'Item': 'L & T Gen Set II (Prime)', 'Rate': 870, 'Collection': 'WBEDTA;SERUM;URINE;ESR;MER;ECG', 'PrintInRecp': True, 'ShortName': 'L&T SET II', 'ItemCode': '', 'Category': 10, 'Outsourced': False, 'RepoFreq': '', 'RepoCollTime': '', 'OutSrcTo': '', 'TubeColors': '16711808,255,16711935,0,65280,65535,,'}
{'mstItemKey': 9740, 'mstPLKey': 29, 'Item': 'ApolloMunich Cat 1', 'Rate': 630, 'Collection': 'WBEDTA;SERUM;URINE;MER;EGC', 'PrintInRecp': True, 'ShortName': 'ApMun cat1', 'ItemCode': '', 'Category': 10, 'Outsourced': False, 'RepoFreq': '', 'RepoCollTime': '', 'OutSrcTo': '', 'TubeColors': '16711808,255,16711935,65280,65535,,,'}

class Mstitemrepotests(models.Model):
    mstitemkey = models.ForeignKey('Mstplitems', models.DO_NOTHING, db_column='mstItemKey', primary_key=True)  # Field name made lowercase.
    msttestkey = models.ForeignKey('Msttests', models.DO_NOTHING, db_column='mstTestKey')  # Field name made lowercase.
    mstrepokey = models.ForeignKey('Mstrepo', models.DO_NOTHING, db_column='mstRepoKey')  # Field name made lowercase.
    eorder = models.SmallIntegerField(db_column='EOrder')  # Field name made lowercase.
    formula = models.CharField(db_column='Formula', max_length=150)  # Field name made lowercase.
    vrule = models.CharField(db_column='VRule', max_length=150)  # Field name made lowercase.
    vmsg = models.CharField(db_column='VMsg', max_length=20)  # Field name made lowercase.
    vrulemust = models.BooleanField(db_column='VRuleMust')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstItemRepoTests'
        unique_together = (('mstitemkey', 'msttestkey', 'mstrepokey'),)
        
{'mstItemKey': 8854, 'mstTestKey': 186, 'mstRepoKey': 103, 'EOrder': 1, 'Formula': '', 'VRule': '', 'VMsg': '', 'VRuleMust': False}
{'mstItemKey': 8854, 'mstTestKey': 678, 'mstRepoKey': 1, 'EOrder': 2, 'Formula': '', 'VRule': '', 'VMsg': '', 'VRuleMust': False}
{'mstItemKey': 8854, 'mstTestKey': 706, 'mstRepoKey': 1, 'EOrder': 24, 'Formula': '', 'VRule': '', 'VMsg': '', 'VRuleMust': False}
{'mstItemKey': 8854, 'mstTestKey': 187, 'mstRepoKey': 103, 'EOrder': 20, 'Formula': '', 'VRule': '[pc]>150000 and [pc]<500000', 'VMsg': 'IS PLATELASE NORMAL', 'VRuleMust': False}
{'mstItemKey': 8854, 'mstTestKey': 188, 'mstRepoKey': 103, 'EOrder': 21, 'Formula': '', 'VRule': '', 'VMsg': '', 'VRuleMust': False}
{'mstItemKey': 8854, 'mstTestKey': 189, 'mstRepoKey': 103, 'EOrder': 15, 'Formula': '', 'VRule': '[hb]>8 and [mcv]>76 and [mch]>21', 'VMsg': 'check hb or mch', 'VRuleMust': False}
{'mstItemKey': 8854, 'mstTestKey': 190, 'mstRepoKey': 103, 'EOrder': 16, 'Formula': '', 'VRule': '', 'VMsg': '', 'VRuleMust': False}
{'mstItemKey': 8854, 'mstTestKey': 191, 'mstRepoKey': 103, 'EOrder': 17, 'Formula': '', 'VRule': '', 'VMsg': '', 'VRuleMust': False}
{'mstItemKey': 8854, 'mstTestKey': 223, 'mstRepoKey': 103, 'EOrder': 12, 'Formula': '100-([poly]+[lymp]+[eosi])', 'VRule': '', 'VMsg': '', 'VRuleMust': False}
{'mstItemKey': 8854, 'mstTestKey': 514, 'mstRepoKey': 103, 'EOrder': 13, 'Formula': '', 'VRule': '[poly]+[lymp]+[eosi]+[mono]+[baso]=100', 'VMsg': 'DC total is not 100!', 'VRuleMust': False}



class Mstrepo(models.Model):
    mstrepokey = models.AutoField(db_column='mstRepoKey', primary_key=True)  # Field name made lowercase.
    repoid = models.CharField(db_column='RepoID', unique=True, max_length=10)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    rtfdata = models.TextField(db_column='RTFData')  # Field name made lowercase. This field type is a guess.
    repogrpkey = models.ForeignKey('Mstrepogrp', models.DO_NOTHING, db_column='RepoGrpKey')  # Field name made lowercase.
    printhisto = models.BooleanField(db_column='PrintHisto')  # Field name made lowercase.
    includeheader = models.BooleanField(db_column='IncludeHeader')  # Field name made lowercase.
    includefooter = models.BooleanField(db_column='IncludeFooter')  # Field name made lowercase.
    tatinmm = models.SmallIntegerField(db_column='TATinMM')  # Field name made lowercase.
    samplename = models.CharField(db_column='SampleName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    autoverify = models.BooleanField(db_column='AutoVerify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstRepo'
{'mstRepoKey': 1, 'RepoID': '500', 'Title': 'URINE ANALYSIS', 'RTFData': '{\\rtf1\\ansi\\ansicpg1252\\deff0\\deflang1033{\\fonttbl{\\f0\\fswiss\\fprq2\\fcharset0 Trebuchet MS;}{\\f1\\fswiss\\fprq2\\fcharset0 Arial;}{\\f2\\fswiss\\fprq2\\fcharset0 Garamond;}{\\f3\\fnil\\fcharset0 Arial;}}\r\n{\\colortbl ;\\red0\\green0\\blue0;}\r\n\\viewkind4\\uc1\\pard\\qc\\tx1440\\tx3960\\tx5760\\tx7200\\cf1\\ul\\f0\\fs24 ROUTINE URINE EXAMINATION\r\n\\par \\pard\\tx1440\\tx3960\\tx5760\\tx7200\\ulnone\\f1\\fs16 \r\n\\par \\pard\\ri720\\tx1440\\tx3960\\tx5760\\tx7200\\ul\\b\\fs20 PHYSICAL\\ulnone\\tab\\ul\\f2\\{speci\\}\\ulnone\\b0 , \\ul\\b\\{vol\\}\\ulnone\\b0  mL, \\ul\\b\\{color\\}\\ulnone\\b0 , \\ul\\b\\{trans\\}\\ulnone\\b0  urine sample received  $vol$ \r\n\\par \\tab having  \\ul\\b\\{sp\\}\\ulnone\\b0  Sp. Gravity and \\ul\\b\\{uph\\}\\ulnone\\b0  pH  $sp$ \\b \r\n\\par \\pard\\tx1440\\tx3960\\tx5760\\tx7200\\b0\\f1\\fs16 \r\n\\par \\ul\\b\\fs20 CHEMICAL\\ulnone\\b0\\tab\\f2 :Protein\\tab\\{albu\\}\\tab mg/dL\\tab < 15 \\tab\\tab $albu$ \r\n\\par \\tab Glucose\\tab\\{rus\\}\\tab mg/dL\\tab < 30\\tab  \\tab $rus$ \r\n\\par \\tab Bile Salts\\tab\\{bs\\}\\tab\\tab\\tab\\tab\\tab $bs$ \r\n\\par \\tab Bile Pigments(Bilirubin)\\tab\\{bp\\}\\tab\\tab\\tab\\tab\\tab  $bp$ \r\n\\par \\tab Ketone\\tab\\{uace\\}\\tab mg/dL\\tab < 10\\tab\\tab   $uace$  \r\n\\par \\tab Urobilinogens\\tab\\{urobill\\}\\tab mg/dL\\tab < 2\\tab\\tab  $urobill$ \r\n\\par \\tab Nitrite\\tab\\{unit\\}\\tab\\tab Absent\\tab\\tab  $unit$ \r\n\\par \\tab Pus Cells(Leucocytes)\\tab\\{leu\\} \\tab Cell / microL\\tab < 10\\tab $bacteria$\r\n\\par \\tab Red Cells\\tab\\{urbc\\}\\tab Cell / microL\\tab < 5\\tab $bacteria$ \r\n\\par \\f1\\fs16 \r\n\\par \\ul\\b\\fs20 MICROSCOPIC EXAMINATION (After centrifugation at 2000 r.p.m. for 5 minutes) \r\n\\par \\ulnone\\b0\\tab\\f2 Reveals NO clinically significant formed elements except\\tab\\tab\\tab   \r\n\\par \\tab Pus Cells\\tab\\{pus\\}  \\tab /H.P.F.\\tab   $pus$\r\n\\par \\tab Red Cells\\tab\\{redcells\\}  \\tab /H.P.F.\\tab    $redcells$ \r\n\\par \\tab Epithelial Cells\\tab\\{epithelial\\} \\tab /H.P.F.\\tab    $epithelial$ \r\n\\par \\tab Casts\\tab\\{casts\\}\\tab   $casts$\r\n\\par \\tab Crystals\\tab\\{crystals\\}\\tab   $crystals$\r\n\\par \\tab Amorphous\\tab\\{amorp\\}\\tab   $amorp$\r\n\\par \\tab Fungus\\tab\\{fung\\}\\tab    $fung$ \r\n\\par \\tab T. Vaginalis\\tab\\{vaginalis\\}\\tab   $vaginalis$\r\n\\par \\tab Bacterias\\tab\\{bacteria\\}\\tab  $bacteria$ \\cf0\\ul\\b\\f3\\fs28 \r\n\\par }\r\n', 'RepoGrpKey': 9, 'PrintHisto': False, 'IncludeHeader': True, 'IncludeFooter': True, 'TATinMM': 30, 'SampleName': None, 'AutoVerify': False}
{'mstRepoKey': 2, 'RepoID': '2', 'Title': 'LIPID PRIOFILE', 'RTFData': '{\\rtf1\\ansi\\ansicpg1252\\deff0\\deflang1033{\\fonttbl{\\f0\\fnil\\fcharset0 Trebuchet MS;}{\\f1\\fnil\\fcharset0 Garamond;}}\r\n{\\colortbl ;\\red0\\green0\\blue0;}\r\n\\viewkind4\\uc1\\pard\\qc\\tx720\\tx3600\\tx5760\\tx7200\\cf1\\ul\\f0\\fs24 LIPID PROFILE\r\n\\par \\pard\\tx720\\tx3600\\tx5760\\tx7200\\ulnone\\f1\\fs16 \r\n\\par \\fs22\\tab SAMPLE:\\{smptyp\\}\r\n\\par \\tab Serum Cholesterol\\tab :\\{cho\\}\\tab mg/dl\\tab <160 Excellent $cho$ \r\n\\par \\tab\\tab\\tab\\tab <200 Desirable $cho$ \r\n\\par \\tab\\tab\\tab\\tab 200-239 Boderline High $cho$ \r\n\\par \\tab\\tab\\tab\\tab >240 High $cho$ \r\n\\par \\tab Serum Triglyceride\\tab :\\{tri\\}\\tab mg/dl\\tab <150 Normal $tri$ \r\n\\par \\tab\\tab\\tab\\tab 150-199 Borderlin High $tri$ \r\n\\par \\tab\\tab\\tab\\tab 200-499 High $tri$ \r\n\\par \\tab\\tab\\tab\\tab >500 Very High $tri$ \r\n\\par \\tab S. HDL Cholesterol\\tab :\\{hdl\\}\\tab mg/dl\\tab <40 Low $hdl$ \r\n\\par \\tab (DIRECT HDL C)\\tab\\tab\\tab 60 & above Excellent $hdl$ \r\n\\par \\tab S. LDL Cholesterol\\tab :\\{ldl\\}\\tab mg/dl\\tab < 80 \\tab Excellent $ldl$ \r\n\\par \\tab (Caclulatory Value)\\tab\\tab\\tab < 100\\tab Optimal $ldl$ \r\n\\par \\tab\\tab\\tab\\tab 100-129 Near or above optimal $ldl$ \r\n\\par \\tab\\tab\\tab\\tab 130-159 Borderline high $ldl$ \r\n\\par \\tab\\tab\\tab\\tab 160-189 High $ldl$ \r\n\\par \\tab\\tab\\tab\\tab >190\\tab Very High $ldl$ \r\n\\par  \\tab S. VLDL Cholesterol\\tab :\\{vldl\\}\\tab mg/dl\\tab 15-30 mg/dL $vldl$ \r\n\\par \\tab Total Lipids\\tab :\\{totlip\\}\\tab mg/dl\\tab 400-1000 mg/dL $totlip$ \r\n\\par \\tab LDL/HDL CHO Ratio\\tab :\\{ldlhdl\\}\\tab\\tab Up to 3.5 $ldlhdl$ \r\n\\par \\tab T CHO/HDL CHO Ratio\\tab :\\{chohdl\\}      Noraml<4.5;Double Risk Up to 7; Three time risk up to 11 $chohdl$ \r\n\\par \\ul\\f0\\fs24 \r\n\\par }\r\n', 'RepoGrpKey': 9, 'PrintHisto': False, 'IncludeHeader': True, 'IncludeFooter': True, 'TATinMM': 0, 'SampleName': None, 'AutoVerify': False}


class Mstrepotests(models.Model):
    mstrepotestkey = models.AutoField(db_column='mstRepoTestKey', primary_key=True)  # Field name made lowercase.
    mstrepokey = models.ForeignKey(Mstrepo, models.DO_NOTHING, db_column='mstRepoKey')  # Field name made lowercase.
    msttestkey = models.ForeignKey('Msttests', models.DO_NOTHING, db_column='mstTestKey')  # Field name made lowercase.
    eorder = models.SmallIntegerField(db_column='EOrder')  # Field name made lowercase.
    formula = models.CharField(db_column='Formula', max_length=150)  # Field name made lowercase.
    vrule = models.CharField(db_column='VRule', max_length=150)  # Field name made lowercase.
    vmsg = models.CharField(db_column='VMsg', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstRepoTests'
        unique_together = (('mstrepokey', 'msttestkey'),)
{'mstRepoTestKey': 1, 'mstRepoKey': 1, 'mstTestKey': 598, 'EOrder': 0, 'Formula': '', 'VRule': '', 'VMsg': ''}
{'mstRepoTestKey': 2, 'mstRepoKey': 1, 'mstTestKey': 1, 'EOrder': 1, 'Formula': '', 'VRule': '', 'VMsg': ''}
{'mstRepoTestKey': 3, 'mstRepoKey': 1, 'mstTestKey': 678, 'EOrder': 2, 'Formula': '', 'VRule': '', 'VMsg': ''}
{'mstRepoTestKey': 4, 'mstRepoKey': 1, 'mstTestKey': 233, 'EOrder': 3, 'Formula': '', 'VRule': '', 'VMsg': ''}
{'mstRepoTestKey': 5, 'mstRepoKey': 1, 'mstTestKey': 2, 'EOrder': 5, 'Formula': '', 'VRule': '', 'VMsg': ''}
{'mstRepoTestKey': 6, 'mstRepoKey': 1, 'mstTestKey': 229, 'EOrder': 6, 'Formula': '', 'VRule': '', 'VMsg': ''}
{'mstRepoTestKey': 7, 'mstRepoKey': 1, 'mstTestKey': 786, 'EOrder': 7, 'Formula': '', 'VRule': '', 'VMsg': ''}
{'mstRepoTestKey': 8, 'mstRepoKey': 1, 'mstTestKey': 82, 'EOrder': 8, 'Formula': '', 'VRule': '', 'VMsg': ''}
{'mstRepoTestKey': 9, 'mstRepoKey': 1, 'mstTestKey': 849, 'EOrder': 9, 'Formula': '', 'VRule': '', 'VMsg': ''}
{'mstRepoTestKey': 10, 'mstRepoKey': 1, 'mstTestKey': 668, 'EOrder': 10, 'Formula': '', 'VRule': '', 'VMsg': ''} 



class Mstplitems(models.Model):


{'mstPLKey': 1, 'PLName': 'MATER PRICE LIST(31-12-2015)', 'PLDesc': 'MASTER Price list for patient'}
{'mstPLKey': 25, 'PLName': 'Appendix', 'PLDesc': 'Main Price list for patient'}
{'mstPLKey': 16, 'PLName': 'OPL', 'PLDesc': 'Other Path Labs'}
{'mstPLKey': 29, 'PLName': 'MD INDIA (PVT INSURANCE)', 'PLDesc': 'Main Price list for patient'}
{'mstPLKey': 30, 'PLName': 'Health India (Pvt Insurance Co', 'PLDesc': 'Main Price list for patient'}
{'mstPLKey': 31, 'PLName': 'LIC', 'PLDesc': 'Price List for LIC Client'}
{'mstPLKey': 32, 'PLName': 'Spurthi E Meditek', 'PLDesc': 'Main Price list for patient'}
{'mstPLKey': 18, 'PLName': 'SHREEJI HEALTH CHECK UP', 'PLDesc': 'MK HEALTH CHECK UP'}
{'mstPLKey': 19, 'PLName': 'Astha consultancy', 'PLDesc': 'Other Path Labs'}
{'mstPLKey': 23, 'PLName': 'Old Oncg', 'PLDesc': 'discont from 13 oct 2017'}
{'mstPLKey': 33, 'PLName': 'Cash Patient Price list', 'PLDesc': 'Main Price list for patient'}
{'mstPLKey': 38, 'PLName': 'Diabetic Club A/B Price list', 'PLDesc': 'Price list for diabetic club membership type A OR B'}
{'mstPLKey': 39, 'PLName': 'Diabetic Club C/D Price list', 'PLDesc': 'Price list for diabetic club membership type A OR B'}
{'mstPLKey': 40, 'PLName': 'Diabetic Club E Price list', 'PLDesc': 'Price list for diabetic club membership type A OR B'}
{'mstPLKey': 41, 'PLName': 'HEALTH ASSURE', 'PLDesc': 'MASTER Price list for patient'}
{'mstPLKey': 42, 'PLName': 'SUPREME IND', 'PLDesc': 'HEALTH CHECK UP OF SUPREME IND'}
{'mstPLKey': 43, 'PLName': 'Samparpan ', 'PLDesc': 'Main Price list for patient'}
{'mstPLKey': 44, 'PLName': 'MDNETWORX', 'PLDesc': 'Main Price list for patient'}
{'mstPLKey': 45, 'PLName': 'wellnext ', 'PLDesc': 'Main Price list for patient'}
{'mstPLKey': 46, 'PLName': 'ONCG ', 'PLDesc': 'Main Price list for patient'}
{'mstPLKey': 34, 'PLName': 'E MEDITEK (Pvt Insurance Co)', 'PLDesc': 'Main Price list for patient'}
{'mstPLKey': 35, 'PLName': 'ICICI Lombard GIC Ltd', 'PLDesc': 'Main Price list for patient'}
{'mstPLKey': 36, 'PLName': 'Medi Assist India TPA Pvt. Ltd', 'PLDesc': 'Main Price list for patient'}
{'mstPLKey': 37, 'PLName': 'UnitedHealthcare India Pvt Ltd', 'PLDesc': 'Main Price list for patient'}
{'mstPLKey': 48, 'PLName': 'Cash Patient B Price list', 'PLDesc': 'Main Price list for patient'}
{'mstPLKey': 50, 'PLName': 'Mahi Price list', 'PLDesc': 'Main Price list for patient'}