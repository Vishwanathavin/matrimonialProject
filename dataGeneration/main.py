import pandas as pd

def renamingContent(inpFile):

    # rename the columns
    inpFile = inpFile.rename(columns={'REG.NO': 'ID',
                                      'DOB': 'DOB',
                                      'S.S': 'SUBSECT',
                                      'NAME': 'NAME',
                                      'GOTHRAM': 'GOTHRAM',
                                      'STAR': 'STAR',
                                      'HT': 'HEIGHT',
                                      'QUALIFICATION': 'QUALIFICATION',
                                      'JOB': 'JOB',
                                      'PLACE': 'PLACE',
                                      'INCOME': 'INCOME',
                                      'PA': 'PARENTS_ALIVE',
                                      'EXPECTATIONS_QUAL': 'EXPECTATIONS_QUALIFICATION',
                                      'EXPECTATIONS_JOB': 'EXPECTATIONS_JOB',
                                      'EXPECTATIONS_S.S': 'EXPECTATIONS_SUBSECT'
                                      })

    # rename data
    inpFile['SUBSECT'] = inpFile['SUBSECT'].replace('V','Vadamal')\
                                            .replace('B','Brahacharanam')\
                                            .replace('VT','Vathimal')\
                                            .replace('AS','Ashtasagasram')\
                                            .replace('GKL','Gurukkal')\
                                            .replace('CHOZ','Choziyal')\
                                            .replace('TB','TeluguBrahmin')\
                                            .replace('OB','OtherBrahmin')

    inpFile['PARENTS_ALIVE'] = inpFile['PARENTS_ALIVE'].replace('B','Both')\
                                                .replace('M','Mother Only')\
                                                .replace('F','Father Only')


    # Rename gothram and stars
    inpFile['GOTHRAM'] = inpFile['GOTHRAM'].replace('BH.WAJAM', 	'BHARADWAJAM')\
                                            .replace('KOUSIGA', 	'KOUSIGAM')\
                                            .replace('GARGEYA', 	'GARGA')\
                                            .replace('N.KASHYAPA', 	'NAITHRUPAKASHYAPA')\
                                            .replace('SH.MARSHANAM', 	'SHADMARSHANAM')\
                                            .replace('POURGUTHSA', 	'POURGUTSA')\
                                            .replace('POUR', 	'POURGUTSA')\
                                            .replace('UCHITHYA', 	'UTHSITHYA')\
                                            .replace('GOWSTHIRA', 	'GOWTHAMA')

    inpFile['STAR'] = inpFile['STAR'].str.replace('T.VADIRAI', 'THIRUVADHIRAI') \
        .str.replace('UTTHIRAM', 'UTHIRAM') \
        .str.replace('T.VONAM', 'THIRUVONAM') \
        .str.replace('P.POOSAM', 'PUNARPOOSAM') \
        .str.replace('M.SEERISHAM', 'MIRUGASEERISHAM') \
        .str.replace('TIRUVADIRAI', 'THIRUVADIRAI')\
        .str.replace('TIRUVONAM', 'THIRUVONAM')\
        .str.replace('T.VADHIRAI', 'THIRUVADIRAI')

    inpFile['STAR-noPadham'] = inpFile['STAR'].str.replace(' -4', '') \
        .str.replace(' -3', '') \
        .str.replace(' -2', '') \
        .str.replace(' -1', '')\
        .str.replace(' - 4', '')\
        .str.replace(' - 3', '')\
        .str.replace(' - 2', '')\
        .str.replace(' - 1', '')


    # Qualification : Get UG or PG

    searchFor = ['BE', 'B.TECH', 'B.COM', 'B.SC', 'BCA', 'BBA']
    inpFile.loc[inpFile['QUALIFICATION'].str.contains('|'.join(searchFor)), 'Degree'] = 'Undergraduate'

    searchFor = ['ME', 'M.TECH', 'M.COM', 'M.SC', 'MCA', 'MBA', 'CA']
    inpFile.loc[inpFile['QUALIFICATION'].str.contains('|'.join(searchFor)), 'Degree'] = 'Postgraduate'

    searchFor = ['PH.D']
    inpFile.loc[inpFile['QUALIFICATION'].str.contains('|'.join(searchFor)), 'Degree'] = 'Doctorate'

    searchFor = ['BE', 'B.TECH', 'ME', 'M.TECH', 'Ph.D','MBA','CA','ICWA']
    inpFile.loc[inpFile['QUALIFICATION'].str.contains('|'.join(searchFor)), 'Type'] = 'Professional'

    searchFor = ['MBBS']
    inpFile.loc[inpFile['QUALIFICATION'].str.contains('|'.join(searchFor)), 'Degree'] = 'Physician'

    searchFor = ['IIT', 'IIM']
    inpFile.loc[inpFile['QUALIFICATION'].str.contains('|'.join(searchFor)), 'College'] = 'IIT/IIM'

    # salary

    # Place of job

    return inpFile

def main():

    # read the file

    inpFile = pd.read_csv('./data/BI-October2017Chart.csv')

    inpFile=renamingContent(inpFile)

    inpFile.to_csv('treatedData.csv')
    print("Done boss")
if __name__ == '__main__':
    main()