from extorgclass import Department, ExtOrg
import sqlalchemy
import oraclecon as con
import pandas as pd
import os


engine = sqlalchemy.create_engine(con.strengine)
dfsis = pd.read_sql_query(con.sisorgs, engine)
if os.path.exists(r'C:\Users\Beth\PycharmProjects\ExtOrgMatchingFromHome\files\siscleanedorgs.csv'):
    os.remove(r'C:\Users\Beth\PycharmProjects\ExtOrgMatchingFromHome\files\siscleanedorgs.csv')

for index, row in dfsis.iterrows():
    externalorg = ExtOrg(dfsis.iloc[index]['orgname'], dfsis.iloc[index]['country'], 'SIS', dfsis.iloc[index]['orgid'])
    externalorg.CleanOrgname()
    dfsiscleaned = pd.DataFrame()
    dfsiscleaned = dfsiscleaned.append(
        {'orgid': str(externalorg.orgid), 'orgname': externalorg.orgname, 'country': externalorg.country,
         'system': externalorg.system, 'cleanedname': externalorg.cleanedname,
         'originalname': externalorg.originalorgname, 'orgtype': externalorg.orgtype}, ignore_index=True)

dfl = pd.read_sql_query(con.lorgs, engine)
if os.path.exists(r'C:\Users\Beth\PycharmProjects\ExtOrgMatchingFromHome\files\lcleanedorgs.csv'):
    os.remove(r'C:\Users\Beth\PycharmProjects\ExtOrgMatchingFromHome\files\lcleanedorgs.csv')

for index, row in dfl.iterrows():
    externalorg = ExtOrg(dfl.iloc[index]['orgname'], dfl.iloc[index]['country'], 'LIAISON', dfl.iloc[index]['orgid'])
    externalorg.CleanOrgname()
    dflcleaned = pd.DataFrame()
    dflcleaned = dflcleaned.append(
        {'orgid': str(externalorg.orgid), 'orgname': externalorg.orgname, 'country': externalorg.country,
         'system': externalorg.system, 'cleanedname': externalorg.cleanedname,
         'originalname': externalorg.originalorgname, 'orgtype': externalorg.orgtype}, ignore_index=True)



#externalorg = ExtOrg('Indiana University', 'USA', 'SIS', '12345')
#externalorg.CleanOrgname()
print(externalorg.orgtype)
print(externalorg.cleanedname)
print (externalorg.df.head(1))
#print(externalorg.orgtype)

#dept1 = Department('BIOL6', 'Biology Phd')
#dept2 = Department('CHEM5', 'Chemistry Masters')

# 2 ways to call a method
# Department.description(dept1)
#dept1.description()
#dept2.description()
