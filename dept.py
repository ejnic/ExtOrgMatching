#### Department object to be used to work with program codes from SIS and Liaison ####
import re
import pandas as pd

class ExtOrg:
    def __init__(self, orgname, country, system, orgid):
        self.orgid = str(orgid)
        self.orgname = orgname.upper()
        self.country = country
        self.system = system
        self.cleanedname = orgname.upper()
        self.originalorgname = orgname.upper()
        self.orgtype = ''
        self.df = pd.DataFrame(columns=['orgid', 'orgname', 'country', 'system','cleanedname', 'originalname', 'orgtype'])

    def CleanOrgname(self):
        self.cleanedname = re.sub( r'[^\x00-\x7F]+', '', self.cleanedname)

        if re.search(r'(UNIVERSITY)', self.cleanedname):
            self.orgtype = self.orgtype + 'UNIVERSITY '
            self.cleanedname = re.sub(r'UNIVERSITY', ' ', self.cleanedname)

        if re.search(r'(UNIV$| UNIV |^UNIV )', self.cleanedname):
            self.orgtype = self.orgtype + 'UNIVERSITY '
            self.cleanedname = re.sub(r'(UNIV$| UNIV |^UNIV )', ' ', self.cleanedname)

        if re.search(r'(. U|. U .|^U .)', self.cleanedname):
            self.orgtype = self.orgtype + 'UNIVERSITY '
            self.cleanedname = re.sub(r'( U$| U |^U )', ' ', self.cleanedname)

        if re.search(r'COLLEGE', self.cleanedname):
            self.orgtype = self.orgtype + 'COLLEGE '
            self.cleanedname = re.sub(r'COLLEGE', '', self.cleanedname)

        if re.search(r'(COLL$| COLL |^COLL )', self.cleanedname):
            self.orgtype = self.orgtype + 'COLLEGE '
            self.cleanedname = re.sub(r'(COLL$| COLL |^COLL )', ' ', self.cleanedname)

        if re.search(r'(COL$| COL |^COL )', self.cleanedname):
            self.orgtype = self.orgtype + 'COLLEGE '
            self.cleanedname = re.sub(r'(COL$| COL |^COL )', ' ', self.cleanedname)

        if re.search(r'SCHOOL', self.cleanedname):
            self.orgtype = self.orgtype + 'SCHOOL '
            self.cleanedname = re.sub(r'SCHOOL', ' ', self.cleanedname)

        if re.search(r'(SCHL$| SCHL |^SCHL )', self.cleanedname):
            self.orgtype = self.orgtype + 'SCHOOL '
            self.cleanedname = re.sub(r'(SCHL$| SCHL |^SCHL )', ' ', self.cleanedname)

        if re.search(r'INSTITUTE', self.cleanedname):
            self.orgtype = self.orgtype + 'INSTITUTE '
            self.cleanedname = re.sub(r'INSTITUTE', ' ', self.cleanedname)

        if re.search(r'(INST$| INST |^INST )', self.cleanedname):
            self.orgtype = self.orgtype + 'INSTITUTE '
            self.cleanedname = re.sub(r'(INST$| INST |^INST )', ' ', self.cleanedname)

        if re.search(r'ACADEMY', self.cleanedname):
            self.orgtype = self.orgtype + 'ACADEMY '
            self.cleanedname = re.sub(r'ACADEMY', '', self.cleanedname)

        if re.search(r'( ACD$| ACD |^ACD )', self.cleanedname):
            self.orgtype = self.orgtype + 'ACADEMY '
            self.cleanedname = re.sub(r'( ACD$| ACD |^ACD )', ' ', self.cleanedname)

        if re.search(r'( ACAD$| ACAD |^ACAD )', self.cleanedname):
            self.orgtype = self.orgtype + 'ACADEMY '
            self.cleanedname = re.sub(r'( ACAD$| ACAD |^ACAD )', ' ', self.cleanedname)

        if re.search(r'CONSERVATORY', self.cleanedname):
            self.orgtype = self.orgtype + 'CONSERVATORY '
            self.cleanedname = re.sub(r'CONSERVATORY', ' ', self.cleanedname)

        self.cleanedname = re.sub(r'( OF | THE | ^THE | AND | AT | FOR | IN )', ' ', self.cleanedname)
        self.cleanedname = re.sub(r'(\'|,|-|&)', '', self.cleanedname)
        self.cleanedname = re.sub(r'( +)', ' ', self.cleanedname).strip()

        self.cleanedname = self.cleanedname + ' ' + self.orgtype.strip()

        self.df = self.df.append({'orgid':str(self.orgid), 'orgname':self.orgname, 'country':self.country, 'system':self.system,
            'cleanedname':self.cleanedname, 'originalname':self.originalorgname,
            'orgtype':self.orgtype}, ignore_index=True)

        if self.system == 'SIS':
            self.df.to_csv(r'C:\Users\ejnic\Google Drive Personal\Python\ClassesAndObjectsTutorial\siscleanedorgs.csv',
                       mode='a',index=False, header=False)
        else:
            self.df.to_csv(r'C:\Users\ejnic\Google Drive Personal\Python\ClassesAndObjectsTutorial\lcleanedorgs.csv',
                           mode='a', index=False, header=False)

        #['orgname', 'country', 'system', 'cleanedname', 'originalname', 'orgtype']

        #self.orgtype = self.orgtype + 'UNIVERSITY' if self.cleanedname.str.contains(r'UNIV')
'''
        self.df.loc[self.df['orgname'].str.contains(r'COLL'), 'orgtype'] = 'COLLEGE'
        self.df['orgname'] = self.df['orgname'].str.replace("COLLEGE", "")
        self.df.loc[self.df['orgname'].str.contains(r'SCHOOL'), 'orgtype'] = 'SCHOOL'
        self.df['orgname'] = self.df['orgname'].str.replace("\sSCHOOL", "")
        self.df.loc[self.df['orgname'].str.contains(r'INSTITUTE'), 'orgtype'] = 'INSTITUTE'
        self.df['orgname'] = self.df['orgname'].str.replace('INSTITUTE', '')
        self.df.loc[self.df['orgname'].str.contains(r'ACADEMY'), 'orgtype'] = 'ACADEMY'
        self.df['orgname'] = self.df['orgname'].str.replace('ACADEMY', '')
        self.df.loc[self.df['orgname'].str.contains(r'CONSERVATORY'), 'orgtype'] = 'CONSERVATORY'
        self.df['orgname'] = self.df['orgname'].str.replace('CONSERVATORY', ' ')

        self.df['orgname'] = self.df['orgname'].str.replace(" OF ", " ")
        self.df['orgname'] = self.df['orgname'].str.replace("OF ", " ")
        self.df['orgname'] = self.df['orgname'].str.replace(" AND ", " ")
        self.df['orgname'] = self.df['orgname'].str.replace(" & ", " ")
        self.df['orgname'] = self.df['orgname'].str.replace(" THE ", " ")
        self.df['orgname'] = self.df['orgname'].str.replace("THE ", "")
        self.df['orgname'] = self.df['orgname'].str.replace(".", "")
        self.df['orgname'] = self.df['orgname'].str.replace(",", "")
        self.df['orgname'] = self.df['orgname'].str.replace("'", "")
        self.df['orgtype'] = self.df['orgtype'].replace(np.nan, '')

        self.cleanedname = self.df['orgname'] + ' ' + self.df['orgtype']

        self.df['system'] = system
'''





class Department:


    # also called constructor
    def __init__(self, deptcd, deptdescr):
        self.deptcd = deptcd
        self.deptdescr = deptdescr
        self.dept  = self.deptcd[:4]
        print('init')

    def description(self):
        print('program info', self.deptcd, ' ', self.dept, ' ', self.deptdescr)

