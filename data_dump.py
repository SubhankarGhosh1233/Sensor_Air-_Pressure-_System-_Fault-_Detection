import pymongo
import pandas as pd
import json
# 
client = pymongo.MongoClient("mongodb+srv://subhankar:Subhankar@cluster1.xsd7qsq.mongodb.net/")
## Define Database and Collection
dataBase_name = "apsSensor"

collection_name="Sensor"

data_file_path="aps_failure_training_set1.csv"
if __name__=="__main__":
    df=pd.read_csv(data_file_path)
    print(f"Rows and Columns: {df.shape}")


    #convert dataframe to .json so that we can dump these records in mongodb
    df.reset_index(drop=True,inplace=True)

    json_record =  list(json.loads(df.T.to_json()).values())
    print(json_record[0])  

    # insert converted json to mongodb
    client[dataBase_name][collection_name].insert_many(json_record)

print(client.list_database_names())
print(client[dataBase_name].list_collection_names())




