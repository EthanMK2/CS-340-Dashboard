from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:48286/AAC' % (username, password))
        self.database = self.client['AAC']
        print("Connection Successful!")

# Method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary  
            return "True"
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        return "False"

# Method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            foundData = self.database.animals.find(data, {"_id": False}) # data should be dictionary, ignore id
            foundData = list(foundData)
            if len(foundData) <= 0:
                print("Read Unsuccessful. No data found.")
                return
            return foundData
        else:
            raise Exception("Nothing to read, because data parameter is empty")

# Method to implement the U in CRUD
    def update(self, searchQuery, updateData):
        if searchQuery is not None and updateData is not None:
            result = self.database.animals.update_one(searchQuery, updateData) # searchQuery/updataData both are dictionaries
            if result.matched_count == 0:
                print("Update Unsuccessful. Data Not found.")
                return
            print("Update Successful.", "Matched", result.matched_count, "Modified", result.modified_count)
            print(result.raw_result)
        else:
            raise Exception("Nothing to update, because parameter(s) is/are empty")

# Method to implement the D in CRUD
    def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_many(data) # data should be dictionary
            print("Deleted Count:", result.deleted_count)
        else:
            raise Exception("Nothing to delete, because data parameter is empty")