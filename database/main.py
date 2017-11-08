import  pandas as pd
import pymongo
def main():

    Phase1Cols = ['ID','DOB','SUBSECT','NAME','GOTHRAM','STAR-noPadham','Degree','Type','College','HEIGHT']

    inpFile = pd.read_csv('../outputData/treatedData.csv')[Phase1Cols]

    # Connect to DB. Work on the exception handlers. They dont seem to work
    print("Connecting to database...")
    print()
    try:
        conn = pymongo.MongoClient()
        print("Connected successfully!!!")
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s" % e)
    database='ssmatri'
    database = conn[database]

    print("Inserting the data into the Database...")
    print()
    for index, row in inpFile.iterrows():

        # Convert each row in the dataframe in to a dict
        record = row.to_dict()

        database.personInfo.update({"_id": record["ID"]}, {'$set': record}, upsert=True)

if __name__=='__main__':
    main()