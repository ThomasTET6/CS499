# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username, password, HOST, PORT))
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 
            
    # Create method, the C in CRUD
    def create(self, data):
        """
        Insert a single document into the MongoDB collection.

        :param data: Dictionary containing the document to be inserted
        :return: True if insert is successful, False otherwise
        """
        # Validate input before attempting database operation
        if data is None:
            return False

        try:
            self.collection.insert_one(data)
            return True
        except PyMongoError as e:
            # Catch and report database-related errors without crashing the program
            print(f"Insert failed: {e}")
            return False


    # Read method, the R in CRUD
    def read(self, query):
        """
        Retrieve document(s) from the MongoDB collection that match a query.

        :param query: Dictionary specifying search criteria
        :return: List of matching documents, or an empty list if none are found
        """
        # Ensure a valid query is provided
        if query is None:
            return []

        try:
            # Use find() to allow retrieval of multiple documents
            cursor = self.collection.find(query)
            return list(cursor)
        except PyMongoError as e:
            # Handle database read errors gracefully
            print(f"Read failed: {e}")
            return []


    # Update method, the U in CRUD
    def update(self, query, new_values):
        """
        Update one or more documents in the MongoDB collection.

        :param query: Dictionary specifying which documents to update
        :param new_values: Dictionary containing update operators and values
        :return: Number of documents modified
        """
        # Validate inputs to prevent unintended updates
        if query is None or new_values is None:
            return 0

        try:
            result = self.collection.update_many(query, new_values)
            return result.modified_count
        except PyMongoError as e:
            # Capture update failures without interrupting program execution
            print(f"Update failed: {e}")
            return 0


    # Delete method, the D in CRUD
    def delete(self, query):
        """
        Remove one or more documents from the MongoDB collection.

        :param query: Dictionary specifying which documents to delete
        :return: Number of documents removed from the collection
        """
        # Ensure a valid query is provided before deleting data
        if query is None:
            return 0

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError as e:
            # Handle deletion errors safely
            print(f"Delete failed: {e}")
            return 0
