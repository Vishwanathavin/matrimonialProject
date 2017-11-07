import pandas as pd



def main():
    inpFile = pd.read_csv('../data/BI-October2017Chart.csv')
    print (inpFile.head())

if __name__=='__main__':
    main()
